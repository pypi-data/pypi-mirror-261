from ergondata_executions.interfaces import *
from ergondata_executions.v1.queue.interfaces import Queue, QueueItemStatus
from ergondata_executions.v1.task_execution.interfaces import TaskExecution
from ergondata_executions.v1.queue_exception.interfaces import QueueException
from ergondata_executions.v1.queue_priority.interfaces import QueuePriority
from typing import Any
from ergondata_executions.interfaces import APIPagination

class QueueItem(BaseModel):
    id: StrictStr
    processing_status: QueueItemStatus
    payload: Any
    queue: Queue
    retries_within_count: StrictInt
    retries_outside_count: StrictInt
    created_at: datetime
    processing_status_message: Optional[StrictStr] = None
    processing_exception: Optional[QueueException] = None
    processing_priority: Optional[QueuePriority] = None
    external_id: Optional[StrictStr] = None
    task_producer_execution: Optional[TaskExecution] = None
    task_consumer_execution: Optional[TaskExecution] = None
    tags: Optional[List[StrictStr]] = None
    started_at: Optional[datetime] = None
    finished_at: Optional[datetime] = None


class CreateQueueItemRequestPayload(BaseModel):
    payload: Any
    external_id: Optional[StrictStr] = None
    processing_status_id: Optional[Literal["pending", "success", "system_error", "business_exception"]] = "pending"
    processing_status_message: Optional[StrictStr] = None
    processing_exception_id: Optional[StrictStr] = None
    processing_priority_id: Optional[StrictStr] = None
    tags: Optional[List[StrictStr]] = None


class CreateQueueItemResponsePayload(APIBaseResponse):
    data: Optional[Union[QueueItem, None]] = None


class GetQueueItemQueryParams(BaseModel):
    priority_id__in: Optional[list[StrictStr]] = None
    external_id: Optional[StrictStr] = None
    tags__contains: Optional[List[StrictStr]] = None
    tags__exact: Optional[List[StrictStr]] = None


class GetQueueItemResponsePayload(APIBaseResponse):
    data: Optional[QueueItem] = None


class UpdateQueueItemRequestPayload(BaseModel):
    payload: Optional[Any] = None
    processing_status_id: Optional[Literal["success", "system_error", "business_exception"]] = None
    processing_status_message: Optional[StrictStr] = None
    processing_exception_id: Optional[StrictStr] = None
    tags: Optional[List[StrictStr]] = None



class UpdateQueueItemResponsePayload(CreateQueueItemResponsePayload):
    pass


class GetQueueItemsQueryParams(BaseModel):
    page: StrictStr = 1
    page_size: StrictStr = 10
    id: Optional[StrictStr] = None
    id__in: Optional[List[StrictStr]] = None
    external_id: Optional[StrictStr] = None
    external_id__in: Optional[List[StrictStr]] = None
    external_id__contains: Optional[StrictStr] = None
    tags__contains: Optional[StrictStr] = None
    tags__exact: Optional[List[StrictStr]] = None
    processing_priority_id: Optional[StrictStr] = None
    processing_priority_id__in: Optional[list[StrictStr]] = None
    processing_status_id: Optional[StrictStr] = None
    processing_status_id__in: Optional[List[StrictStr]] = None
    task_producer_execution_id: Optional[StrictStr] = None
    task_producer_execution_id__in: Optional[List[StrictStr]] = None
    task_consumer_execution_id: Optional[StrictStr] = None
    task_consumer_execution_id__in: Optional[List[StrictStr]] = None
    task_producer_execution__worker_id: Optional[StrictStr] = None
    task_producer_execution__worker_id__in: Optional[List[StrictStr]] = None
    task_consumer_execution__worker_id: Optional[StrictStr] = None
    task_consumer_execution__worker_id__in: Optional[List[StrictStr]] = None
    produced_by_user_id: Optional[StrictStr] = None
    produced_by_user_id__in: Optional[List[StrictStr]] = None
    consumed_by_user_id: Optional[StrictStr] = None
    consumed_by_user_id__in: Optional[List[StrictStr]] = None
    processing_exception_id: Optional[StrictStr] = None
    processing_exception_id__in: Optional[List[StrictStr]] = None
    processing_status_message__contains: Optional[StrictStr] = None
    max_retries_within_execution: Optional[StrictInt] = None
    max_retries_within_execution__lt: Optional[StrictInt] = None
    max_retries_within_execution__lte: Optional[StrictInt] = None
    max_retries_within_execution__gt: Optional[StrictInt] = None
    max_retries_within_execution__gte: Optional[StrictInt] = None
    max_retries_outside_execution: Optional[StrictInt] = None
    max_retries_outside_execution__gt: Optional[StrictInt] = None
    max_retries_outside_execution__gte: Optional[StrictInt] = None
    max_retries_outside_execution__lt: Optional[StrictInt] = None
    max_retries_outside_execution__lte: Optional[StrictInt] = None
    created_at__lte: Optional[datetime] = None
    created_at__lt: Optional[datetime] = None
    created_at__gt: Optional[datetime] = None
    created_at__gte: Optional[datetime] = None
    started_at__lte: Optional[datetime] = None
    started_at__lt: Optional[datetime] = None
    started_at__gt: Optional[datetime] = None
    started_at__gte: Optional[datetime] = None
    finished_at__lte: Optional[datetime] = None
    finished_at__lt: Optional[datetime] = None
    finished_at__gt: Optional[datetime] = None
    finished_at__gte: Optional[datetime] = None
    payload: Optional[StrictStr] = None
    payload__contains: Optional[StrictStr] = None

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def to_dict(self):

        original_dict = self.dict()
        new_dict = original_dict.copy()
        public_keys = original_dict.items()

        for key, value in public_keys:
            if isinstance(value, list):
                new_dict[key] = ','.join(value)

        return new_dict

class GetQueueItemsResponsePayload(APIBaseResponse):
    data: Optional[List[QueueItem]] = None
    pagination: Optional[APIPagination] = None


class GetQueueItemsReporter(BaseModel):
    queue_id: StrictStr
    data: List[QueueItem]