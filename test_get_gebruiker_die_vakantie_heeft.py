import json
import requests


def test_get_gebruiker_die_vakantie_heeft():
    url = "http://localhost:8080/user/1"
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.get(url, headers=headers, timeout=3)
    assert response.status_code == 200
    data = json.loads(response.content)
    assert data["lastname"] == "MacDonald"
    assert data["reservation"]["startDate"] == "2021-03-11"
    print(response.text)


test_get_gebruiker_die_vakantie_heeft()
