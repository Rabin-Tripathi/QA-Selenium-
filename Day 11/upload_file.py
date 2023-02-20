import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# driver.get("https://www.foundit.in/")
driver.get("https://demo.automationtesting.in/Register.html")
driver.maximize_window()

# driver.find_element(By.XPATH, "//div[@class='heroSection-buttonContainer_secondaryBtn secondaryBtn']").click()
driver.find_element(By.XPATH, "//input[@id='imagesrc']").send_keys("C:/Users/rabin/Downloads/files_example_CSV_5000(3).pdf")


time.sleep(3)
driver.close()