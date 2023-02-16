import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://www.selenium.dev/documentation/")
driver.maximize_window()

driver.switch_to.frame("td-section-nav")
driver.find_element(By.XPATH, "//a[@id='m-documentationwebdriver']//span[contains(text(),'WebDriver')]").click()
# driver.switch_to.default_content()  # go back to main page

# driver.find_element(By.XPATH, "//a[@id='m-documentationwebdrivergetting_started']//span[contains(text(),'Getting Started')]").click()

# driver.find_element(By.XPATH, "//a[normalize-space()='Driver Sessions']").click()

time.sleep(4)
driver.close()
