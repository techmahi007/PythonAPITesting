import requests
import json
import jsonpath

def test_add_student_data():
    api_url = "https://thetestingworldapi.com/api/studentsDetails"
    file = open("D:/Training_Programs/Python_Automation_July_2023/API_Testing_Python_Pytest_Allure/TestCases/RequestJson.json","r")
    request_json = json.loads(file.read())
    response = requests.post(api_url, request_json)
    print(response.text)

def test_get_student_data():
    api_url = "https://thetestingworldapi.com/api/studentsDetails/7699655"
    response = requests.get(api_url)
    #json_response = json.loads(response.text)
    # you can use response.json() also in place of json.loads()
    json_response = response.json()
    id = jsonpath.jsonpath(json_response, 'data.id')
    assert id[0] == 7699655

def test_update_student_data():
    api_url = "https://thetestingworldapi.com/api/studentsDetails/7699655"
    file = open("C:/Users/mahimna.bhuskute/Desktop/Training Programs/Python Automation July 2023/Step by Step Rest API Testing using Python + Pytest +Allure/RequestJson.json","r")
    request_json = json.loads(file.read())
    response = requests.put(api_url, request_json)
    print(response.text)

def test_delete_student_data():
    api_url = "https://thetestingworldapi.com/api/studentsDetails/7699655"
    response = requests.delete(api_url)
    print(response.text)