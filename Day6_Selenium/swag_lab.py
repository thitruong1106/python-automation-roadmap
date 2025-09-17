"""
Selenium Automation script - SauceDemo Login

Description: 

The purpose of this script is to demostrate a basic Selenium test using python. 

It navigates to https://www.saucedemo.com/, enters login credentials, and clicks the login button. 

Planned extensions to script: 
- Add items to card, different items, and adjust quantity.
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

    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    #click on cart button to view card 
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    #Cilck on checkout button 
    driver.find_element(By.ID, "checkout").click()
    #form field
    driver.find_element(By.ID, "first-name").send_keys("Kim")
    driver.find_element(By.ID, "last-name").send_keys("Smith")
    driver.find_element(By.ID, "postal-code").send_keys("2100")

    driver.find_element(By.ID, "continue").click()

    driver.find_element(By.ID, "finish").click()

    complete = driver.find_element(By.CLASS_NAME, "complete-header")
    print("Order Status:", complete.text)

    time.sleep(20)
    driver.quit()

if __name__ == "__main__":
    first_test()