#17/09/2025
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
def login_test():
    driver = webdriver.Chrome()
    try:
        url = "https://the-internet.herokuapp.com/login"
        driver.get(url)

        #wait for page to load content 
        wait = WebDriverWait(driver,10)
        username_field = wait.until(EC.element_to_be_clickable((By.ID, "username")))
        password_field = wait.until(EC.element_to_be_clickable((By.ID, "password")))
        username_field.send_keys("tomsmith")
        password_field.send_keys("SuperSecretPassword!")
        #login button
        driver.find_element(By.CSS_SELECTOR, "button.radius").click()  

        #verify login successful 
        flash = wait.until(EC.visibility_of_element_located((By.ID, "flash"))) #success message
        assert "You logged into a secure area!" in flash.text

        time.sleep(10) #Do something 
        #log out, (a class)
        logout_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a.button.secondary.radius")))
        logout_button.click()

        #verify flash logout 
        flash = wait.until(EC.visibility_of_element_located((By.ID, "flash")))
        print("Flash after logout:", flash.text.strip())
        assert "You logged out of the secure area!" in flash.text
        print("Testing of login and logout done")

    finally:
        driver.quit()

if __name__ == "__main__":
    login_test()