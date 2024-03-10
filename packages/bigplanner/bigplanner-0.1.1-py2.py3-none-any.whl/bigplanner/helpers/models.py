"""
This module will help in creating synthetic or random data
for testing purposes.

- [ ] feed pytest pydantic data consistency
- [ ] feed FastAPI swagger examples
- [ ] other runtime uses

"""

from .general import new_uid
from .faker import fake, next_monotonic_uid

from ..models.enums import *
from ..models.inventory import *
from ..models.task import *
from ..models.script import *

# Other models that will be generated here
from ..models.resource import *
from ..models.planner import *


def random_item():
    return {
        "id": new_uid(),
        "name": fake.item_name(),
        #"name": fake.name(),
        #"description": fake.sentence(),
        "description": fake.paragraph(nb_sentences=1), 
    }

# ---------------------------------------------------------
# Item
# ---------------------------------------------------------

def random_planner_item():
    data = {
        **random_item(),
        'foo': 1,
        }
    return data
    
def random_planner_request():
    return {
        **random_item(),
        'foo': 1,
    }

def random_planner_response():
    return {
        **random_item(),
        'foo': 1,
    }


# ---------------------------------------------------------
# Activity
# ---------------------------------------------------------

def random_activity():
    data = {
        **random_item(),
        'start': random.randint(1, 10),
        'delta': random.randint(1, 10),
        'assigned': list(set([new_uid() for _ in range(random.randint(1, 3))])),
        'children': {},
    }
    data['end'] = data['start'] + data['delta']
    
    return data

def random_activity_group():
    activities = [random_activity() for _ in range(random.randint(1, 10))]
    
    return  {
        **random_activity(),        
        'children' : { a['id']: a for a in activities},
    }
    
# ---------------------------------------------------------
# Resource
# ---------------------------------------------------------
def random_resource():
    return {
        **random_item(),
        'profile': random.randint(1, 50),
    }
# ---------------------------------------------------------
# Dependencies
# ---------------------------------------------------------
def random_dependency():
    return {
        **random_item(),
        'source': new_uid(),
        'target': new_uid(),
        'kind': random.choice(list(TaskDependenceType)),
    }

# ---------------------------------------------------------
# Project
# ---------------------------------------------------------
def random_project():
    resources = [random_resource() for _ in range(random.randint(1, 10))]
    dep_1 = [random_dependency() for _ in range(random.randint(1, 10))]
    dep_2 = [random_dependency() for _ in range(random.randint(1, 10))]
    
    return {
        **random_activity(),
        'resources': { a['id']: a for a in resources},
        'dependences': {
            TaskDependenceGroup.HARD: { a['id']: a for a in dep_1},
            TaskDependenceGroup.SOFT: { a['id']: a for a in dep_2},
        }
    }
# ---------------------------------------------------------
# Tasks
# ---------------------------------------------------------
def random_task():
    return {
        **random_item(),
        'foo': 1,
    }

