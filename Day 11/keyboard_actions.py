import time
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

''' 
Ctrl+A
Ctrl+C
Tab
Ctrl+V
'''

input1 = driver.find_element(By.XPATH, "//input[@id='field1']")
input2 = driver.find_element(By.XPATH, "//input[@id='field2']")

driver.find_element(By.XPATH, "//input[@id='field1']").clear()
input1.send_keys("Welcome to Selenium Guys!!!")

act = ActionChains(driver)

####### 1. Ctrl + A --> Select all the text
# Multiple line Command
'''act.key_down(Keys.CONTROL)
act.send_keys("a")
act.key_up(Keys.CONTROL)
act.perform()
'''

# Single line Command
act.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform()


####### 2. Ctrl + C --> Copy the text
act.key_down(Keys.CONTROL).send_keys("c").key_up(Keys.CONTROL).perform()


####### 3. Tab --> Press Tab key to navigate next input box
act.send_keys(Keys.TAB).perform()


####### 4. Ctrl + V --> Paste the text
act.key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()


time.sleep(4)
driver.close()
