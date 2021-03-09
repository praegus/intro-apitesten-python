import requests
import json


def test_maak_reservering_json_foutief():
    url = "http://localhost:8080/user/reserve/1"
    payload = {"dateRange": "2021-03-11 2021-03-14"}
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.post(url, headers=headers, json=payload, timeout=3)
    assert response.status_code == 500
    data = json.loads(response.content)
    assert data["error"] == "Internal Server Error"
    print(response.text)


test_maak_reservering_json_foutief()