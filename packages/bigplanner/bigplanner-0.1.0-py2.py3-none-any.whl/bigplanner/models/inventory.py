"""
This file supports Inventory Pattern for bigplanner
"""

from datetime import datetime, timedelta
import random
import uuid
from dateutil.parser import parse

from typing import Union, List, Tuple, Dict
from typing_extensions import Annotated


from syncmodels.model import BaseModel, validator, Field
from syncmodels.mapper import *

# from models.generic.price import PriceSpecification
# from models.generic.schedules import OpeningHoursSpecificationSpec

from bigplanner.definitions import UID_TYPE

from .base import *
from ..ports import *

# TODO: extend model corpus classes, a.k.a: the pydantic based thesaurus foundations classes
# TODO: this classes may be included in the main thesaurus when project is stable
# TODO: and others projects can benefit from them, making the thesaurus bigger and more powerful

# ---------------------------------------------------------
# InventoryItem
# ---------------------------------------------------------
# TODO: Inherit from smartmodels.model.inventory (or similar) 
class BigplannerInventory(Item):
    """A Bigplanner InventoryItem model"""
    pass

    

# ---------------------------------------------------------
# InventoryRequest
# ---------------------------------------------------------
class BigplannerInventoryRequest(Request):
    
    """A Bigplanner request to inventory manager.
    Contains all query data and search parameters.
    """
    pass
# ---------------------------------------------------------
# InventoryResponse
# ---------------------------------------------------------
class BigplannerInventoryResponse(Response):
    
    """A Bigplanner response to inventory manager.
    Contains the search results given by a request.
    """
    data: Dict[UID_TYPE, BigplannerInventory] = {}







