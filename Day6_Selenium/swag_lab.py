"""
Selenium Automation script - SauceDemo Login

Description: 

The purpose of this script is to demostrate a basic Selenium test using python. 

It navigates to https://www.saucedemo.com/, enters login credentials, and clicks the login button. 

Planned extensions to script: 
- Add items to card, 
- Proceed through checkout flow 
- Validation of order 

"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
def first_test():
    #Create an instance of chrome browser
    driver = webdriver.Chrome()
    #navigate to website 
    driver.get("https://www.saucedemo.com/")
    
    #wait for page to load content 
    wait = WebDriverWait(driver, 10)
    username_field = wait.until(EC.element_to_be_clickable((By.ID, "user-name")))
    username_field.send_keys("standard_user")

    #password field, ID="password"
    password_field = wait.until(EC.element_to_be_clickable((By.ID, "password")))
    password_field.send_keys("secret_sauce")
    #Find the elemnt button on page, and click
    driver.find_element(By.ID, "login-button").click()

    #click login button
    time.sleep(20)
    driver.quit()

if __name__ == "__main__":
    first_test()