from pydantic import BaseModel, StrictStr, StrictInt, StrictBool
from typing import Union, Optional, Literal, List
from ergondata_executions.interfaces import APIBaseResponse
from ergondata_executions.v1.queue_item.interfaces import GetQueueItemsQueryParams, GetQueueItemQueryParams
from pydantic import Field

class AuthRequestPayload(BaseModel):
    username: StrictStr
    password: StrictStr
    organization_id: StrictStr = Field(alias="client_id")

    class Config:
        populate_by_name = True


class AuthSuccessResponsePayload(BaseModel):
    token: Optional[Union[StrictStr, None]]


class AuthResponsePayload(APIBaseResponse):
    token: Optional[StrictStr] = None



class TargetQueue(BaseModel):
    id: StrictStr
    alias: StrictStr

class Dispatcher(BaseModel):
    process_id: StrictStr
    task_id: StrictStr
    target_queues: List[TargetQueue]


class ReporterSourceQueue(BaseModel):
    id: StrictStr
    query: GetQueueItemsQueryParams = None
    add_pages: Union[StrictInt, Literal["all"], None] = None


class Reporter(BaseModel):
    process_id: StrictStr
    task_id: StrictStr
    source_queues: List[ReporterSourceQueue]


class Linear(BaseModel):
    process_id: StrictStr
    task_id: StrictStr


class SourceQueue(BaseModel):
    id: StrictStr
    query: GetQueueItemQueryParams = None


class Performer(BaseModel):
    process_id: StrictStr
    task_id: StrictStr
    source_queue: SourceQueue


class PerformerAndDispatcher(BaseModel):
    process_id: StrictStr
    task_id: StrictStr
    source_queue: SourceQueue
    target_queues: List[TargetQueue]


class TaskExecutionConfig(BaseModel):
    dispatcher: Dispatcher = None
    performer: Performer = None
    performer_and_dispatcher: PerformerAndDispatcher = None


class APIConfig(BaseModel):
    task_exec_config: Union[Performer, Dispatcher, PerformerAndDispatcher, Linear, Reporter] = None
    api_timeout: StrictInt = 10
    enable_logs: bool = True,
    log_file_path: StrictStr = None
    log_level: Literal["info", "debug", "error", "warning"] = "debug"
    preserve_logger_handler: StrictBool = True