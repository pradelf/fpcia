import logging
import time

from fpcia.utils import interroger_nominatim


def test_log(caplog):
    caplog.set_level(logging.INFO)
    pass


def test_hello_successfully():
    """Check if test framwork works with library"""

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


# Remplir latitude et longitude


def test_gps_successfully():
    latitude, longitude = interroger_nominatim("Saint-Nom la Bretèche, France")
    logging.getLogger().info(f"Latitude: {latitude}, Longitude: {longitude}")
    time.sleep(1)  # Respecte les conditions d'utilisation de Nominatim
    assert latitude is not None
    assert longitude is not None
    assert abs(latitude - 48.8641009) < 0.1
    assert abs(longitude - 2.0205241) < 0.1


def test_gps_failure():
    latitude, longitude = interroger_nominatim("ThisAddressDoesNotExist12345")
    logging.getLogger().info(f"Latitude: {latitude}, Longitude: {longitude}")
    time.sleep(1)  # Respecte les conditions d'utilisation de Nominatim
    assert latitude is None
    assert longitude is None
