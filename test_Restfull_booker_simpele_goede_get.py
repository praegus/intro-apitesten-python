import requests
import json

base_url = "http://localhost:3001"


def test_get_booking():
    url = base_url + "/booking/6"
    headers = {
        'Content-Type': 'application/json',
        'Connection': 'keep-alive',
        'Accept': '*/*'
    }
    response = requests.get(url, headers=headers, timeout=3)
    assert response.status_code == 200

    data = json.loads(response.content)
    assert data["firstname"] == "Jim"
    print(response.content)


test_get_booking()
