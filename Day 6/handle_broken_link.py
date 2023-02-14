# We need to install the requests package

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import requests as requests

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("http://www.deadlinkcity.com")
driver.maximize_window()

all_links = driver.find_elements(By.TAG_NAME, "a")
count =0

for link in all_links:
    url = link.get_attribute('href')
    try:
        res = requests.head(url)
    except:
        None

    if res.status_code >= 400:
        print(url, " is broken link")
        count += 1
    else:
        print(url, " is valid link")

print("Total number of broken links: ", count)

