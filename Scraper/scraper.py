from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def ComcastLogin(user, password):
    usernameStr = user
    passwordStr = password

    browser = webdriver.Chrome()
    browser.get(('https://login.xfinity.com/login?r=comcast.net&s=oauth&continue=https%3A%2F%2Foauth.xfinity.com%2Foauth%2Fauthorize%3Fresponse_type%3Dcode%26redirect_uri%3Dhttps%253A%252F%252Fauth.xfinity.com%252Foauth%252Fcallback%26client_id%3Dmy-xfinity%26state%3Dhttps%253A%252F%252Fcustomer.xfinity.com%252F%2523%252F%253FCMP%253DILC_signin_myxfinity_re%26response%3D1&client_id=my-xfinity&reqId=d1ef0ba4-cab0-45d6-96b6-a20c52554897'))

    username = browser.find_element_by_id('user')
    username.send_keys(usernameStr)
    password = browser.find_element_by_id('passwd')
    password.send_keys(passwordStr)
    submit = browser.find_element_by_id('sign_in')
    submit.click()

    browser.implicitly_wait(10)

    executed = False

    while executed == False:
        try:
            manage = browser.find_element_by_partial_link_text('Manage Internet')
            manage.click()
            print("Attempted.")
            executed = True
        except:
            print("Did not work.")
            break

    browser.implicitly_wait(10)


    