import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import os

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.implicitly_wait(4)

driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
driver.maximize_window()

#### Methods for taking the screenshots by automation scripts

# driver.save_screenshot("F:/Study/QA/python Selenium/Project1/Day 12/homepage.png")
# driver.save_screenshot(os.getcwd()+"//homepage.png")
driver.get_screenshot_as_file(os.getcwd()+"//ticket.png")


time.sleep(3)
driver.close()
