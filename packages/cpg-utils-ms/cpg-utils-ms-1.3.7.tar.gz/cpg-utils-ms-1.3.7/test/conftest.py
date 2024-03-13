import os
import json

import pytest


@pytest.fixture
def test_resources_path():
    return os.path.abspath(os.path.join(os.path.dirname(__file__), "resources"))

@pytest.fixture
def json_load(test_resources_path):
    def _loader(file_name):
        with open(os.path.join(test_resources_path, file_name), "r") as json_file:
            return json.load(json_file)
    return _loader
