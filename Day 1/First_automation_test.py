
from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

'''serv = Service("C:/Drivers/chromedriver_win32/chromedriver.exe")
driver = webdriver.Chrome(service=serv)
'''

driver.get("https://parabank.parasoft.com")

print(driver.title)

driver.find_element(By.NAME, "username").send_keys("rabin10")
driver.find_element(By.NAME, "password").send_keys("123456")
driver.find_element(By.CLASS_NAME, "button").click()

driver.close()
