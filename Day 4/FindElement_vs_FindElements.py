import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://demo.nopcommerce.com/")

#### find_element() - Returns only Single Web Element
#### Three scenario for find_element

# 1. Locator Matching with Single Web Element
element = driver.find_element(By.XPATH, "//input[@id='small-searchterms']")
element.send_keys("Laptop")

# 2. Locator Matching with Multiple Web Elements
mul_element = driver.find_element(By.XPATH, "//div[@class='footer']//a")
print(mul_element.text)  # Prints the first link only from footer i.e. sitemap

# 3. Element not available then throw NoSuchElementException
'''login_element = driver.find_element(By.LINK_TEXT, "Log ")
login_element.click()'''



#### find_elements() - Returns Multiple Web Elements
#### Three scenarios for find_elements

# 1. Locator Matching with Single Web Element
elements = driver.find_elements(By.XPATH, "//input[@id='small-searchterms']")
print(len(elements))    # elements is a list of collection
print(elements[0].send_keys("Laptop"))

# 2. Locator Matching with Multiple Web Elements
mul_elements = driver.find_elements(By.XPATH, "//div[@class='footer']//a")
print(len(mul_elements))  # Prints the first link only from footer i.e. sitemap
print(mul_elements[0].text)

# Using for loop we can extract all the text values of every web elements
for ele in mul_elements:
    print(ele.text)

# 3. Element not available
login_elements = driver.find_elements(By.LINK_TEXT, "Log ")
print("Elements returned: ", len(login_elements))


time.sleep(5)

driver.close()
