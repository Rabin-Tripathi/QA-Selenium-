from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://admin-demo.nopcommerce.com/login")

driver.find_element(By.ID, "Email").clear()
driver.find_element(By.ID, "Email").send_keys("admin@yourstore.com")

driver.find_element(By.ID, "Password").clear()
driver.find_element(By.ID, "Password").send_keys("admin")

driver.find_element(By.XPATH, "/html/body/div[6]/div/div/div/div/div[2]/div[1]/div/form/div[3]/button").click()

# search box using xpath
driver.find_element(By.XPATH, "//*[@id='search-box']/span/input").send_keys("Languages")

exp_title = "Dashboard / nopCommerce administration"
act_title = driver.title

if act_title == exp_title:
    print("Login Test Successful")
else:
    print("Login Test Failed")

driver.close()


