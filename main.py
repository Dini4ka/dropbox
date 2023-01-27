import requests
import json
import undetected_chromedriver.v2 as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from trash import get_auth_token

app_key = "p3kpv209f0w81mq"
app_secret = "mqlefiuagbszfh9"

# build the authorization URL:
authorization_url = "https://www.dropbox.com/oauth2/authorize?client_id=p3kpv209f0w81mq&response_type=code"

authorization_code = get_auth_token()
print(authorization_code)

# exchange the authorization code for an access token:
token_url = "https://api.dropboxapi.com/oauth2/token"
params = {
    "code": authorization_code,
    "grant_type": "authorization_code",
    "client_id": app_key,
    "client_secret": app_secret
}
r = requests.post(token_url, data=params)
print(r.text)
