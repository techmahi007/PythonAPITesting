import requests

headerdata = {'T1':'First Header','T2':'Second Header'}

response = requests.get('https://httpbin.org/get', headers=headerdata)

print(response.text)