import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://demo.automationtesting.in/Windows.html")
driver.maximize_window()

'''
window_id = driver.current_window_handle
print(window_id)        # CDwindow-C710A3105C9BC367634E9C73CF1682CB
                        # CDwindow-CCC3E08ACD7D718B2A69894DF3126CE9
'''

driver.find_element(By.XPATH, "//a[@href='http://www.selenium.dev']//button[@class='btn btn-info'][normalize-space()='click']").click()
windows_id = driver.window_handles

# Approach 1
'''
parentWindow_id = windows_id[0]
childWindow_id = windows_id[1]

print(parentWindow_id, childWindow_id)
#CDwindow-A619D35F27B6DAB7DA333D4653146F84 CDwindow-1E68F80FE95A0D3D69A6D90AC52E58E6

# Switching into the child window
driver.switch_to.window(childWindow_id)
print("Title of the child window is :", driver.title)

# Again switching to the parent window
driver.switch_to.window(parentWindow_id)
print("Title of the parent window is: ", driver.title)
'''

'''
# Approach 2 --> Using for loop
for windId in windows_id:
    driver.switch_to.window(windId)
    print(driver.title)
'''

time.sleep(3)

# Closing the specific browser in Multiple browser
for windId in windows_id:
    driver.switch_to.window(windId)
    if driver.title == "Frames & windows" or driver.title == 'Selenium':
        driver.close()


driver.close()
