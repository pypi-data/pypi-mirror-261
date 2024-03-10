from enum import IntEnum


class TaskDependenceType(IntEnum):
    END_START = 0
    START_START = 1
    END_END = 2
    START_END = 3


class TaskDependenceGroup(IntEnum):
    HARD = 0
    SOFT = 1
