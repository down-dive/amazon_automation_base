from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from assertpy import assert_that
from selenium.webdriver.common.by import By
# from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# from .login_page import login
# import time
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.support.select import Select
import requests





# import os
import time

def landing():
    
    driver = webdriver.Chrome('drivers/macos/chromedrivermac')

    driver.get('https://www.amazon.com')

    # find broken links
#     links = driver.find_elements(By.TAG_NAME, "a")
#     for link in links:
#       r = requests.get(link.get_attribute('href'))
#       print(link.get_attribute('href'), r.status_code)

#       # Initialize a list to store broken links
#     broken_links = []

#     for link in links:
#       href = link.get_attribute('href')
#       if href and href != 'javascript:void(0)':  # Exclude javascript:void(0)
#         try:
#             r = requests.get(href)
#             print(href, r.status_code)
#             if r.status_code != 200:
#                 broken_links.append(href)
#         except requests.exceptions.MissingSchema:
#             print("Invalid URL:", href)
#             broken_links.append(href)

# # Print the list of broken links
#     print("Broken Links:")
#     for broken_link in broken_links:
#        print(broken_link)

    # authentication pop up
    # username = "user"
    # password = "passwd"
    # driver.get('http://' + username+':' +password + '@'+ 'httpbin.org/basic-auth/user/passwd') 

    # windows size
    # width = driver.get_window_size().get("width")
    # height = driver.get_window_size().get("height")
    # print(width, height)
    # print(driver.get_window_size())

    # print(width, height)
    # driver.set_window_size(1024, 768)
    time.sleep(5)
    
    # uploading files with send_keys and full path
    # driver.get("https://demoqa.com/upload-download")
    # driver.find_element(By.ID, "uploadFile").send_keys("/Users/yevgeniyaterlyuk/Documents/Projects/Amazon_automation/Pages/Yev session.docx")

    # get title
    # print(driver.title)
      
   # switching windows
    # driver.get("https://login.yahoo.com/") 
    # driver.find_element(By.CLASS_NAME, "privacy").click()
    # driver.find_element(By.CSS_SELECTOR, ".privacy").click()
    # original_window = driver.window_handles[0]
    # driver.find_element(By.XPATH, '//*[contains(@class,"privacy")]').click()
    # second_window = driver.window_handles[1]
    # driver.switch_to.window(original_window)
    # prints the title of the second window
    # print("Second window title = " + driver.title)  
    # prints windows id
    # print(driver.window_handles)    
   
#     #selecting a drop down
#     # driver.get('https://demoqa.com/select-menu')
#     # driver.find_element(By.XPATH, '//*[contains(@data-testid,"open-registration-form-button")]').click()
#     # Select select = new Select(driver.findElement(By.id("oldSelectMenu")));
#     # drop=Select(driver.find_element(By.ID, "oldSelectMenu"))
#     # drop.select_by_visible_text('Blue')
#     # drop.select_by_index(3)
#     # drop.select_by_value("9")

#     # driver.find_element(By.XPATH, '//*[contains(@id, "month")]').click()

#     # takng a screenshot
#     # driver.save_screenshot("image.png")
#     # driver.save_screenshot("./images/image.png")

#     # retrieving css property
#     # element = driver.find_element(By.XPATH, '//*[contains(@class,"nav-logo-link")]')
#     # print(element.value_of_css_property("font-size"))
  
#     # maximising the window
#     # driver.maximize_window()

#     # scrolling
#     # driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
#     # driver.execute_script("window.scrollTo(0,800)")

#     # hovering
#     # hover_elemet = driver.find_element(By.XPATH, "//span[text()='Account & Lists']")
#     # a = ActionChains(driver)
#     # a.move_to_element(hover_elemet).perform()
  


 

#     time.sleep(5)
#     # login()

#     # login_out_button = driver.find_element(By.XPATH, "//button[(text()='Log Out')]")
#     # assert_that(login_out_button).is_true()
#     # print("Log in test is successful")
#     # driver.close()
#     # os.system('killall chrome')
 

