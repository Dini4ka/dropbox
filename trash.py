import undetected_chromedriver.v2 as uc
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


from config import *

import time


def get_auth_token():
    opts = Options()
    opts.add_argument("--headless")
    driver = uc.Chrome(options=opts)
    while True:
        print('getting Token...')
        try:
            driver.get('https://www.dropbox.com/oauth2/authorize?client_id=p3kpv209f0w81mq&response_type=code')
            time.sleep(10)
            print('authorization with login and password...')
            driver.find_element(By.NAME, 'login_email').send_keys(mail)
            driver.find_element(By.NAME, 'login_password').send_keys(password)
            driver.find_element(By.CLASS_NAME, 'signin-text').click()
            time.sleep(10)
            driver.find_element(By.ID, 'warning-button-continue').click()
            time.sleep(10)
            driver.find_elements(By.CLASS_NAME, 'dig-Button-content')[1].click()
            time.sleep(10)
            auth_code = driver.find_element(By.CLASS_NAME, 'auth-box')
            auth_code = auth_code.get_attribute('value')
            print('Success!!')
            break
        except Exception as er:
            print('Error! Trying again')
        finally:
            pass
    driver.quit()
    return auth_code


