import json
import requests


def test_get_naar_niet_bestaand_account():
    url = "http://localhost:8080/user/10"
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.get(url, headers=headers, timeout=3)
    assert response.status_code == 500
    data = json.loads(response.content)
    assert data["message"] == "No value present"
    print(response.text)


test_get_naar_niet_bestaand_account()