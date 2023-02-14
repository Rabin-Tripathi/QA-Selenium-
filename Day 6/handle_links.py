import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://itera-qa.azurewebsites.net/home")
driver.maximize_window()

# Click on the link
driver.find_element(By.LINK_TEXT, "Test Automation").click()

# Partial Link Test
# driver.find_element(By.PARTIAL_LINK_TEXT, "Test").click()

# Find total number of links in the page
links = driver.find_elements(By.XPATH, "//a")
# links = driver.find_elements(By.TAG_NAME, "a")
print(len(links))

# Print all the links name
for link in links:
    print(link.text)