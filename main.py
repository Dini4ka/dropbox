import requests
import json
import undetected_chromedriver.v2 as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

app_key = "p3kpv209f0w81mq"
app_secret = "mqlefiuagbszfh9"

# build the authorization URL:
authorization_url = "https://www.dropbox.com/oauth2/authorize?client_id=%s&response_type=code" % app_key

# send the user to the authorization URL:
print('Go to the following URL and allow access:')
print(authorization_url)
authorization_code = 'QmPT8i3XN9gAAAAAAAAAE09fC0I_5NxUufsolH50oFw'

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
