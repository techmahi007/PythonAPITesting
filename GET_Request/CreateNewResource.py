import requests
import json
import jsonpath

url = "https://reqres.in/api/users"

# Read input json file
file = open("C:/Users/mahimna.bhuskute/Desktop/Training Programs/Python Automation July 2023/Step by Step Rest API Testing using Python + Pytest +Allure/CreateUser.json", 'r')
json_input = file.read()

# parsing the data into json format
request_json = json.loads(json_input)
#print(request_json)

# Make POST request with json body
response = requests.post(url, request_json)
#print(response.content)

# Validating response code
assert response.status_code == 201

# Fetch response from headers
print(response.headers.get('Content-Length'))

# Parse response to json format
response_json = json.loads(response.text)

# Pick id using json path
id = jsonpath.jsonpath(response_json, 'id')
print(id[0])