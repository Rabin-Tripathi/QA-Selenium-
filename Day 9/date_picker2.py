import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
driver.maximize_window()

driver.find_element(By.XPATH, "//input[@id='dob']").click()  # Opens date picker

datePicker_month = Select(driver.find_element(By.XPATH, "//select[@aria-label='Select month']"))
datePicker_month.select_by_visible_text("Dec")  # Month

datePicker_year = Select(driver.find_element(By.XPATH, "//select[@aria-label='Select year']"))
datePicker_year.select_by_visible_text("1999")

# Finding date xpath
all_dates = driver.find_elements(By.XPATH, "//table[@class='ui-datepicker-calendar']/tbody/tr/td/a")

for date in all_dates:
    if date.text == "12":
        date.click()
        break;

time.sleep(3)
driver.close()
