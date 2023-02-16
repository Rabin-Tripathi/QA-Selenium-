import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://mypage.rediff.com/")
driver.maximize_window()

# Login Button Xpath
driver.find_element(By.XPATH, "//input[@value=' Go ']").click()
time.sleep(3)
driver.switch_to.alert.accept()

driver.close()

