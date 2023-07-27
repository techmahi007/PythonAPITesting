import requests
from requests.auth import HTTPBasicAuth

def test_user_authentication():
    response = requests.get("https://api.github.com/user", auth=HTTPBasicAuth("techmahi007","mahimna.22010012"))
    print(response.text)