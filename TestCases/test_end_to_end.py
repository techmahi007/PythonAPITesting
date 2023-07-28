import requests
import json
import jsonpath

def test_add_new_data():
    api_url = "https://thetestingworldapi.com/api/studentsDetails"
    file = open("D:/Training_Programs/Python_Automation_July_2023/API_Testing_Python_Pytest_Allure/TestCases/addUser.json","r")
    request_json = json.loads(file.read())
    response = requests.post(api_url,request_json)
    id = jsonpath.jsonpath(response.json(), 'id')
    print(id[0])

    tech_api_url = "https://thetestingworldapi.com/api/technicalskills"
    file = open("D:/Training_Programs/Python_Automation_July_2023/API_Testing_Python_Pytest_Allure/TestCases/TechDetails.json","r")
    request_json = json.loads(file.read())
    request_json['id'] = int(id[0])
    request_json['st_id'] = id[0]
    response = requests.post(tech_api_url,request_json)
    print(response.text)

    addr_api_url = "https://thetestingworldapi.com/api/addresses"
    file = open("D:/Training_Programs/Python_Automation_July_2023/API_Testing_Python_Pytest_Allure/TestCases/address.json","r")
    request_json = json.loads(file.read())
    request_json['stId'] = id[0]
    response = requests.post(addr_api_url,request_json)
    print(response.text)

    final_details = "https://thetestingworldapi.com/api/FinalStudentDetails/" + str(id[0])
    response = requests.get(final_details)
    print(response.text)