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

# exchange the authorization code for an access token:
token_url = "https://api.dropboxapi.com/oauth2/token"
params = {
    "code": authorization_code,
    "grant_type": "authorization_code",
    "client_id": app_key,
    "client_secret": app_secret
}
r = requests.post(token_url, data=params)
access_token = r.json()['access_token']


def upload_file(token, src_path, dst_path):
    url = "https://content.dropboxapi.com/2/files/upload"

    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/octet-stream",
        "Dropbox-API-Arg": "{\"path\":\"%s\"}" % dst_path,
    }

    data = open(src_path, "rb").read()

    r = requests.post(url, headers=headers, data=data)
    print(r.content)


def download_file(token, src_path, dst_path):
    url = "https://content.dropboxapi.com/2/files/download"

    headers = {
        "Authorization": f"Bearer {token}",
        "Dropbox-API-Arg": "{\"path\":\"%s\"}" % dst_path,
    }

    r = requests.post(url, headers=headers)
    print(r.status_code)
    with open(src_path,'wb') as f:
        f.write(r.content)


download_file(access_token, 'download/new_file', '/test/test.sql')
