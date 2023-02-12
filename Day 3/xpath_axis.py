from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://money.rediff.com/gainers/bse/daily/groupa")

'''# self keyword or element or node
text_message = driver.find_element(By.XPATH, "/html/body/div[2]/div[5]/table/tbody/tr[18]/td[1]/a/self::a").text
print(text_message)

# Parent node or element
text_message = driver.find_element(By.XPATH, "/html/body/div[2]/div[5]/table/tbody/tr[18]/td[1]/a/parent::td").text
print(text_message)'''

'''
# Child node or element
child = driver.find_elements(By.XPATH, "/html/body/div[2]/div[5]/table/tbody/tr[18]/td[1]/a/ancestor::tr/child::td")
print(len(child))
'''

'''
# Ancestor element or node
text_message = driver.find_element(By.XPATH, "/html/body/div[2]/div[5]/table/tbody/tr[18]/td[1]/a/ancestor::tr").text
print(text_message)
'''

'''
# Descendant element or node
desc = driver.find_elements(By.XPATH, "/html/body/div[2]/div[5]/table/tbody/tr[18]/td[1]/a/ancestor::tr/descendant::*")
print("Number of descendant nodes: ", len(desc))
'''

'''
# Following element or node
followings = driver.find_elements(By.XPATH, "/html/body/div[2]/div[5]/table/tbody/tr[18]/td[1]/a/ancestor::tr/following::*")
print("Number of following nodes: ", len(followings))
'''

'''
# Following siblings element or node
following_siblings = driver.find_elements(By.XPATH, "/html/body/div[2]/div[5]/table/tbody/tr[18]/td[1]/a/ancestor::tr/following-sibling::tr")
print("Number of following siblings nodes: ", len(following_siblings))      # 365
'''

'''
# Preceding nodes or elements
preceding = driver.find_elements(By.XPATH, "/html/body/div[2]/div[5]/table/tbody/tr[18]/td[1]/a/ancestor::tr/preceding::tr")
print("Number of preceding nodes: ", len(preceding))       # * -331, tr- 18
'''

# preceding siblings nodes or elements
preceding_siblings = driver.find_elements(By.XPATH, "/html/body/div[2]/div[5]/table/tbody/tr[18]/td[1]/a/ancestor::tr/preceding-sibling::tr")
print("Number of preceding siblings nodes: ", len(preceding_siblings))      # 17


driver.close()
