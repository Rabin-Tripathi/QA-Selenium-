from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://demo.nopcommerce.com/register?returnUrl=%2F")
driver.maximize_window()

# is_displayed and is_enabled command
search_box = driver.find_element(By.XPATH, "//input[@id='small-searchterms']")

# name_box.is_displayed() -- way to write display commands
print("Display Status:", search_box.is_enabled())

print("Display Status:", search_box.is_displayed())

# is_selected() for radio buttons and check boxes
rd_male = driver.find_element(By.XPATH, "//input[@id='gender-male']")
rd_female = driver.find_element(By.XPATH, "//input[@id='gender-female']")

# Before selecting the radio button
print("Default radio button status: ")
print(rd_male.is_selected())    # False
print(rd_female.is_selected())  # False

rd_male.click()      # Selecting the Male radio button

# After selecting male radio button)
print("After selecting the male radio button: ")
print(rd_male.is_selected())
print(rd_female.is_selected())


driver.close()
