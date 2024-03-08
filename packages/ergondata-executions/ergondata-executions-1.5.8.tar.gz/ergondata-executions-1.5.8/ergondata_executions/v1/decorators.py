import wrapt
from typing import Type, Union, List
from pydantic import StrictBool, BaseModel
from ergondata_executions.v1.api_exceptions import *
from ergondata_executions.v1.queue_item.interfaces import (
    CreateQueueItemRequestPayload,
    UpdateQueueItemRequestPayload,
    GetQueueItemsResponsePayload,
    GetQueueItemsReporter
)
from requests import Response

def api_request(
    out_schema: Type[BaseModel],
    exec_token: StrictBool = False,
    queue_item: StrictBool = None,
    log_message: StrictStr = None,
    log_response: StrictBool = True
):
    @wrapt.decorator
    def wrapper(wrapped, instance, args, kwargs):

        self = instance
        if log_message:
            self.api_client.logger.info(log_message.format(**kwargs))

        response = wrapped(*args, **kwargs)

        if not isinstance(response, Response):
            return

        if response.status_code == 200:

            response = response.json()
            clean_response = response

            data = out_schema(**response)

            if log_response and not exec_token:
                self.api_client.logger.info(data)

            if exec_token:

                self.api_client.set_task_execution(
                    process_id=self.api_client.config.task_exec_config.process_id,
                    exec_token=data.exec_token,
                    task_id=data.data.task.id,
                    task_execution_id=data.data.id
                )

                if log_response:
                    del clean_response['exec_token']
                    self.api_client.logger.info(out_schema(**clean_response))

            if queue_item:
                self.api_client.queue_item = data.data

        else:
            data = out_schema(**response.json())
            self.api_client.logger.error(data)

        return data

    return wrapper


def func_logger(log_in: StrictBool = True, log_out: StrictBool = True, log_args: StrictBool = True):
    @wrapt.decorator
    def wrapper(wrapped, instance, args, kwargs):

        self = instance
        ergon = self.ergon
        function_id = wrapped.__name__

        if log_in:

            arg_str = ', '.join(f"{k}={v}" for k, v in zip(wrapped.__code__.co_varnames, args))
            arg_str += ', '.join(f"{k}={v}" for k, v in kwargs.items())

            if arg_str and log_args:
                message = f"Stepped in {function_id} with arguments: {arg_str}"
            else:
                message = f"Stepped in {function_id}"

            ergon.write_tk_exec_log(
                message=message,
                level="info",
                task_step_id=function_id
            )

        result = wrapped(*args, **kwargs)

        if log_out:
            ergon.write_tk_exec_log(
                message=f"Stepped out {function_id}",
                level="info",
                task_step_id=function_id
            )

        return result

    return wrapper

@wrapt.decorator
def run_decorator(wrapped, instance, args, kwargs):

    self = instance

    self.ergon.write_tk_exec_log(
        message="Running main method",
        task_step_id="main",
        level="info"
    )

    try:
        result = wrapped(*args, **kwargs)
        self.ergon.update_task_execution(processing_status_id="success")
        self.ergon.write_tk_exec_log(message="Stepped out of main method with success. Task execution finished.")
        return result
    except TaskException:
        pass
    except SystemExit:
        pass
    except BaseException as e:
        self.ergon.write_tk_exec_log(message=str(e), level="error")
        raise TaskFailed(ergon=self.ergon, processing_status_message=str(e))


def run(wrapped_function=None):
    # Check if the decorator is called without parentheses
    if wrapped_function is None:
        return run_decorator
    else:
        return run_decorator(wrapped_function)


def create_queue_item(
    target_alias: StrictStr = None,
    stop_on_failure_exception_id: StrictStr = False
):

    @wrapt.decorator
    def wrapper(wrapped, instance, args, kwargs):

        self = instance
        target_queue = None

        try:


            # Access the item argument if available
            result: CreateQueueItemRequestPayload = wrapped(*args, **kwargs)

            if not result:
                return

            for queue in self.ergon.api_client.config.task_exec_config.target_queues:
                if queue.alias == target_alias:
                    target_queue = queue.id
                    break
                else:
                    target_queue = None

            if not target_queue:
                raise TaskFailed(ergon=self.ergon, processing_status_message="Improperly configured target queue id")

            self.ergon.create_queue_item(
                process_id=self.ergon.api_client.config.task_exec_config.process_id,
                queue_id=target_queue,
                processing_status_message=result.processing_status_message,
                payload=result.payload,
                external_id=result.external_id,
                processing_priority_id=result.processing_priority_id,
                processing_status_id=result.processing_status_id,
                tags=result.tags
            )

            return result

        except DispatcherQIException:
            self.ergon.write_tk_exec_log(message=f"Queue item raised an exception", level="error")
            if stop_on_failure_exception_id:
                raise TaskException(
                    ergon=self.ergon,
                    processing_status_message=f"Stopping task execution due to failure to create one item.",
                    task_exception_id=stop_on_failure_exception_id
                )
        except DispatcherQISysError:
            self.ergon.write_tk_exec_log(message=f"Queue item raised a system exception", level="error")
            if stop_on_failure_exception_id:
                raise TaskException(
                    ergon=self.ergon,
                    processing_status_message=f"Stopping task execution due to failure to create one item.",
                    task_exception_id=stop_on_failure_exception_id
                )

        except DispatcherQIBusException:
            self.ergon.write_tk_exec_log(message=f"Queue item raised a business exception", level="error")
            if stop_on_failure_exception_id:
                raise TaskException(
                    ergon=self.ergon,
                    processing_status_message=f"Stopping task execution due to failure to create one item.",
                    task_exception_id=stop_on_failure_exception_id
                )

        except TaskException:
            sys.exit()
        except KeyboardInterrupt:
            raise TaskFailed(ergon=self.ergon, processing_status_message="Keyboard interruption")
        except BaseException as e:
            self.ergon.write_tk_exec_log(message=f"Queue item raised an unknown error {e}", level="error")
            if stop_on_failure_exception_id:
                raise TaskException(
                    ergon=self.ergon,
                    processing_status_message=f"Stopping task execution due to failure to create one item => {str(e)}",
                    task_exception_id=stop_on_failure_exception_id
                )

    return wrapper

