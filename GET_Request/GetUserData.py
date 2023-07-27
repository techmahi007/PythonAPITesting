import requests

# API url
url = "https://reqres.in/api/users?page=2"

# Send GET request
response = requests.get(url)

# print("\n\n**************This is the response status code**************\n")
# print(response)

# # printing response contents
# print("\n\n**************These are the contents**************\n")
# print(response.content)

# # printing response headers
# print("\n\n**************These are the headers**************\n")
# print(response.headers)

# Validate status code
print(response.status_code)

# assert is used to validate actual result with expected result
assert response.status_code == 200

# Fetch response headers
print(response.headers.get('Date'))
print(response.headers.get('Server'))

# Fetch cookies
print(response.cookies)

# Fetch encoding
print(response.encoding)

# Fetch elapsed time - time taken between sending request & getting response
print(response.elapsed)