import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://itera-qa.azurewebsites.net/home/automation")
driver.maximize_window()

# drop_down_country = driver.find_element(By.XPATH, "//select[@class='custom-select']")
drop_down = Select(driver.find_element(By.XPATH, "//select[@class='custom-select']"))

# select option from the dropdown
drop_down.select_by_visible_text("Spain")
drop_down.select_by_value("7")
drop_down.select_by_index("5")  # index always starts from 0.

# Capture all the options and print them
all_options = drop_down.options
print("The total number of options: ", len(all_options))

for opt in all_options:
    print(opt.text)

# Select option from dropdown without using built-in method or functions
for opt in all_options:
    if opt.text == "Italy":
        opt.click()
        break


time.sleep(3)

driver.close()


