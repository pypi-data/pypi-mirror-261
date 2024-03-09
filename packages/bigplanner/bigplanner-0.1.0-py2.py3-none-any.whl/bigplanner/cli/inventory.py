# import re
# import os
# import yaml

import click

# from bigplanner.helpers import *
from bigplanner.cli.main import main, CONTEXT_SETTINGS
from bigplanner.cli.config import config


from bigplanner.definitions import DEFAULT_LANGUAGE, UID_TYPE

# TODO: include any logic from module core
# Examples
# from bigplanner.models import *
# from bigplanner.logic import Tagger
# from syncmodels.storage import Storage

# Import local inventory models
from bigplanner.models.inventory import BigplannerInventory as Item
from bigplanner.models.inventory import BigplannerInventoryRequest as Request
from bigplanner.models.inventory import BigplannerInventoryResponse as Response

# ---------------------------------------------------------
# Dynamic Loading Interface / EP Exposure
# ---------------------------------------------------------
TAG = "Inventory"
DESCRIPTION = "Inventory CLI API"
API_ORDER = 10

# ---------------------------------------------------------
# Loggers
# ---------------------------------------------------------

from agptools.logs import logger

log = logger(__name__)

# ---------------------------------------------------------
# Inventory CLI router
# ---------------------------------------------------------
@main.group(context_settings=CONTEXT_SETTINGS)
@click.pass_obj
def inventory(env):
    """subcommands for manage inventory for bigplanner"""
    # banner("User", env.__dict__)


submodule = inventory


@submodule.command()
@click.option("--path", default=None)
@click.pass_obj
def create(env, path):
    """Create a new inventory item for bigplanner"""
    # force config loading
    config.callback()

    # TODO: implement


@submodule.command()
@click.pass_obj
def read(env):
    """Find and list existing inventory items for bigplanner"""
    # force config loading
    config.callback()

    # TODO: implement


@submodule.command()
@click.pass_obj
def update(env):
    """Update and existing inventory item for bigplanner"""
    # force config loading
    config.callback()

    # TODO: implement


@submodule.command()
@click.pass_obj
def delete(env):
    """Delete an existing inventory item for bigplanner"""
    # force config loading
    config.callback()

    # TODO: implement
