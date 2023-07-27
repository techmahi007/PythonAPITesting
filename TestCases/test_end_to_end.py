import requests
import json
import jsonpath

def test_add_new_data():
    api_url = "https://thetestingworldapi.com/api/studentsDetails"
    file = open("C:/Users/mahimna.bhuskute/Desktop/Training Programs/Python Automation July 2023/Step by Step Rest API Testing using Python + Pytest +Allure/TestCases/addUser.json","r")
    request_json = json.loads(file.read())
    response = requests.post(api_url,request_json)
    id = jsonpath.jsonpath(response.json(), 'id')
    print(id[0])

    tech_api_url = "https://thetestingworldapi.com/api/technicalskills"
    file = open("C:/Users/mahimna.bhuskute/Desktop/Training Programs/Python Automation July 2023/Step by Step Rest API Testing using Python + Pytest +Allure/TestCases/TechDetails.json","r")
    request_json = json.loads(file.read())
    request_json['id'] = int(id[0])
    request_json['st_id'] = id[0]
    response = requests.post(tech_api_url,request_json)
    print(response.text)

    addr_api_url = "https://thetestingworldapi.com/api/addresses"
    file = open("C:/Users/mahimna.bhuskute/Desktop/Training Programs/Python Automation July 2023/Step by Step Rest API Testing using Python + Pytest +Allure/TestCases/address.json","r")
    request_json = json.loads(file.read())
    request_json['stId'] = id[0]
    response = requests.post(addr_api_url,request_json)
    print(response.text)

    final_details = "https://thetestingworldapi.com/api/FinalStudentDetails/" + str(id[0])
    response = requests.get(final_details)
    print(response.text)