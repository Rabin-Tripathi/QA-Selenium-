
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://practice.automationtesting.in/")
driver.maximize_window()

# XPATH
# driver.find_element(By.XPATH, "//*[@id='search-box']/span/input").send_keys("Languages")

# Link_text and partial_link_text
# driver.find_element(By.LINK_TEXT, "Register").click()
# driver.find_element(By.PARTIAL_LINK_TEXT, "Reg").click()

# ClassName
# TagName

# sliders
# sliders = driver.find_element(By.CLASS_NAME, "homeslider-container")
# print(len(sliders))  #total number of sliders in homepage

links = driver.find_elements(By.TAG_NAME, 'a')
print(len(links))     # total number of links in homepage

driver.close()

