# -*- coding: utf-8 -*-
# *******************************************************
#   ____                     _               _
#  / ___|___  _ __ ___   ___| |_   _ __ ___ | |
# | |   / _ \| '_ ` _ \ / _ \ __| | '_ ` _ \| |
# | |__| (_) | | | | | |  __/ |_ _| | | | | | |
#  \____\___/|_| |_| |_|\___|\__(_)_| |_| |_|_|
#
#  Sign up for free at https://www.comet.com
#  Copyright (C) 2015-2021 Comet ML INC
#  This file can not be copied and/or distributed without the express
#  permission of Comet ML Inc.
# *******************************************************

import logging

import comet_ml
from comet_ml import _logging

import sentry_sdk

from . import before_send, environment_details, logger_setup, shutdown

LOGGER = logging.getLogger(__name__)


@_logging.convert_exception_to_log_message(
    "Error setting up error tracker",
    logger=LOGGER,
    exception_info=True,
    logging_level=logging.DEBUG,
)
def setup_sentry_error_tracker() -> None:
    config = comet_ml.get_config()

    sentry_dsn = config.get_string(None, "comet.internal.sentry_dsn")
    # IMPORTANT: this block must be updated after merging the API key parser
    comet_url = config.get_string(None, "comet.url_override")
    debug = config.get_bool(None, "comet.internal.sentry_debug")

    sentry_sdk.init(
        dsn=sentry_dsn,
        integrations=[],
        default_integrations=False,
        debug=debug,
        before_send=before_send.callback,
    )

    sdk_context = environment_details.collect()
    sdk_context["comet_url"] = comet_url
    sentry_sdk.set_context(
        "python-sdk-context",
        sdk_context,
    )

    root_logger = logging.getLogger("comet_ml")
    logger_setup.setup_sentry_error_handlers(root_logger)

    shutdown.register_flush()


@_logging.convert_exception_to_log_message(
    "Error while checking if Sentry should be enabled",
    logger=LOGGER,
    exception_info=True,
    return_on_exception=False,
    logging_level=logging.DEBUG,
)
def enabled() -> bool:
    config = comet_ml.get_config()

    sentry_dsn = config.get_string(None, "comet.internal.sentry_dsn")
    if sentry_dsn is None:
        return False

    error_tracking_config = config.get_bool(None, "comet.error_tracking.enable")
    if error_tracking_config is not None:
        return error_tracking_config

    # IMPORTANT: this block must be updated after merging the API key parser
    backend_url = config.get_string(None, "comet.url_override")
    CLOUD_BACKEND_ADDRESS = "https://www.comet.com/clientlib/"

    if CLOUD_BACKEND_ADDRESS == backend_url:
        return True

    return False


def initialized() -> bool:
    if sentry_sdk.Hub.current.client is not None:
        return True

    return False
