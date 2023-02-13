from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

print(driver.title)         # Gives title of the Page
print(driver.current_url)   # Gives the URL
print(driver.page_source)   # To capture the source code of Page

driver.close()
