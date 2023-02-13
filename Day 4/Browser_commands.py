import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://admin-demo.nopcommerce.com/admin/")
driver.maximize_window()

driver.find_element(By.XPATH, "//a[normalize-space()='nopCommerce']").click()  # It will perform the click action in the link

time.sleep(5)

driver.close()

# Browser Commands
# close() --> Focus on closing the single browser where driver focused
# quit() --> Focus on closing the all/multiple browser
