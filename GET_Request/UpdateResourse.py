import requests
import json
import jsonpath

url = "https://reqres.in/api/users/2"

# Read input json file
file = open("C:\\Users\\mahimna.bhuskute\\Desktop\\Training Programs\\Python Automation July 2023\\Step by Step Rest API Testing using Python + Pytest +Allure\\CreateUser.json", 'r')
json_input = file.read()

# parsing the data into json format
request_json = json.loads(json_input)
#print(request_json)

# Make PUT request with json body
response = requests.put(url, request_json)
#print(response.content)

# Validating response code
assert response.status_code == 200

# parse response content
response_json = json.loads(response.text)
updated_list = jsonpath.jsonpath(response_json, 'updatedAt')

print(updated_list[0])