import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://admin-demo.nopcommerce.com/admin/")
driver.maximize_window()

email = driver.find_element(By.XPATH, "//input[@id='Email']")
email.clear()
email.send_keys("abc@gmail.com")

# Text attribute is always used to return the inner text of the web element
print("Output of text: ", email.text)   # print nothing

# get attribute --> we used it if the inner text is not available
# and to get the value of any attribute of web element
print("Output of get attribute(): ", email.get_attribute('value'))  # print -> abc@gmail.com

button = driver.find_element(By.XPATH, "//button[@type='submit']")
print("Output of text: ", button.text)
print("Output of get_attribute(): ", button.get_attribute('value'))
print("Output of get_attribute(): ", button.get_attribute('type'))


time.sleep(4)

driver.close()