@wrapt.decorator
def get_queue_item_decorator(wrapped, instance, args, kwargs):

    self = instance
    queue_id = self.ergon.api_client.config.task_exec_config.source_queue.id
    query = self.ergon.api_client.config.task_exec_config.source_queue.query

    self.ergon.write_tk_exec_log(message=f"Reading queue items from {queue_id}")

    while True:

        try:

            queue_item = self.ergon.get_queue_item(
                process_id=self.ergon.api_client.config.task_exec_config.process_id,
                queue_id=queue_id,
                tags__exact=query.tags__exact,
                tags__contains=query.tags__contains,
                external_id=query.external_id,
                priority_id__in=query.priority_id__in
            )

            if not queue_item.data:
                self.ergon.write_tk_exec_log(message=f"No more queue items to read from {queue_id}")
                break

            result: UpdateQueueItemRequestPayload = wrapped(queue_item, *args, **kwargs)

            self.ergon.update_queue_item(
                process_id=self.ergon.api_client.config.task_exec_config.process_id,
                queue_id=queue_id,
                queue_item_id=queue_item.data.id,
                processing_status_id=result.processing_status_id,
                processing_status_message=result.processing_status_message,
                processing_exception_id=result.processing_exception_id,
                payload=result.payload
            )

            self.ergon.write_tk_exec_log(message=f"Queue item {queue_item.data.id} processed with success")

        except PerformerQIException:
            pass
        except PerformerQISysError:
            pass
        except PerformerQIBusException:
            pass
        except TaskException:
            sys.exit()
        except BaseException as e:
            self.ergon.write_tk_exec_log(message=str(e), level="error")
            self.ergon.update_queue_item(
                process_id=self.ergon.api_client.config.task_exec_config.process_id,
                queue_item_id=self.ergon.api_client.queue_item.id,
                processing_status_id="system_error",
                processing_status_message=str(e),
                queue_id=queue_id
            )


def get_next_item(wrapped_function=None):
    # Check if the decorator is called without parentheses
    if wrapped_function is None:
        return get_queue_item_decorator
    else:
        return get_queue_item_decorator(wrapped_function)


@wrapt.decorator
def get_queue_items_decorator(wrapped, instance, args, kwargs):

    self = instance
    source_queues = self.ergon.api_client.config.task_exec_config.source_queues
    data: Union[GetQueueItemsReporter, List] = []

    for queue in source_queues:

        self.ergon.write_tk_exec_log(message=f"Reading data from queue {queue.id}")

        queue_items = self.ergon.get_queue_items(
            process_id=self.ergon.api_client.config.task_exec_config.process_id,
            queue_id=queue.id,
            query_params=queue.query,
        )

        queue_items_obj = GetQueueItemsReporter(
            queue_id=queue.id,
            data=queue_items.data
        )

        self.ergon.write_tk_exec_log(message=f"Data obtained with success {queue.id}")

        if queue_items.pagination.has_next_page:

            if queue.add_pages and isinstance(queue.add_pages, int) and queue.add_pages > 0:

                self.ergon.write_tk_exec_log(message=f"There are more pages left to query. {queue.id}")

                for i in range(int(queue.query.page_size), queue.add_pages):

                    queue.query.page = i + 1
                    self.ergon.write_tk_exec_log(message=f"Getting data for page: {queue.query.page}")

                    queue_items: GetQueueItemsResponsePayload = self.ergon.get_queue_items(
                        process_id=self.ergon.api_client.config.task_exec_config.process_id,
                        queue_id=queue.id,
                        query_params=queue.query
                    )

                    queue_items_obj.data.extend(queue_items.data)

                    if not queue_items.pagination.has_next_page:
                        self.ergon.write_tk_exec_log(message=f"No more pages left paginate")
                        break

            elif queue.add_pages == "all":

                self.ergon.write_tk_exec_log(message=f"Pagination set to all. Starting pagination procedure.")

                while True:

                    queue.query.page = queue.query.page + 1
                    self.ergon.write_tk_exec_log(message=f"Getting data for page: {queue.query.page}")

                    queue_items: GetQueueItemsResponsePayload = self.ergon.get_queue_items(
                        queue_id=queue.id,
                        process_id=self.ergon.api_client.config.task_exec_config.process_id,
                        query_params=queue.query
                    )

                    queue_items_obj.data.extend(queue_items.data)

                    if not queue_items.pagination.has_next_page:
                        self.ergon.write_tk_exec_log(message=f"No more pages left paginate")
                        break
            else:
                pass
        else:
            pass

        data.append(queue_items_obj)

    return wrapped(data, *args, **kwargs)


def get_queue_items(wrapped_function=None):
    # Check if the decorator is called without parentheses
    if wrapped_function is None:
        return get_queue_items_decorator
    else:
        return get_queue_items_decorator(wrapped_function)

