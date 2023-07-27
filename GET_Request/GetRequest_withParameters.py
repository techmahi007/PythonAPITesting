import requests

param = {'name':'calsoft','email':'calsoftindia@gmail.com','number':'+91-123456789'}

response = requests.get('https://httpbin.org/get', params=param)

print(response.text)