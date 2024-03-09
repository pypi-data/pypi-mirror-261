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

# Import local scripts models
from bigplanner.models.script import BigplannerScript as Item
from bigplanner.models.script import BigplannerScriptRequest as Request
from bigplanner.models.script import BigplannerScriptResponse as Response

# ---------------------------------------------------------
# Dynamic Loading Interface / EP Exposure
# ---------------------------------------------------------
TAG = "Scripts"
DESCRIPTION = "Scripts CLI API"
API_ORDER = 10

# ---------------------------------------------------------
# Loggers
# ---------------------------------------------------------

from agptools.logs import logger

log = logger(__name__)

# ---------------------------------------------------------
# Script CLI port implementation
# ---------------------------------------------------------
@main.group(context_settings=CONTEXT_SETTINGS)
@click.pass_obj
def script(env):
    """subcommands for manage scripts for bigplanner"""
    # banner("User", env.__dict__)


submodule = script


@submodule.command()
@click.option("--path", default=None)
@click.pass_obj
def create(env, path):
    """Create a new script for bigplanner"""
    # force config loading
    config.callback()

    # TODO: implement


@submodule.command()
@click.pass_obj
def read(env):
    """Find and list existing scripts for bigplanner"""
    # force config loading
    config.callback()

    # TODO: implement


@submodule.command()
@click.pass_obj
def update(env):
    """Update and existing scripts for bigplanner"""
    # force config loading
    config.callback()

    # TODO: implement


@submodule.command()
@click.pass_obj
def delete(env):
    """Delete an existing scripts for bigplanner"""
    # force config loading
    config.callback()

    # TODO: implement
