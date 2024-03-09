"""
This file supports Script Pattern for bigplanner
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
# ScriptItem
# ---------------------------------------------------------
class BigplannerScript(Item):
    """A Bigplanner Script model"""
    pass

    

# ---------------------------------------------------------
# ScriptRequest
# ---------------------------------------------------------
class BigplannerScriptRequest(Request):
    
    """A Bigplanner request to Script manager.
    Contains all query data and search parameters.
    """
    pass
# ---------------------------------------------------------
# ScriptResponse
# ---------------------------------------------------------
class BigplannerScriptResponse(Response):
    
    """A Bigplanner response to Script manager.
    Contains the search results given by a request.
    """
    data: Dict[UID_TYPE, BigplannerScript] = {}






