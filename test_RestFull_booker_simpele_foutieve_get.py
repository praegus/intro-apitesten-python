# bij deze test krijg je geen goed response terug daarom moeilijk testbaar

import requests
import json

base_url = "http://localhost:3001"

# Let op work in progress


def test_get_niet_bestaande_booking():
    url = base_url + "/booking/q"
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.get(url, headers=headers, timeout=3)
    # https://stackoverflow.com/questions/16573332/jsondecodeerror-expecting-value-line-1-column-1-char-0
    # response.raise_for_status()  # raises exception when not a 2xx response
    # if response.status_code != 204:
    #     return response.json()
    assert response.status_code == 404
    data = json.loads(response.content)
    assert data["error"] == "Not Found"
    print(response.content)


test_get_niet_bestaande_booking()
