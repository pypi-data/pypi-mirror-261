"""The CLI to interface with the Celestical Serverless Cloud."""
import logging
from typing import Optional
from typing_extensions import Annotated

import typer

from celestical.compose import (
    upload_compose,
    upload_images)
from celestical.docker_local import list_local_images
from celestical.helper import cli_panel, welcome_message
from celestical.configuration import LOGGING_LEVEL
from celestical.user import user_login, user_register

app = typer.Typer(pretty_exceptions_short=True,
                  no_args_is_help=True,
                  help=welcome_message,
                  rich_markup_mode="rich")

logging.basicConfig(encoding='utf-8', level=LOGGING_LEVEL)

# @app.callback(invoke_without_command=True)
@app.command()
def apps():
    """List all apps from current user."""
    cli_panel("(not available yet) Here will appear a recap of your apps activities")
    # TODO


@app.command()
def login() -> None:
    """Login to Parametry's Celestical Cloud Services via the CLI."""
    user_login()


@app.command()
def register():
    """Register as a user for Celestical Cloud Services via the CLI."""
    user_register()


@app.command()
def images():
    """ List all local docker images for you.
        Similar to 'docker image ls'.
    """
    table, err_msg = list_local_images()

    if table is None or err_msg != "":
        cli_panel("Docker service is [red]unaccessible[/red]\n\n"
                 +f"{err_msg}")
    else:
        cli_panel("The following are your local docker images\n"
                 +f"{table}")


@app.command()
def deploy(compose_path: Annotated[Optional[str], typer.Argument()] = "./"):
    """Compress and upload a Docker image to the Celestical Cloud."""
    # TODO in helpers: create repetitive code functions for
    # - printing information
    # - getting prompts

    # --- First the compose enrichment:
    # 1- find compose file
    # 2- enrich it
    enriched_compose = upload_compose(compose_path)

    # --- Upload images according to response
    # 1- read response, and feedback user on status
    # 2- if 200, select the list of images in response.
    # 3- compress concerned images
    # 4- upload concerned images
    # .. keep feedback to user whenever progress is made
    if enriched_compose is not None:
        cli_panel("At this point your image will upload: TODO")

    # TODO
    # upload_images(compose_path=compose_path)
    # upload_images()


