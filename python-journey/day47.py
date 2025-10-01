from selenium import webdriver
from selenium.webdriver.common.by import By

crome_options = webdriver.ChromeOptions()
crome_options.add_experimental_option("detach" , True)

driver = webdriver.Chrome(options=crome_options)
driver.get("https://www.python.org/")

event_time = driver.find_elements(By.CSS_SELECTOR, value=".event-widget time")
event_names = driver.find_elements(By.CSS_SELECTOR, value=".event-widget li a")

events = {}
try:
    events = {
        n: {"time": event_time[n].text, "name": event_names[n].text}
        for n in range(len(event_time))
    }
    # for n in range(len(event_time)):
    #     events[n] = {
    #         "time" : event_time[n].text ,
    #         "name" : event_names[n].text,
    #     }
    print(events)
finally:
    # driver.close() # will close that paticular tab
    driver.quit() # will close that window 

    