from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from assertpy import assert_that
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .search_page import search
# from dotenv import load_dotenv
from dotenv import dotenv_values

# Load environment variables from .env file
env_vars = dotenv_values(".env")

# Access the environment variables
username = env_vars["USERNAME"]
password = env_vars["PASSWORD"]

import os
import time

# from webdriver_factory import WebDriverFactory

class LoginPage:
    def __init__(self):
        self.driver = WebDriverFactory.get_driver()
        # Other page initialization code



def login():

    driver = webdriver.Chrome('drivers/macos/chromedrivermac')
    wait = WebDriverWait(driver, 10)


    # driver.get('https://www.amazon.com')

    # waiting for sign in bar to show up and clicking it
    wait.until(EC.visibility_of_element_located((By.ID, 'nav-link-accountList-nav-line-1'))).click()
 
    # locating email tab and entering the email
    driver.find_element(By.ID, 'ap_email').send_keys(username)
    # clicking continue button in 2 lines of code
    continue_button = driver.find_element(By.ID, "continue")
    continue_button.click()
    # waiting for next page to load
    wait.until(EC.element_to_be_clickable((By.ID, 'signInSubmit')))
    # locating the password tab and entering the password
    driver.find_element(By.ID, 'ap_password').send_keys(password)
    # clicking submit button
    driver.find_element(By.ID, 'signInSubmit').click()
 
    wait.until(EC.visibility_of_element_located((By.ID, "nav-link-accountList-nav-line-1")))



    # os.system('killall chrome')

    search()
 

