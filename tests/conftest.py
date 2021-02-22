import pytest
import sys
import os

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
def service():

    return {
        "name": "New Service",
        "domain": "https://statping.com",
        "expected": "",
        "expected_status": 200,
        "check_interval": 30,
        "type": "http",
        "method": "GET",
        "post_data": "",
        "port": 0,
        "timeout": 30,
        "order_id": 0,
    }
