import logging
import math
import time
from collections import defaultdict
from functools import lru_cache

import pandas as pd
import requests

logger = logging.getLogger(__name__)
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

logger = logging.getLogger(__name__)
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)


def haversine_distance(lat1, lon1, lat2, lon2):
    """Calculate the Haversine distance between two points on the Earth."""
    R = 6371.0  # Earth radius in kilometers

    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    a = (
        math.sin(dlat / 2) ** 2
        + math.cos(math.radians(lat1))
        * math.cos(math.radians(lat2))
        * math.sin(dlon / 2) ** 2
    )
    c = 2 * math.asin(math.sqrt(a))
    distance = R * c
    return distance


# Fonction pour interroger l'API Nominatim
def interroger_nominatim(adress: str):
    """Interroger l'API Nominatim pour obtenir les coordonnées géographiques d'une adresse."""
    adresse = adress
    url = "https://nominatim.openstreetmap.org/search"
    params = {"q": adresse, "format": "json", "addressdetails": 1, "limit": 1}
    headers = {"User-Agent": "MonApplicationGeocodage/1.0 (francis.pradel@gmail.com)"}
    response = requests.get(url, params=params, headers=headers)

    if response.status_code == 200:
        results = response.json()
        if results:
            latitude = results[0]["lat"]
            longitude = results[0]["lon"]
            return float(latitude), float(longitude)
    return None, None
