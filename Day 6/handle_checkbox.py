import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://itera-qa.azurewebsites.net/home/automation")
driver.maximize_window()

# 1. Select specific checkbox
# driver.find_element(By.XPATH, "//input[@id='monday']").click()

# 2. Select all the checkboxes
checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox' and contains(@id, 'day')]")
print(len(checkboxes))  # 7

# approach 1
'''for i in range(len(checkboxes)):
    checkboxes[i].click()
'''
# approach 2
'''for checkbox in checkboxes:
    checkbox.click()
'''

# 3. Select multiple checkboxes by choice
'''for checkbox in checkboxes:
    weekName = checkbox.get_attribute('id')
    if weekName == 'wednesday' or weekName == 'tuesday':
        checkbox.click()
'''

# 4. Select last 2 or 3 checkboxes
# range(4,7) --> 5,7
for i in range(len(checkboxes)-3, len(checkboxes)):
    checkboxes[i].click()

# 5. Select first 2 checkboxes
for i in range(len(checkboxes)):
    if i < 2:
        checkboxes[i].click()

time.sleep(3)
# 6. Clearing all the checkboxes
for checkbox in checkboxes:
    if checkbox.is_selected():
        checkbox.click()


driver.close()
