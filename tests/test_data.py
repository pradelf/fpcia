import datetime
import math
from datetime import time

import pandas as pd
import pytest
from fpcia.data import MyPandaDataset


@pytest.fixture
def create_a_good_test_dataset():
    """Create a goodtest dataset instance with no missing values"""
    df = pd.DataFrame(
        [
            {
                "city": "Paris",
                "department": "75",
                "region": "Île-de-France",
                "population": 2148000,
                "area_km2": 105.4,
                "lat": 48.8566,
                "lon": 2.3522,
            },
            {
                "city": "Lyon",
                "department": "69",
                "region": "Auvergne-Rhône-Alpes",
                "population": 515695,
                "area_km2": 47.87,
                "lat": 45.7640,
                "lon": 4.8357,
            },
            {
                "city": "Marseille",
                "department": "13",
                "region": "Provence-Alpes-Côte d'Azur",
                "population": 861635,
                "area_km2": 240.62,
                "lat": 43.2965,
                "lon": 5.3698,
            },
            {
                "city": "Nice",
                "department": "06",
                "region": "Provence-Alpes-Côte d'Azur",
                "population": 342637,
                "area_km2": 71.92,
                "lat": 43.7102,
                "lon": 7.2620,
            },
            {
                "city": "Nantes",
                "department": "44",
                "region": "Pays de la Loire",
                "population": 306694,
                "area_km2": 65.19,
                "lat": 47.2184,
                "lon": -1.5536,
            },
            {
                "city": "Bordeaux",
                "department": "33",
                "region": "Nouvelle-Aquitaine",
                "population": 254436,
                "area_km2": 49.36,
                "lat": 44.8378,
                "lon": -0.5792,
            },
            {
                "city": "Strasbourg",
                "department": "67",
                "region": "Grand Est",
                "population": 284677,
                "area_km2": 78.26,
                "lat": 48.5734,
                "lon": 7.7521,
            },
            {
                "city": "Lille",
                "department": "59",
                "region": "Hauts-de-France",
                "population": 232787,
                "area_km2": 34.83,
                "lat": 50.6292,
                "lon": 3.0573,
            },
        ]
    )

    try:
        dataset = MyPandaDataset(df)
    except Exception:
        dataset = df

    return dataset


@pytest.fixture
def create_a_bad_test_dataset():
    """Create a test dataset instance"""
    df = pd.DataFrame(
        [
            {
                "city": "Paris",
                "department": "75",
                "region": "Île-de-France",
                "population": 2148000,
                "area_km2": 105.4,
                "lat": 48.8566,
                "lon": 2.3522,
            },
            {
                "city": "Lyon",
                "department": "69",
                "region": "Auvergne-Rhône-Alpes",
                "population": 515695,
                "area_km2": 47.87,
                "lat": 45.7640,
                "lon": 4.8357,
            },
            {
                "city": "Marseille",
                "department": "13",
                "region": "Provence-Alpes-Côte d'Azur",
                "population": 861635,
                "area_km2": 240.62,
                "lat": 43.2965,
                "lon": None,
            },
            {
                "city": "Nice",
                "department": "06",
                "region": "Provence-Alpes-Côte d'Azur",
                "population": 342637,
                "area_km2": 71.92,
                "lat": 43.7102,
                "lon": 7.2620,
            },
            {
                "city": "Nantes",
                "department": "44",
                "region": "Pays de la Loire",
                "population": 306694,
                "area_km2": 65.19,
                "lat": 47.2184,
                "lon": -1.5536,
            },
            {
                "city": "Bordeaux",
                "department": "33",
                "region": "Nouvelle-Aquitaine",
                "population": 254436,
                "area_km2": 49.36,
                "lat": 44.8378,
                "lon": -0.5792,
            },
            {
                "city": "Strasbourg",
                "department": "67",
                "region": "Grand Est",
                "population": 284677,
                "area_km2": 78.26,
                "lat": 48.5734,
                "lon": 7.7521,
            },
            {
                "city": "Lille",
                "department": "59",
                "region": "Hauts-de-France",
                "population": 232787,
                "area_km2": 34.83,
                "lat": 50.6292,
                "lon": 3.0573,
            },
        ]
    )

    try:
        dataset = MyPandaDataset(df)
    except Exception:
        dataset = df

    return dataset


def test_how_null_is_not_null(create_a_good_test_dataset):
    """Test the how_null_is_it function with a dataset that has no missing values."""
    from fpcia.eda import how_null_is_it

    result = how_null_is_it(create_a_good_test_dataset)
    assert "Overall missing values in dataset : 0" in result
    assert "missing values in dataset per column :" in result
    assert "city" in result
    assert "department" in result
    assert "region" in result
    assert "population" in result
    assert "area_km2" in result
    assert "lat" in result
    assert "lon" in result


def test_how_null_is_null(create_a_bad_test_dataset):
    from fpcia.eda import how_null_is_it

    result = how_null_is_it(create_a_bad_test_dataset)
    assert "Overall missing values in dataset : 0" in result
    assert "missing values in dataset per column :" in result
    assert "city" in result
    assert "department" in result
    assert "region" in result
    assert "population" in result
    assert "area_km2" in result
    assert "lat" in result
    assert "lon" in result


def test_hello_successfully(create_a_good_test_dataset):
    """Check if test framework works with library"""

    # GIVEN
    texte = "Hello"
    world = "World"
    # WHEN
    result = f"{texte} {world}!"

    # THEN
    assert result == "Hello World!"
    assert isinstance(result, str)
    assert len(result) == 12
    assert "World" in result
    assert isinstance(create_a_test_dataset, pd.DataFrame)
    assert create_a_test_dataset.shape == (8, 7)
    assert list(create_a_test_dataset.columns) == [
        "city",
        "department",
        "region",
        "population",
        "area_km2",
        "lat",
        "lon",
    ]
