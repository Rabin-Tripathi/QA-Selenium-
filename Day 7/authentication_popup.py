import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://admin:admin@the-internet.herokuapp.com/basic_auth")
driver.maximize_window()

# Syntax: - http://username:password@url
# Example: - https://admin:admin@the-internet.herokuapp.com/basic_auth

time.sleep(4)

driver.close()
