import datetime
import pytz
import os
import sys

import pytest
from ruamel.yaml import YAML

from statping import Statping

STATPING_URL = os.getenv("STATPING_URL", "http://localhost:8080")
STATPING_TOKEN = os.getenv("STATPING_TOKEN", None)
STATPING_SERVICES_FILE = os.getenv("STATPING_SERVICES_FILE", "services.yml")


@pytest.fixture
def statping():
    return Statping(
        STATPING_URL,
        token=STATPING_TOKEN,
    )


@pytest.fixture
def message():

    # end_on = (datetime.datetime.today() + datetime.timedelta(days=1)).isoformat()

    return {
        "description": "Several issues",
        "end_on": pytz.utc.localize(
            datetime.datetime.utcnow() + datetime.timedelta(days=1)
        ).isoformat(),
        "service": 0,
        "start_on": pytz.utc.localize(datetime.datetime.utcnow()).isoformat(),
        "title": "Panic",
    }


def test_get_all_messages(statping):

    messages = statping.messages.get_all_messages()
    assert type(messages) == list


def test_create_message(statping, message):

    response = statping.messages.create_message(message)
    assert "error" not in response


def test_delete_message(statping, message):

    msg = statping.messages.create_message(message)
    assert msg["status"] == "success"

    response = statping.messages.delete_message(msg["id"])
    # Assert response is true
    assert response


# def test_update_message(message, statping):

# message = statping.services.update_service(12, service)
