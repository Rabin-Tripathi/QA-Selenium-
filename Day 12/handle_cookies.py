import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.implicitly_wait(4)

driver.get("https://www.dummyticket.com/")
driver.maximize_window()


# Note: - Cookies are not a single object actually it is a multiple attribute where each attribute associated have some value.
# It is in a dictionary form.


#### Capture cookies from the browser
cookies = driver.get_cookies()
print("Number of cookies: ", len(cookies))  # 9

### Printing the details of all cookies using for loop
for c in cookies:
    # print(c)
    print(c.get('name'), ":", c.get('value'))   # Capturing the particular cookies value

#### How to add your new cookie to the browser
driver.add_cookie({"name": "MyCookie", "value": "2468"})
cookies = driver.get_cookies()
print("Number of cookies after adding my own cookies: ", len(cookies))  # 10

#### How to specific cookie from the browser
driver.delete_cookie("MyCookie")
cookies = driver.get_cookies()
print("Number of cookies after deleting my own cookies: ", len(cookies))  # 9

#### Deleting all the cookies
driver.delete_all_cookies()
cookies = driver.get_cookies()
print("Number of cookies after deleting all the cookies: ", len(cookies))  # 0


time.sleep(3)
driver.close()
