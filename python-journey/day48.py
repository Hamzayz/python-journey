from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

web = webdriver.Chrome(options=options)
web.get("https://secure-retreat-92358.herokuapp.com/")


try:
    name = web.find_element(By.NAME, value="fName")
    name.send_keys("hamza")
    last_name = web.find_element(By.NAME, value="lName")
    last_name.send_keys("khan")
    email = web.find_element(By.NAME, value="email")
    email.send_keys("hamzaisrar1251@gmail.com")
finally:
    button = web.find_element(By.CLASS_NAME, value="btn-primary")
    button.click()