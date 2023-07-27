import requests
import json
import jsonpath

# API url
url = "https://reqres.in/api/users?page=2"

# Send GET request
response = requests.get(url)

# Parse response to json format
json_response = json.loads(response.text)
# print(json_response)

# Fetch value using json path
# page = jsonpath.jsonpath(json_response, 'page')
# print(page[0])

# assert page[0] == 3

first_name = jsonpath.jsonpath(json_response, 'data[0].first_name')
# print(first_name[0])

for i in range(0,3):
    first_name = jsonpath.jsonpath(json_response, 'data[' + str(i) + '].first_name')
    print(first_name[0])