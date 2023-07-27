import requests
import json
import jsonpath

def test_add_new_student():
    global id
    api_url = "https://thetestingworldapi.com/api/studentsDetails"
    file = open("C:/Users/mahimna.bhuskute/Desktop/Training Programs/Python Automation July 2023/Step by Step Rest API Testing using Python + Pytest +Allure/TestCases/AddStudent.json", "r")
    json_request = json.loads(file.read())
    response = requests.post(api_url, json_request)
    id = jsonpath.jsonpath(response.json(), 'id')
    print(id[0])

def test_get_details():
    api_url = "https://thetestingworldapi.com/api/studentsDetails/"+str(id[0])
    response = requests.get(api_url)
    print(response.text)