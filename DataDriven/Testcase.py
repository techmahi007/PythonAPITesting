import requests
import json
import jsonpath
import openpyxl

from DataDriven import Libraries

def test_add_multiple_students():
    # API
    api_url = "https://thetestingworldapi.com/api/studentsDetails"
    file = open("C:/Users/mahimna.bhuskute/Desktop/Training Programs/Python Automation July 2023/Step by Step Rest API Testing using Python + Pytest +Allure/TestCases/AddStudent.json", "r")
    request_json = json.loads(file.read())

    obj = Libraries.Common("C:/Users/mahimna.bhuskute/Downloads/Book.xlsx", "Sheet1")
    col = obj.fetch_col_count()
    row = obj.fetch_row_count()
    keyList = obj.fetch_key_names()

    for i in range(2, row+1):
        updated_json_request = obj.update_request_with_data(i, request_json, keyList)
        response = requests.post(api_url, updated_json_request)
        print(response)