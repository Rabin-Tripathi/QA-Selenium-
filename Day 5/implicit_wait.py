import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.implicitly_wait(10)      # 10 seconds

driver.get("https://google.com/")
driver.maximize_window()

search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("Selenium")
search_box.submit()

# time.sleep(3)
driver.find_element(By.XPATH, "//h3[text()='Selenium']").click()

driver.quit()
