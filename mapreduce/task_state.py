from enum import Enum


class TaskState(Enum):
    WORKING = 1
    COMPLETED = 2
    EXCEPTION = -1
