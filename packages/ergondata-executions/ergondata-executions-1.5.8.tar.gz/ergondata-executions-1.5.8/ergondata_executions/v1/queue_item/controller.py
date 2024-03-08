import requests

from ergondata_executions.v1.auth.controller import AuthController
from ergondata_executions.v1.queue_item.interfaces import *
from ergondata_executions.v1.decorators import *

class QueueItemController:

    CREATE_QUEUE_ITEM_URL = "processes/{0}/queues/{1}/items"
    GET_QUEUE_ITEM_URL = "processes/{0}/queues/{1}/item"
    GET_QUEUE_ITEMS_URL = "processes/{0}/queues/{1}/items"
    UPDATE_QUEUE_ITEM_URL = "processes/{0}/queues/{1}/items/{2}"

    def __init__(self, api_client: AuthController):
        self.api_client = api_client

    @api_request(log_message="Creating queue item", out_schema=CreateQueueItemResponsePayload)
    def create_queue_item(
        self,
        process_id: StrictStr,
        queue_id: StrictStr,
        payload: Any,
        external_id: StrictStr = None,
        processing_status_id: Union[StrictStr, None] = "pending",
        processing_exception_id: StrictStr = None,
        processing_priority_id: StrictStr = None,
        processing_status_message: StrictStr = None,
        tags: List[StrictStr] = None

    ) -> CreateQueueItemResponsePayload:
        res: Any = requests.post(
            url=f"{self.api_client.ROOT_URL}{self.CREATE_QUEUE_ITEM_URL.format(process_id, queue_id)}",
            json=CreateQueueItemRequestPayload(
                external_id=external_id,
                payload=payload,
                processing_status_id=processing_status_id,
                processing_priority_id=processing_priority_id,
                processing_status_message=processing_status_message,
                processing_exception_id=processing_exception_id,
                tags=tags
            ).model_dump(),
            headers=self.api_client.exec_header if self.api_client.exec_token else self.api_client.auth_header,
            timeout=self.api_client.timeout
        )
        return res

    @api_request(log_message="Getting queue item", out_schema=GetQueueItemResponsePayload, queue_item=True)
    def get_queue_item(
        self,
        process_id: StrictStr,
        queue_id: StrictStr,
        external_id: StrictStr = None,
        priority_id__in: List[StrictStr] = None,
        tags__contains: List[StrictStr] = None,
        tags__exact: List[StrictStr] = None
    ) -> GetQueueItemResponsePayload:
        res: Any = requests.get(
            url=f"{self.api_client.ROOT_URL}{self.GET_QUEUE_ITEM_URL.format(process_id, queue_id)}",
            params=GetQueueItemQueryParams(
                external_id=external_id,
                priority_id__in=priority_id__in,
                tags__contains=tags__contains,
                tags__exact=tags__exact
            ).model_dump(),
            headers=self.api_client.exec_header if self.api_client.exec_token else self.api_client.auth_header
        )
        return res

    @api_request(log_message="Updating queue item", out_schema=UpdateQueueItemResponsePayload)
    def update_queue_item(
        self,
        process_id: StrictStr,
        queue_item_id: StrictStr,
        queue_id: StrictStr,
        payload: Any = None,
        processing_status_id: StrictStr = None,
        processing_exception_id: StrictStr = None,
        processing_status_message: StrictStr = None,
        tags: List[StrictStr] = None
    ) -> UpdateQueueItemResponsePayload:
        res: Any = requests.put(
            url=f"{self.api_client.ROOT_URL}{self.UPDATE_QUEUE_ITEM_URL.format(process_id, queue_id, queue_item_id)}",
            json=UpdateQueueItemRequestPayload(
                payload=payload,
                processing_status_id=processing_status_id,
                processing_exception_id=processing_exception_id,
                processing_status_message=processing_status_message,
                tags=tags
            ).model_dump(),
            headers=self.api_client.exec_header if self.api_client.exec_token else self.api_client.auth_header
        )
        return res

    @api_request(log_message="Getting queue items", out_schema=GetQueueItemsResponsePayload, log_response=False)
    def get_queue_items(
        self,
        process_id: StrictStr,
        queue_id: StrictStr,
        query_params: GetQueueItemsQueryParams = None
    ):
        query_params = query_params.to_dict() if query_params else None

        res: Any = requests.get(
            url=f"{self.api_client.ROOT_URL}{self.GET_QUEUE_ITEMS_URL.format(process_id, queue_id)}",
            params=query_params,
            headers=self.api_client.exec_header if self.api_client.exec_token else self.api_client.auth_header
        )
        return res