"""
This module contains all Models used to interact with the outside world
no matter is it comes from an API REST interface or CLI interface.

In CLI case, a pretty print method will enrich the console output.
"""

from datetime import datetime, timedelta
from dateutil.parser import parse

from enum import Enum
from typing import Union, List, Tuple
from typing_extensions import Annotated


from syncmodels.model import BaseModel, validator, Field
from syncmodels.mapper import *

# from models.generic.price import PriceSpecification
# from models.generic.schedules import OpeningHoursSpecificationSpec


# ---------------------------------------------------------
# Enum Definitions
# ---------------------------------------------------------
class ExampleEnum(str, Enum):
    """Enum representing something ..."""

    # a reference to the specification
    # https://github.com/smart-data-models/dataModel.TourismDestinations/blob/master/TouristProfile/schema.json
    SINGLE = "Single"
    # SINGLE_PARENT = "Single parent"  # TODO: evaluate this future extension
    COUPLE = "Couple"
    FAMILY = "Family"
    FRIENDS = "Friends"
    # FRIENDS_RELATIVES = "Friends/Relatives" # TODO: evaluate this future extension


class NumberedExampleEnum(int, Enum):
    """Enum representing a numeric sorted something ..."""

    NONE: Annotated[int, "lowest"] = 0
    VERY_LOW = 1
    LOW = 2
    MEDIUM = 3
    HIGH = 4
    VERY_HIGHT: Annotated[int, "highest"] = 5


# ---------------------------------------------------------
# App Config Preferences Models
# ---------------------------------------------------------
class MyAppPreferences(BaseModel):
    name: str = Field(
        default="no_name",
        description="A name for this user app preference",
        examples=[
            "A travel to Roma",
            "Second Visit to Budapest",
        ],
    )

    alternatives: int = Field(
        default=1,
        description="number of max alternatives to compute for the same preferences",
        ge=1,
    )
    temperature: float = 0.5
