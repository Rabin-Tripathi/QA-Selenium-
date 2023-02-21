import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
driver.maximize_window()

driver.find_element(By.XPATH, "//span[@id='select2-billing_country-container']").click()

country_list = driver.find_elements(By.XPATH, "//ul[@id='select2-billing_country-results']/li")
print("Number of Country List: ", len(country_list))

for country in country_list:
    if country.text == "Nepal":
        country.click()
        break


time.sleep(3)
driver.close()
