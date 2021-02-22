import datetime
import pytz
import os
import sys

import pytest
from ruamel.yaml import YAML

from statping import Statping

@pytest.fixture
def message():
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
