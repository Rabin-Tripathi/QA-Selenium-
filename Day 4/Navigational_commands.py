import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://www.nopcommerce.com/en")
driver.get("https://www.orangehrm.com/")

driver.back()   # nopcommerce
driver.forward()    # orangehrm
driver.refresh()

driver.maximize_window()

# Navigational Commands are : -
# back(), forward(), and refresh()

driver.quit()

