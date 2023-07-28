import requests
import json
import jsonpath
import pytest

url = "https://reqres.in/api/users"

@pytest.fixture(scope="module")
def start_exec():
    global file
    file = open("D:/Training_Programs/Python_Automation_July_2023/API_Testing_Python_Pytest_Allure/CreateUser.json", 'r')

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