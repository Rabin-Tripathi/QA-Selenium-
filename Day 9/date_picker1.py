import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://jqueryui.com/datepicker/")
driver.maximize_window()

# If the web have only one frame we can directly pass 0 as an index
driver.switch_to.frame(0)  # switch to frame

# mm/dd/yyy
# driver.find_element(By.XPATH, "//input[@id='datepicker']").send_keys("10/19/2001")

# Logic to write the date from the date picker
year = "2002"
month = "December"
date = "12"

driver.find_element(By.XPATH, "//input[@id='datepicker']").click()  # Opens Datepicker

### Select expected month and year
while True:
    mon = driver.find_element(By.XPATH, "//span[@class='ui-datepicker-month']").text
    yr = driver.find_element(By.XPATH, "//span[@class='ui-datepicker-year']").text

    if mon == month and yr == year:
        break;
    else:
        # driver.find_element(By.XPATH, "//span[@class='ui-icon ui-icon-circle-triangle-e']").click()     # Next arrow
        driver.find_element(By.XPATH, "//span[@class='ui-icon ui-icon-circle-triangle-w']").click()  # Previous arrow

### Select expected Date
dates = driver.find_elements(By.XPATH, "//tbody/tr/td/a")

for element in dates:
    if element.text == date:
        element.click()
        break;

time.sleep(3)
driver.close()

