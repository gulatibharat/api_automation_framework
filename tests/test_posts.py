from utils.api_client import get


import json
from utils.api_client import get, post

import json

def test_create_post():

    payload = {
        "title": "Python API Testing",
        "body": "Learning Requests Library",
        "userId": 1
    }

    print("\n========== Request Payload ==========")
    print(json.dumps(payload, indent=4))

    response = post(payload)

    print("\n========== Response ==========")
    print("Status Code :", response.status_code)
    print("Response Body:")
    print(json.dumps(response.json(), indent=4))
    print("=====================================\n")

    assert response.status_code == 201

    data = response.json()
    print(data)

def test_get_by_userid():

    response = get("?userId=2")
    print(response.headers)
    assert response.status_code == 200


    posts = response.json()

    print("\nPosts for User ID = 2\n")

    for post in posts:
        print(json.dumps(post))
        print("-" * 60)

    for post in posts:
        assert post["userId"] == 2

def test_get_single_post():

    response = get("/1")

    assert response.status_code == 200

    post = response.json()

    assert post["id"] == 1
    assert post["userId"] == 1
