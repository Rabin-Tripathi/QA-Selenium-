import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()

# Login
driver.find_element(By.XPATH, "//input[@placeholder='Username']").send_keys("Admin")
driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys("admin123")
driver.find_element(By.XPATH, "//button[@type='submit']").click()


# Admin--> User Management--> Users
driver.find_element(By.XPATH, "//a[normalize-space()='']").click()
driver.find_element(By.XPATH, "//span[normalize-space()='User Management']").click()
driver.find_element(By.XPATH, "//ul[@role='menu']//li").click()

# Total rows in a table
rows = len(driver.find_elements(By.XPATH, "//div[@class='oxd-table-card']"))
print("Total number of rows in a table", rows)

count = 0
for r in range(1, rows+1):
    status = driver.find_element(By.XPATH, "//div[@class='oxd-table']//div//div[5]").text
    if status == "Enabled":
        count = count+1

print("Total Numbers of users: ", rows)
print("Total number of enabled users is ", count)
print("NUmber of disabled users: ", (rows-count))

time.sleep(3)
driver.close()
