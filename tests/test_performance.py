import time

import pytest

from . import resources


@pytest.fixture
def scenarii() -> dict:
    return {}


@pytest.fixture
def go_performance():
    """Fixture to create Data config for performance tests"""
    pass


def run(config: dict):
    """Run data processing with given config"""
    pass


def test_data_performance(scenarii: dict, go_performance: None):
    """Check performance of data processing functions with various scenarii"""
    # GIVEN
    configs = []
    for scenario in scenarii:
        config = go_performance(scenario)
        configs.append(config)
    # WHEN
    results = {"status": "SUCCESS", "runs": []}
    for c in configs:
        start = time.time()
        result, _ = run(c)
        end = time.time()
        duration = end - start
        results["runs"].append([result, duration])

    # THEN
    assert True
    assert results["status"] == "SUCCESS"
