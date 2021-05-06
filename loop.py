import json
import requests
users = ["1", "2", "3", "4", "5", "6", "7", "8"]
dates = ["01", "02", "03", "04", "05", "06", "07", "08"]


def test_post_vakantie():
    for user in users:
        url = "http://localhost: 8080/user/reserve/{}".format(user)
        payload = {"dateRange": "2021-03-11 tot 2021-03-14"}
        headers = {
            'Content-Type': 'application/json'
        }
        response = requests.post(url, headers=headers, json=payload, timeout=3)
        assert response.status_code == 200
        data = json.loads(response.content)
        assert data["reserveringIsGoedgekeurd"] == True
        print(response.text)
        break


test_post_vakantie()
