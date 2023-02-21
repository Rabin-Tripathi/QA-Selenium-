import time
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.implicitly_wait(4)

'''
driver.get("https://www.dummyticket.com/")
driver.maximize_window()

link = Keys.CONTROL + Keys.RETURN
driver.find_element(By.XPATH, "//a[contains(text(),'Buy Ticket')]").send_keys(link)
'''

### New Tab - Selenium 4: Opens a new tab and switch to that tab
'''
driver.get("https://www.dummyticket.com/")
driver.switch_to.new_window('tab')
driver.get("https://www.foundit.in/")
'''

### New Window - Selenium 4: Opens a new window and switch to that window
driver.get("https://www.dummyticket.com/")
driver.switch_to.new_window('window')
driver.get("https://www.foundit.in/")


time.sleep(5)
driver.close()
