from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from assertpy import assert_that
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def search():
    print("Hello")

    driver = webdriver.Chrome('drivers/macos/chromedrivermac')
    wait = WebDriverWait(driver, 10)

    driver.get('https://www.amazon.com')

    print("Hello World")

    # # waiting for sign in bar to show up and clicking it
    # wait.until(EC.visibility_of_element_located((By.ID, 'nav-link-accountList-nav-line-1'))).click()
 
    # locating search tab and entering the search criteria
    driver.find_element(By.ID, 'nav-bb-search').send_keys("snail mucin serum")
    # # clicking continue button in 2 lines of code
    # continue_button = driver.find_element(By.ID, "continue")
    # continue_button.click()
    # # waiting for next page to load
    # wait.until(EC.element_to_be_clickable((By.ID, 'signInSubmit')))
    # # locating the password tab and entering the password
    # driver.find_element(By.ID, 'ap_password').send_keys("Pankevich1990")
    # # clicking submit button
    # driver.find_element(By.ID, 'signInSubmit').click()
 
    # wait.until(EC.visibility_of_element_located((By.ID, "nav-link-accountList-nav-line-1")))


    # print("It worked!")
    # # os.system('killall chrome')

    # search()
 

