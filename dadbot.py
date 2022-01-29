from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time

sku = "625242"

store = ["152", "1856", "174", "6980", "161", "147", "134", "1764", "6978", "175"]

num = 0

driver = webdriver.Chrome()

driver.get("https://homedepot.com")

driver.maximize_window()

for i in store:

    driver.get("https://www.homedepot.com/l/")

    time.sleep(2)

    search = driver.find_element(By.ID, "storeSearchBox")

    search.send_keys(f"{i}")

    search.send_keys(Keys.RETURN)

    time.sleep(2)

    links = driver.find_elements(By.XPATH, "//div[@class='sfstorenamehours']//a[contains(@href," + i + ")]")

    search = links[0].get_attribute("href")

    driver.get(search)

    time.sleep(2)

    button = driver.find_element(By.CLASS_NAME, "storeDetailHeader__storeHeaderButton")

    button.click()

    time.sleep(2)

    search = driver.find_element(By.ID, "headerSearch")

    search.send_keys(f"{sku}")

    search.send_keys(Keys.RETURN)

    time.sleep(2)

    if(driver.find_elements(By.CLASS_NAME, "alert-inline__message")):
        
        text = driver.find_element(By.CLASS_NAME, "alert-inline__message")

        print("in stock: " + i + " " + text.text)
        
    elif(driver.find_elements(By.CLASS_NAME, "u__text--success")):
        
        text = driver.find_element(By.CLASS_NAME, "u__text--success")

        print("delivery: " + i + " " + text.text)

    time.sleep(2)

driver.close()


