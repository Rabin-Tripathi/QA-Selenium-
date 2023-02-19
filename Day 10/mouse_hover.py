import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://jqueryui.com/datepicker/")
driver.maximize_window()

'''
driver.find_element(By.XPATH, "//a[@title='QUnit']").click()
driver.find_element(By.XPATH, "//span[normalize-space()='About']").click()
driver.find_element(By.XPATH, "//a[normalize-space()='About QUnit']").click()
'''

### QUnit--> Guides--> Documentation
qunit = driver.find_element(By.XPATH, "//a[@title='QUnit']")
about = driver.find_element(By.XPATH, "//span[normalize-space()='About']")
about_qunit = driver.find_element(By.XPATH, "//a[normalize-space()='About QUnit']")

# MouseHover Actions
act = ActionChains(driver)  # it always requires driver instance

# It creates an action, but it does not perform actions if we don't write perform() method.
act.move_to_element(qunit).move_to_element(about).move_to_element(about_qunit).click().perform()

# Note: - To perform the Right CLick Actions--> context_click(element)
# act = ActionChains(driver)
# act.context_click(button).perform()

# Note: - To perform Double CLick Actions--> double_click(element)
# act = ActionChains(driver)
# act.double_click(button).perform()


time.sleep(3)
driver.close()

