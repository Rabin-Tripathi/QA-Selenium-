import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

slider = driver.find_element(By.XPATH, "//div[@id='slider']")

print("Location of slider before moving.......")
print(slider.location)      # {'x': 987, 'y': 1375}

act = ActionChains(driver)
act.drag_and_drop_by_offset(slider, 50, 0).perform()

print("Location of slider after moving.......")
print(slider.location)



time.sleep(4)
driver.close()
