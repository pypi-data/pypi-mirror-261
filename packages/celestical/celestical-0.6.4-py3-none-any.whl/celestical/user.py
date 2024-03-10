""" user related functions

    This file holds the routines to login, register
    and manage user data and configuration.
"""
import logging
import getpass
from datetime import datetime

from celestical.api import (
    ApiClient,
    AuthApi,
    ApiException,
    UserCreate)
from celestical.configuration import (
    apiconf,
    load_config,
    save_config,
    LOGGING_LEVEL)
from celestical.helper import (
    cli_panel,
    prompt_user,
    confirm_user)

logging.basicConfig(encoding='utf-8', level=LOGGING_LEVEL)

def login_form(ask:str = "Please enter your wonderful Celestical credentials",
    default_email:str = None
    ) -> (str, str):
    cli_panel(ask)
    user_mail = prompt_user("User Mail", default=default_email)
    if "@" not in user_mail:
        cli_panel(message="Email is incorrect: no @ sign found.", type="error")
        return login_form(ask)

    password = getpass.getpass(" *** Password: ")
    if len(password) <= 7:
        cli_panel(message="Password to short!", type="error")
        return login_form(ask)
    return (user_mail, password)


def user_login(default_email:str = None,
               force_relog:bool = False) -> bool:
    """Login to Parametry's Celestical Cloud Services via the CLI.

    Returns:
        bool
    """

    user_data = {}
    if default_email is None:
        user_data = load_config()

    use_user = False
    if "access_token" in user_data:
        if len(user_data["access_token"]) > 10:
            if "username" not in user_data:
                logging.warning("Oh no it seems config was manually edited.")
            elif force_relog == False:
                cli_panel(f"You are logged in as {user_data['username']}")
                use_user = confirm_user("Do you want to continue" \
                    + f" with user [yellow]{user_data['username']}[/yellow]")
                if use_user:
                    cli_panel("\t --> continuing as " \
                        +f"[yellow]{user_data['username']}[/yellow]")
                    return True

        if force_relog:
            cli_panel("logging out...\n-----\n\n")
            # Similar to a logout: forgeting token
            data = {
                "created": datetime.utcnow().strftime('%Y-%m-%d_%H:%M:%S'),
                "username": "",
                "access_token": "",
                "token_type": ""
            }
            save_config(data)

            if "username" in user_data:
                if user_data['username'] is None or user_data['username'] == "":
                    return user_login(default_email=None)
                # else we've got a previous email info
                return user_login(default_email=user_data['username'])
            return user_login()

    with ApiClient(apiconf) as api_client:
        # Create an instance of the API class
        api_instance = AuthApi(api_client)

        (username, password) = login_form(default_email=default_email)

        try:
            # Auth:Jwt.Login
            api_response = api_instance.auth_jwt_login_auth_jwt_login_post(username, password)
            logging.debug("we did get a api response")
            if api_response.token_type != "bearer":
                logging.debug("This client does not handle non bearer type token")
                return False

            if len(api_response.access_token) < 10:
                logging.debug("Received token seems invalid")
                return False

            # Collect all user data and save it
            logging.debug("Creating and saving user data/conf.")
            data = {
                "created": datetime.utcnow().strftime('%Y-%m-%d_%H:%M:%S'),
                "username": username,
                "access_token": api_response.access_token,
                "token_type": api_response.token_type
            }
            save_config(data)
        except ApiException as api_exp:
            logging.error("Exception when logging in: code Enceladus")
            logging.debug(api_exp)
            cli_panel("Sorry we could not log you in at the moment")
            return False

    return True


def user_register() -> bool:
    """Register as a user for Parametry Cloud Services via the CLI."""

    with ApiClient(apiconf) as api_client:
        auth = AuthApi(api_client=api_client)

        (user_mail, password) = login_form("Please enter new Celestical credentials")

        apires = None
        try:
            apires = auth.register_register_auth_register_post(
                    user_create=UserCreate(
                        email= user_mail,
                        password=password
                        )
                    )
        except ApiException as api_err:
            msg = f"---- Registration error ({api_err.status})"
            logging.error(msg)
            logging.debug(apires)
            if api_err.body:
                logging.debug(api_err.body)
            else:
                logging.debug(api_err.reason)
            return False

        cli_panel("You are now registered and must verify your email")
        return True
