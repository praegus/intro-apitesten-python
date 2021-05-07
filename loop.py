import json
import requests
users = ["1", "2", "3", "4", "5", "6", "7", "8"]
dates = [{"dateRange": "2021-03-11 tot 2021-03-14"}, {"dateRange": "2021-04-11 tot 2021-04-14"}, {"dateRange": "2021-05-11 tot 2021-05-14"}, {"dateRange": "2021-06-11 tot 2021-06-14"},
         {"dateRange": "2021-07-11 tot 2021-07-14"}, {"dateRange": "2021-08-11 tot 2021-08-14"}, {"dateRange": "2021-09-11 tot 2021-09-14"}, {"dateRange": "2021-10-11 tot 2021-10-14"}]


def test_post_vakantie():
    for user in users:
        url = "http://localhost:8080/user/reserve/{}".format(user)
        for date in dates:
            payload = date
            headers = {
                'Content-Type': 'application/json'
            }
            response = requests.post(
                url, headers=headers, json=payload, timeout=3)
            assert response.status_code == 200
            data = json.loads(response.content)
            assert data["reserveringIsGoedgekeurd"] == True
            print(response.text)
            break
        break


test_post_vakantie()
