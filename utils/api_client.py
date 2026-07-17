import requests

BASE_URL = "https://jsonplaceholder.typicode.com/posts"


def get(endpoint):
    return requests.get(f"{BASE_URL}{endpoint}")

def post(payload):
    return requests.post(f"{BASE_URL}", json=payload)

def put(payload):
    return requests.put(f"{BASE_URL}{endpoint}", json=payload)


def patch(endpoint, payload):
    return requests.patch(f"{BASE_URL}{endpoint}", json=payload)


def delete(endpoint):
    return requests.delete(f"{BASE_URL}{endpoint}")