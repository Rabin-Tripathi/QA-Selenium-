import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

# 1. Counting the number of rows and columns
total_rows = driver.find_elements(By.XPATH, "//table[@name='BookTable']//tr")
print("The total number of rows in the table: ", len(total_rows))

total_columns = driver.find_elements(By.XPATH, "//table[@name='BookTable']//tr/th")
print("The total number of columns in the table: ", len(total_columns))

# 2. Read specific row and column data
data = driver.find_element(By.XPATH, "//table[@name='BookTable']//tr[5]/td[1]").text
print("The value/data of given row and column: ", data)


# 3. Read all the rows and columns data
# We do this by using loop statement
'''print("Printing all the rows and data.........")

for r in range(2, total_rows+1):
    for c in range(1, total_columns+1):
        data = driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr["+str(r)+"]/td["+str(c)+"]").text
        print(data, end='           ')
    print()
'''


# 4. Read the data based on the conditions
for r in range(2, total_rows+1):
    author = driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr["+str(r)+"]/td[2]").text
    if author == "Mukesh":
        bookName = driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr[" + str(r) + "]/td[1]").text
        price = driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr[" + str(r) + "]/td[4]").text
        print(bookName, "      ", author, "     ", price)


time.sleep(2)
driver.close()
