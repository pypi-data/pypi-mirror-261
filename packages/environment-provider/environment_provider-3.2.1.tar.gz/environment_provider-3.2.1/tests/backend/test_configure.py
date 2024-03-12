# Copyright Axis Communications AB.
#
# For a full list of individual contributors, please see the commit history.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Tests for the configure backend system."""
import json
import logging
import unittest
from typing import OrderedDict

from etos_lib import ETOS
from etos_lib.lib.config import Config
from jsontas.jsontas import JsonTas

from environment_provider.lib.registry import ProviderRegistry
from environment_provider_api.backend.configure import (
    configure,
    get_configuration,
    get_dataset,
    get_execution_space_provider_id,
    get_iut_provider_id,
    get_log_area_provider_id,
)
from tests.library.fake_database import FakeDatabase
from tests.library.fake_request import FakeRequest


class TestConfigureBackend(unittest.TestCase):
    """Test the configure backend."""

    maxDiff = None

    logger = logging.getLogger(__name__)

    def tearDown(self):
        """Reset all globally stored data for the next test."""
        Config().reset()

    def test_iut_provider_id(self):
        """Test that the configure backend can return IUT provider id.

        Approval criteria:
            - The configure backend shall be able to get the IUT provider id from request.

        Test steps:
            1. Get IUT provider id from request via the configure backend.
            2. Verify that the backend returns the correct iut provider id.
        """
        request = FakeRequest()
        test_provider_id = "test_iut_provider"
        request.fake_params["iut_provider"] = test_provider_id
        self.logger.info("STEP: Get IUT provider id from request via the configure backend.")
        response_provider_id = get_iut_provider_id(request)

        self.logger.info("STEP: Verify that the backend returns the correct iut provider id.")
        self.assertEqual(test_provider_id, response_provider_id)

    def test_iut_provider_id_none(self):
        """Test that the configure backend returns None if IUT provider id is not set.

        Approval criteria:
            - The configure backend shall return None if IUT provider is not in request.

        Test steps:
            1. Get IUT provider from request via the configure backend.
            2. Verify that the backend returns None.
        """
        self.logger.info("STEP: Get IUT provider id from request via the configure backend.")
        response = get_iut_provider_id(FakeRequest())

        self.logger.info("STEP: Verify that the backend returns None.")
        self.assertIsNone(response)

    def test_execution_space_provider_id(self):
        """Test that the configure backend can return execution space provider id.

        Approval criteria:
            - The configure backend shall be able to get the execution space provider id
              from request.

        Test steps:
            1. Get execution space provider id from request via the configure backend.
            2. Verify that the backend returns the correct execution space provider id.
        """
        request = FakeRequest()
        test_provider_id = "test_execution_space_provider_id"
        request.fake_params["execution_space_provider"] = test_provider_id
        self.logger.info(
            "STEP: Get execution space provider id from request via the configure backend."
        )
        response_provider_id = get_execution_space_provider_id(request)

        self.logger.info(
            "STEP: Verify that the backend returns the correct execution space provider id."
        )
        self.assertEqual(test_provider_id, response_provider_id)

    def test_execution_space_provider_id_none(self):
        """Test that the configure backend returns None if execution space provider id is not set.

        Approval criteria:
            - The configure backend shall return None if execution space provider is not in request.

        Test steps:
            1. Get execution space provider from request via the configure backend.
            2. Verify that the backend returns None.
        """
        self.logger.info(
            "STEP: Get execution space provider id from request via the configure backend."
        )
        response = get_execution_space_provider_id(FakeRequest())

        self.logger.info("STEP: Verify that the backend returns None.")
        self.assertIsNone(response)

    def test_log_area_provider_id(self):
        """Test that the configure backend can return log area provider id.

        Approval criteria:
            - The configure backend shall be able to get the log area provider id from request.

        Test steps:
            1. Get log area provider id from request via the configure backend.
            2. Verify that the backend returns the correct log area provider id.
        """
        request = FakeRequest()
        test_provider_id = "test_log_area_provider_id"
        request.fake_params["log_area_provider"] = test_provider_id
        self.logger.info("STEP: Get log area provider id from request via the configure backend.")
        response_provider_id = get_log_area_provider_id(request)

        self.logger.info("STEP: Verify that the backend returns the correct log area provider id.")
        self.assertEqual(test_provider_id, response_provider_id)

    def test_log_area_provider_id_none(self):
        """Test that the configure backend returns None if log area provider id is not set.

        Approval criteria:
            - The configure backend shall return None if log area provider is not in request.

        Test steps:
            1. Get log area provider from request via the configure backend.
            2. Verify that the backend returns None.
        """
        self.logger.info("STEP: Get log area provider id from request via the configure backend.")
        response = get_log_area_provider_id(FakeRequest())

        self.logger.info("STEP: Verify that the backend returns None.")
        self.assertIsNone(response)

    def test_dataset(self):
        """Test that the configure backend can return dataset.

        Approval criteria:
            - The configure backend shall be able to get the dataset from request.

        Test steps:
            1. Get dataset from request via the configure backend.
            2. Verify that the backend returns the correct dataset.
        """
        request = FakeRequest()
        test_dataset = {"test_dataset": "my ultimate dataset"}
        request.fake_params["dataset"] = json.dumps(test_dataset)
        self.logger.info("STEP: Get dataset from request via the configure backend.")
        response_dataset = get_dataset(request)

        self.logger.info("STEP: Verify that the backend returns the correct dataset.")
        self.assertDictEqual(test_dataset, response_dataset)

    def test_dataset_none(self):
        """Test that the configure backend returns None if dataset is not set.

        Approval criteria:
            - The configure backend shall return None if dataset is not in request.

        Test steps:
            1. Get dataset from request via the configure backend.
            2. Verify that the backend returns None.
        """
        self.logger.info("STEP: Get dataset from request via the configure backend.")
        response = get_dataset(FakeRequest())

        self.logger.info("STEP: Verify that the backend returns None.")
        self.assertIsNone(response)

    def test_configure(self):
        """Test that it is possible to configure the environment provider.

        Approval criteria:
            - The configure backend shall set the correct configuration.

        Test steps:
            1. Add providers into the database.
            2. Attempt to configure the environment provider using the provider ids.
            3. Verify that the configuration was stored in the database.
        """
        database = FakeDatabase()
        Config().set("database", database)
        test_iut_provider = {
            "iut": {
                "id": "iut_provider_test",
                "list": {"available": [], "possible": []},
            }
        }
        test_execution_space_provider = {
            "execution_space": {
                "id": "execution_space_provider_test",
                "list": {"available": [{"identifier": "123"}], "possible": []},
            }
        }
        test_log_area_provider = {
            "log": {
                "id": "log_area_provider_test",
                "list": {"available": [], "possible": []},
            }
        }
        self.logger.info("STEP: Add providers into the database.")
        database.put(
            f"/environment/provider/iut/{test_iut_provider['iut']['id']}",
            json.dumps(test_iut_provider),
        )
        provider_id = test_execution_space_provider["execution_space"]["id"]
        database.put(
            f"/environment/provider/execution-space/{provider_id}",
            json.dumps(test_execution_space_provider),
        )
        database.put(
            f"/environment/provider/log-area/{test_log_area_provider['log']['id']}",
            json.dumps(test_log_area_provider),
        )

        test_suite_id = "740d1e2a-2309-4c53-beda-569da70c315c"
        test_dataset = {"a": "dataset"}
        registry = ProviderRegistry(ETOS("", "", ""), JsonTas(), test_suite_id)
        self.logger.info(
            "STEP: Attempt to configure the environment provider using the provider ids."
        )
        success, _ = configure(
            registry,
            test_iut_provider["iut"]["id"],
            test_execution_space_provider["execution_space"]["id"],
            test_log_area_provider["log"]["id"],
            test_dataset,
        )

        self.logger.info("STEP: Verify that the configuration was stored in the database.")
        self.assertTrue(success)
        stored_iut_provider = json.loads(database.get(f"/testrun/{test_suite_id}/provider/iut")[0])
        self.assertDictEqual(stored_iut_provider, test_iut_provider)
        stored_execution_space_provider = json.loads(
            database.get(f"/testrun/{test_suite_id}/provider/execution-space")[0]
        )
        self.assertDictEqual(stored_execution_space_provider, test_execution_space_provider)
        stored_log_area_provider = json.loads(
            database.get(f"/testrun/{test_suite_id}/provider/log-area")[0]
        )
        self.assertDictEqual(stored_log_area_provider, test_log_area_provider)
        stored_dataset = json.loads(database.get(f"/testrun/{test_suite_id}/provider/dataset")[0])
        self.assertDictEqual(stored_dataset, test_dataset)

    def test_configure_missing_parameter(self):
        """Test that the configure backend does not configure if any parameter is missing.

        Approval criteria:
            - The configure backend shall return False and not configure if any parameter
              is missing.

        Test steps:
            1. Attempt to configure the environment provider without any parameters.
            2. Verify that False was returned and no configuration was made.
        """
        database = FakeDatabase()
        Config().set("database", database)
        self.logger.info(
            "STEP: Attempt to configure the environment provider without any parameters."
        )
        registry = ProviderRegistry(ETOS("", "", ""), JsonTas(), None)
        success, _ = configure(registry, None, None, None, None)

        self.logger.info("STEP: Verify that False was returned and no configuration was made.")
        self.assertFalse(success)
        self.assertDictEqual(database.db_dict, {})

    def test_configure_empty_dataset(self):
        """Test that it is possible to configure the environment provider if dataset is empty.

        Approval criteria:
            - It shall be possible to configure using an empty dataset.

        Test steps:
            1. Add providers into the database.
            2. Attempt to configure the environment provider with an empty dataset.
            3. Verify that the configuration was stored in the database.
        """
        database = FakeDatabase()
        Config().set("database", database)
        test_iut_provider = {
            "iut": {
                "id": "iut_provider_test",
                "list": {"available": [], "possible": []},
            }
        }
        test_execution_space_provider = {
            "execution_space": {
                "id": "execution_space_provider_test",
                "list": {"available": [{"identifier": "123"}], "possible": []},
            }
        }
        test_log_area_provider = {
            "log": {
                "id": "log_area_provider_test",
                "list": {"available": [], "possible": []},
            }
        }
        self.logger.info("STEP: Add providers into the database.")
        database.put(
            f"/environment/provider/iut/{test_iut_provider['iut']['id']}",
            json.dumps(test_iut_provider),
        )
        provider_id = test_execution_space_provider["execution_space"]["id"]
        database.put(
            f"/environment/provider/execution-space/{provider_id}",
            json.dumps(test_execution_space_provider),
        )
        database.put(
            f"/environment/provider/log-area/{test_log_area_provider['log']['id']}",
            json.dumps(test_log_area_provider),
        )

        test_suite_id = "740d1e2a-2309-4c53-beda-569da70c315c"
        test_dataset = {}
        registry = ProviderRegistry(ETOS("", "", ""), JsonTas(), test_suite_id)
        self.logger.info(
            "STEP: Attempt to configure the environment provider with an empty dataset."
        )
        success, _ = configure(
            registry,
            test_iut_provider["iut"]["id"],
            test_execution_space_provider["execution_space"]["id"],
            test_log_area_provider["log"]["id"],
            test_dataset,
        )

        self.logger.info("STEP: Verify that the configuration was stored in the database.")
        self.assertTrue(success)
        stored_iut_provider = json.loads(database.get(f"/testrun/{test_suite_id}/provider/iut")[0])
        self.assertDictEqual(stored_iut_provider, test_iut_provider)
        stored_execution_space_provider = json.loads(
            database.get(f"/testrun/{test_suite_id}/provider/execution-space")[0]
        )
        self.assertDictEqual(stored_execution_space_provider, test_execution_space_provider)
        stored_log_area_provider = json.loads(
            database.get(f"/testrun/{test_suite_id}/provider/log-area")[0]
        )
        self.assertDictEqual(stored_log_area_provider, test_log_area_provider)
        stored_dataset = json.loads(database.get(f"/testrun/{test_suite_id}/provider/dataset")[0])
        self.assertDictEqual(stored_dataset, test_dataset)

    def test_get_configuration(self):
        """Test that it is possible to get a stored configuration.

        Approval criteria:
            - It shall be possible to get a stored configuration.

        Test steps:
            1. Store a configuration into the database.
            2. Verify that it is possible to get the stored configuration.
        """
        database = FakeDatabase()
        Config().set("database", database)
        test_suite_id = "8d9344e3-a246-43ec-92b4-fc81ea31067a"
        test_dataset = {"dataset": "test"}
        test_iut_provider = OrderedDict(
            {
                "iut": {
                    "id": "iut_provider_test",
                    "list": {"available": [], "possible": []},
                }
            }
        )
        test_execution_space_provider = OrderedDict(
            {
                "execution_space": {
                    "id": "execution_space_provider_test",
                    "list": {"available": [{"identifier": "123"}], "possible": []},
                }
            }
        )
        test_log_area_provider = OrderedDict(
            {
                "log": {
                    "id": "log_area_provider_test",
                    "list": {"available": [], "possible": []},
                }
            }
        )
        self.logger.info("STEP: Store a configuration into the database.")
        database.put(f"/testrun/{test_suite_id}/provider/dataset", json.dumps(test_dataset))
        database.put(f"/testrun/{test_suite_id}/provider/iut", json.dumps(test_iut_provider))
        database.put(
            f"/testrun/{test_suite_id}/provider/log-area", json.dumps(test_log_area_provider)
        )
        database.put(
            f"/testrun/{test_suite_id}/provider/execution-space",
            json.dumps(test_execution_space_provider),
        )

        self.logger.info("STEP: Verify that it is possible to get the stored configuration.")
        registry = ProviderRegistry(ETOS("", "", ""), JsonTas(), test_suite_id)
        stored_configuration = get_configuration(registry)
        self.assertDictEqual(
            stored_configuration,
            {
                "iut_provider": test_iut_provider["iut"],
                "execution_space_provider": test_execution_space_provider["execution_space"],
                "log_area_provider": test_log_area_provider["log"],
                "dataset": test_dataset,
            },
        )

    def test_get_configuration_missing(self):
        """Test that if a configuration is missing, a partial result is returned.

        Approval criteria:
            - The configure backend shall return a partial configuration if configuration
              is missing.

        Test steps:
            1. Store a faulty configuration into the database.
            2. Verify that it is possible to get the partial configuration.
        """
        database = FakeDatabase()
        Config().set("database", database)
        test_suite_id = "ca51601e-6c9a-4b5d-8038-7dc2561283d2"
        test_dataset = {"dataset": "test"}
        self.logger.info("STEP: Store a faulty configuration into the database.")
        database.put(f"/testrun/{test_suite_id}/provider/dataset", json.dumps(test_dataset))

        self.logger.info("STEP: Verify that it is possible to get the partial configuration.")
        registry = ProviderRegistry(ETOS("", "", ""), JsonTas(), test_suite_id)
        stored_configuration = get_configuration(registry)
        self.assertDictEqual(
            stored_configuration,
            {
                "dataset": test_dataset,
                "iut_provider": None,
                "execution_space_provider": None,
                "log_area_provider": None,
            },
        )
