from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://www.facebook.com/")
driver.maximize_window()

# tag and id --> tagname#id
# driver.find_element(By.CSS_SELECTOR, "input#m_login_email").send_keys("abc@gmail.com")

# tag and class --> tagname.valueofClass
# driver.find_element(By.CSS_SELECTOR, "input._56bg _4u9z _5ruq _8qtn").send_keys("abc@gmail.com")

# tag and attribute --> tagname[attribute=value]
# driver.find_element(By.CSS_SELECTOR, "input[name=email]").send_keys("abc@gmail.com")

# tag class attribute --> tagname.valueofClass[attribute=value]
# driver.find_element(By.CSS_SELECTOR, "input._56bg _4u9z _5ruq _8qtn[name=email]").send_keys("xyz")

driver.close()
