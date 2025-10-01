# type: ignore
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from dotenv import load_dotenv
from time import sleep
import os
load_dotenv("hamza.txt")
email = YOUR_EMAIL
password = PASSWORD

options = webdriver.ChromeOptions()
options.add_argument("--log-level=3")
options.add_argument("--disable-logging")
options.add_experimental_option("detach", True)  

driver = webdriver.Chrome(options=options)
driver.get("https://www.linkedin.com/search/results/all/?keywords=python%20developer%20jobs&origin=TYPEAHEAD_HISTORY&"
            "searchId=50f8b0a3-4d56-4ed8-8682-ff92542adc8d&sid=QfD&spellCorrectionEnabled=true")

def sign():
    sleep(3)
    email_field = driver.find_element(By.ID, value="username")
    email_field.send_keys(email)
    password_field = driver.find_element(By.ID, value="password")
    password_field.send_keys(password)
    sign = driver.find_element(By.CLASS_NAME, value="btn__primary--large")
    sign.click()

try:
    sign()
    sleep(25)
    jobs_button = driver.find_element(By.CLASS_NAME, value="artdeco-pill")
    jobs_button.click()
    sleep(5)
    job_container = driver.find_elements(By.CLASS_NAME, "job-card-container--clickable")

    for job in job_container:
        job.click()
        sleep(5)
        job_save = driver.find_element(By.CLASS_NAME, value="jobs-save-button")
        job_save.click()
        sleep(3)
        for _ in range(3):
            up = driver.find_element(By.CLASS_NAME, value="wnAtzXztZPrciqWGQLqMgqmUJfkwqlRgNQmoOE")
            up.send_keys(Keys.ARROW_DOWN)
        sleep(3)
        notification = driver.find_element(By.CLASS_NAME, value="artdeco-button__icon")
        notification.click()

finally:
    pass
         