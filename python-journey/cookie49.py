from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep , time
from selenium.common.exceptions import NoSuchElementException

option = webdriver.ChromeOptions()
option.add_experimental_option("detach", True)

web = webdriver.Chrome(options=option)
web.get("https://ozh.github.io/cookieclicker/")

sleep(3)
try:
    language = web.find_element(By.ID, value="langSelect-EN")
    language.click()
    sleep(3)
finally:
    cookie = web.find_element(By.ID, value="bigCookie")
    products = [f"product{i}"for i in range(0,19)]
    
    wait_time = 5
    timeout = time()+wait_time
    five_minutes = time() + 5*60

    while True:
        cookie.click()
        if time() > timeout:
            try:
                cookies = web.find_element(By.ID, value="cookies")
                cookies_count = cookies.text.split()[0].replace(",","")
                products = web.find_elements(by=By.CSS_SELECTOR, value="div[id^='product']")

                best_item = None
                for product in reversed(products):
                    print(product.get_attribute("class"))
                    if "enabled" in product.get_attribute("class"):
                        best_item = product
                        break
                if best_item:
                    best_item.click()
                else:
                    print("No enabled product to buy.")
            except (NoSuchElementException , ValueError):
                print("No such product found")

            timeout = time() + wait_time

            if time() > five_minutes:
                try:
                    cookies_element = web.find_element(by=By.ID, value="cookies")
                    print(f"Final result: {cookies_element.text}")
                except NoSuchElementException:
                    print("Couldn't get final cookie count")
                break