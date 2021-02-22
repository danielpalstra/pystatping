import sys
import os

import pytest
from ruamel.yaml import YAML

from statping import Statping


@pytest.mark.skip()
def test_create_service(service, statping):
    # TODO: Implement test for creating services
    pass

    # services = load_services(STATPING_SERVICES_FILE)
    # for service in services:
    #     statping.services.create_service(service)


def test_all_services(statping):

    services = statping.services.get_all_services()
    assert type(services) == list


def test_get_services_by_name(statping):

    services = statping.services.get_service_by_name("SC Identity (Keystone)")
    assert len(list(services)) > 0


def test_upsert_service(service, statping):
    services = statping.services.upsert_service(service)


def test_update_service(service, statping):

    service = statping.services.update_service(12, service)


def test_delete_service(service, statping):

    service = statping.services.create_service(service)
    service_id = service["id"]

    statping.services.delete_service(service_id)


def test_get_details(statping):

    assert type(statping.miscellaneous.get_details()) == dict


def test_create_group(statping):

    group = statping.groups.create_group({"name": "OpenStack Cloud", "public": True})
    print(group)


def test_get_all_groups(statping):

    groups = statping.groups.get_all_groups()
    print(groups)


def test_get_all_messages(statping):

    messages = statping.messages.get_all_messages()
