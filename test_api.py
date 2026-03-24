import pytest
import requests
from unittest.mock import patch

WEATHER_URL = "https://api.example.com/"

# Apply multiple markers to one test
@pytest.mark.external
@pytest.mark.slow
def test_weather_api():
    with patch('requests.get') as mocked_get:
        mocked_get.return_value.status_code = 200

        resp = requests.get(WEATHER_URL)
        assert resp.status_code == 200

