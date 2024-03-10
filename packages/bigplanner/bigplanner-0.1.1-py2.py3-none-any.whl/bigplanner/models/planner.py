"""
This file supports Inventory Pattern for bigplanner
"""

from datetime import datetime, timedelta
import random
import uuid
from dateutil.parser import parse

from typing import Union, List, Tuple, Dict
from typing_extensions import Annotated


from syncmodels.model import BaseModel, field_validator, Field
from syncmodels.mapper import *

# from models.generic.price import PriceSpecification
# from models.generic.schedules import OpeningHoursSpecificationSpec

from .base import *
from .inventory import PlannerItem
from .resource import PlannerResource as Resource
from .enums import TaskDependenceType, TaskDependenceGroup

# TODO: extend model corpus classes, a.k.a: the pydantic based thesaurus foundations classes
# TODO: this classes may be included in the main thesaurus when project is stable
# TODO: and others projects can benefit from them, making the thesaurus bigger and more powerful


# ---------------------------------------------------------
# PlannerActivity
# ---------------------------------------------------------
# TODO: Inherit from smartmodels.model.app (or similar)
class Activity(PlannerItem):
    """A Bigplanner Activity model"""

    start: int = Field(
        0,
        description="task start",
        examples=[
            0,
            2,
        ],
    )
    delta: int = Field(
        1,
        description="task duration",
        examples=[
            1,
            2,
            5,
        ],
    )
    end: int = Field(
        0,
        description="task end",
        examples=[
            0,
            2,
        ],
    )
    assigned: List[UID_TYPE] = Field(
        [],
        description="task start",
        examples=[
            [0, 1],
            [2],
        ],
    )
    children: Dict[UID_TYPE, "Activity"] = {}


# ---------------------------------------------------------
# PlannerDependence
# ---------------------------------------------------------
# TODO: Inherit from smartmodels.model.app (or similar)
class ActivityDependence(Item):
    """Dependencies between Activities model"""

    source: UID_TYPE = Field(
        0,
        description="left side of dependence",
        examples=[
            0,
            1,
        ],
    )
    target: UID_TYPE = Field(
        1,
        description="right side of dependence",
        examples=[
            2,
            3,
        ],
    )
    kind: TaskDependenceType = Field(
        TaskDependenceType.END_START,
        description="type of dependence between activities",
        examples=[
            TaskDependenceType.END_START,
            TaskDependenceType.START_START,
        ],
    )


# ---------------------------------------------------------
# PlannerDependence
# ---------------------------------------------------------
# TODO: Inherit from smartmodels.model.app (or similar)
class Project(Activity):
    """A Bigplanner Project model"""

    resources: Dict[UID_TYPE, Resource] = Field(
        {},
        description="A dict of available resources for a project",
    )
    dependences: Dict[TaskDependenceGroup, Dict[UID_TYPE, ActivityDependence]] = Field(
        {},
        description="activity dependencies grouped by HARD (user) or SOFT (algorithm) type",
    )


# # ---------------------------------------------------------
# # A base BigplannerRequest
# # ---------------------------------------------------------
# class PlannerActivityRequest(Request):
#     """A Bigplanner request to task manager.
#     Contains all query data and search parameters.
#     """

#     pass


# # ---------------------------------------------------------
# # A base BigplannerResponse
# class PlannerActivityResponse(Response):
#     """A Bigplanner response to task manager.
#     Contains the search results given by a request.
#     """

#     data: Dict[UID_TYPE, Item] = {}
