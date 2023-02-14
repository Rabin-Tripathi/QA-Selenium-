import telnetlib3
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# Declaring the explicit_wait web driver
# myWait = WebDriverWait(driver, 10)
myWait = WebDriverWait(driver, 10, poll_frequency=2, ignored_exceptions=[Exception])

# Explicit wait works based on the conditions

driver.get("https://google.com/")
driver.maximize_window()

search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("Selenium")
search_box.submit()

search_link = myWait.until(EC.presence_of_element_located((By.XPATH, "//h3[text()='Selenium']")))
search_link.click()

driver.quit()


