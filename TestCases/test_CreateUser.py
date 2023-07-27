import requests
import json
import jsonpath
import pytest

url = "https://reqres.in/api/users"

@pytest.fixture(scope="module")
def start_exec():
    global file
    file = open("C:\\Users\\mahimna.bhuskute\\Desktop\\Training Programs\\Python Automation July 2023\\Step by Step Rest API Testing using Python + Pytest +Allure\\CreateUser.json", 'r')

def test_create_new_user(start_exec):
    json_input = file.read()
    request_json = json.loads(json_input)
    response = requests.post(url, request_json)
    assert response.status_code == 201

def test_create_other_user(start_exec):
    json_input = file.read()
    request_json = json.loads(json_input)
    response = requests.post(url, request_json)
    response_json = json.loads(response.text)
    id = jsonpath.jsonpath(response_json, 'id')
    print(id[0])