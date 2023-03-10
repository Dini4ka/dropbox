import sys
import json
import undetected_chromedriver.v2 as uc
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import requests
from config import *


class DropboxApp:

    def __init__(self, login, password):
        self.login = login
        self.password = password
        self.authorization_code = None
        self.access_token = None

    def get_authorization_code(self):
        opts = Options()
        opts.add_argument("--headless")
        driver = uc.Chrome(options=opts)
        while True:
            print('getting Token...')
            try:

                # Getting page for authing
                driver.get('https://www.dropbox.com/oauth2/authorize?client_id=p3kpv209f0w81mq&response_type=code')
                time.sleep(10)
                print('authorization with login and password...')
                driver.find_element(By.NAME, 'login_email').send_keys(self.login)
                driver.find_element(By.NAME, 'login_password').send_keys(self.password)
                driver.find_element(By.CLASS_NAME, 'signin-text').click()

                # Checking the correctness of the login and password
                time.sleep(20)
                try:
                    driver.find_element(By.CLASS_NAME, 'error-message')
                    sys.exit('Wrong login or password')
                except Exception:
                    pass

                # We agree to all conditions and accept all threats
                driver.find_elements(By.CLASS_NAME, 'dig-Button-content')[1].click()
                time.sleep(10)
                driver.find_elements(By.CLASS_NAME, 'dig-Button-content')[1].click()
                time.sleep(10)

                # Getting token
                auth_code = driver.find_element(By.CLASS_NAME, 'auth-box')
                code = auth_code.get_attribute('value')
                print('Success!!')
                break

            # sometimes on some pages it is not displayed completely
            except Exception as ex:
                print('Error! Trying again')
            finally:
                pass
        driver.quit()
        self.authorization_code = code

    def get_access_token(self):
        # exchange the authorization code for an access token:
        token_url = "https://api.dropboxapi.com/oauth2/token"
        params = {
            "code": self.authorization_code,
            "grant_type": "authorization_code",
            "client_id": DROPBOX_APP_KEY,
            "client_secret": DROPBOX_APP_SECRET,
        }
        r = requests.post(token_url, data=params)
        token = r.json()['access_token']
        self.access_token = token

    def upload_file(self, src_path, dst_path):
        web_link = "https://content.dropboxapi.com/2/files/upload"

        headers = {
            "Authorization": f"Bearer {self.access_token}",
            "Content-Type": "application/octet-stream",
            "Dropbox-API-Arg": "{\"path\":\"%s\"}" % dst_path,
        }
        try:
            data = open(src_path, "rb").read()
        except FileNotFoundError:
            sys.exit(f'No such file or directory: {src_path}')

        r = requests.post(web_link, headers=headers, data=data)
        if r.status_code == 400:
            sys.exit(f'Wrong format dropbox path: {dst_path}')
        elif r.status_code == 200:
            print(f'Success upload file {src_path}')

    def download_file(self, src_path, dst_path):
        web_link = "https://content.dropboxapi.com/2/files/download"

        headers = {
            "Authorization": f"Bearer {self.access_token}",
            "Dropbox-API-Arg": "{\"path\":\"%s\"}" % dst_path,
        }

        r = requests.post(web_link, headers=headers)
        if r.status_code == 400:
            sys.exit(f'Wrong format dropbox path: {dst_path}')

        # If the file is not found, then a json file always comes
        try:
            result = json.loads(r.content.decode('utf-8'))
            print(result)
            sys.exit(f'Cant find directory: {dst_path}')
        except Exception:
            pass

        # If there are any problems with finding the file
        try:
            with open(src_path, 'wb') as f:
                f.write(r.content)
        except Exception:
            sys.exit(f'wrong path for: {src_path}')
        print(f'file  {dst_path} was successfully downloaded to {src_path}')
