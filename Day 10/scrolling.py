import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

### 1. Scroll down the page by pixel
'''driver.execute_script("window.scrollBy(0,1500)", "")
value = driver.execute_script("return window.pageYOffset;")
print("Number of pixels moved:", value)
'''

### 2. Scroll down the page till the element is visible
'''element = driver.find_element(By.XPATH, "//div[@id='HTML12']//img[1]")
driver.execute_script("arguments[0].scrollIntoView();", element)
value = driver.execute_script("return window.pageYOffset;")
print("Number of pixels moved:", value)         # 2172
'''


### 3. Scroll down the page till end
driver.execute_script("window.scrollBy(0, document.body.scrollHeight)")
value = driver.execute_script("return window.pageYOffset;")
print("Number of pixels moved:", value)

time.sleep(3)

# Scroll up to starting position
driver.execute_script("window.scrollBy(0, -document.body.scrollHeight)")
value = driver.execute_script("return window.pageYOffset;")
print("Number of pixels moved:", value)


time.sleep(3)
driver.close()
