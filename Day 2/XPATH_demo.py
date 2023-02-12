from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://www.daraz.com.np/")
driver.maximize_window()

# Absolute or Full XPATH
'''driver.find_element(By.XPATH, "/html/body/ytd-app/div[1]/div/ytd-masthead/div[4]/div[2]/ytd-searchbox/form/div["
                              "1]/div[1]/input").send_keys("barcelona")
driver.find_element(By.XPATH, "/html/body/ytd-app/div[1]/div/ytd-masthead/div[4]/div[2]/ytd-searchbox/button").click()
'''

# Relative or XPATH
'''driver.find_element(By.XPATH, "//*[@id='q']").send_keys("bag")
driver.find_element(By.XPATH, "//*[@id='topActionHeader']/div/div[2]/div/div[2]/form/div/div[2]/button").click()
'''

# XPATH with OR, AND operator
'''driver.find_element(By.XPATH, "//*[@id='q' or @placeholder='Search in Daraz']").send_keys("bag")
driver.find_element(By.XPATH, "//*[@id='topActionHeader']/div/div[2]/div/div[2]/form/div/div[2]/button and @class='search-box__button--1oH7']").send_keys("bag")
'''

# contains() and start-with()
'''driver.find_element(By.XPATH, "//*[@id='q']").send_keys("t-shirts")
driver.find_element(By.XPATH, "//button[starts-with(@class,'search-box_button--1oH7')").click()
'''

# text()
driver.find_element(By.XPATH, "//a[text()='lzd-site-menu-root-item']").click()


