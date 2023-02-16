import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://the-internet.herokuapp.com/javascript_alerts")
driver.maximize_window()

# Opens alert window
driver.find_element(By.XPATH, "//button[@onclick='jsPrompt()']").click()

alert_window = driver.switch_to.alert
print(alert_window.text)
alert_window.send_keys("Welcome to Alert Windows")

# alert_window.accept()   # Close alert window by using OK button
# time.sleep(4)

alert_window.dismiss()  # Close alert window by using Cancel button
time.sleep(4)

driver.close()
