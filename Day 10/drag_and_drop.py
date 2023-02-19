import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

source_element = driver.find_element(By.XPATH, "//img[@alt='the peaks of high tatras']")
target_element = driver.find_element(By.XPATH, "//div[@id='droppable']")

act = ActionChains(driver)
act.drag_and_drop(source_element, target_element).perform()  # It performs the drag and drop operations


time.sleep(3)
driver.close()

