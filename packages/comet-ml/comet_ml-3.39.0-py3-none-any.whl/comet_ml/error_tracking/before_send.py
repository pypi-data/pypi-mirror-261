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

from typing import TYPE_CHECKING, Any, Dict

import comet_ml

from . import environment_details

if TYPE_CHECKING:
    from comet_ml import BaseExperiment


def callback(event: Dict[str, Any], hint: Any) -> Dict[str, Any]:
    try:
        current_experiment = comet_ml.get_global_experiment()

        experiment_id = (
            current_experiment.id if current_experiment is not None else "no-experiment"
        )
        event["user"] = {
            "experiment_id": experiment_id,
            "experiment_class": current_experiment.__class__.__name__,
        }

        if current_experiment is not None:
            feature_toggles = _extract_raw_feature_toggles(current_experiment)
            event["contexts"]["python-sdk-FT"] = feature_toggles

        event["contexts"]["python-sdk-context"][
            "cloud_provider"
        ] = environment_details.try_get_cloud_provider()
    except Exception as exception:
        event["user"] = {"before_send_callback_failed": str(exception)}

    return event


def _extract_raw_feature_toggles(experiment: "BaseExperiment") -> Dict[str, Any]:
    if not experiment.feature_toggles:
        feature_toggles = {}
    else:
        feature_toggles = experiment.feature_toggles.raw_toggles
    return feature_toggles
