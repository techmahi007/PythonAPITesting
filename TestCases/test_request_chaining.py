import requests
import json
import jsonpath

def test_add_new_student():
    global id
    api_url = "https://thetestingworldapi.com/api/studentsDetails"
    file = open("D:/Training_Programs/Python_Automation_July_2023/API_Testing_Python_Pytest_Allure/TestCases/AddStudent.json", "r")
    json_request = json.loads(file.read())
    response = requests.post(api_url, json_request)
    id = jsonpath.jsonpath(response.json(), 'id')
    print(id[0])

def test_get_details():
    api_url = "https://thetestingworldapi.com/api/studentsDetails/"+str(id[0])
    response = requests.get(api_url)
    print(response.text)