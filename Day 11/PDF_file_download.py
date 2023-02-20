import time
from selenium import webdriver
from selenium.webdriver.common.by import By

import os

location = os.getcwd()

'''from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
'''


#### How to download the file through automation

def chrome_setup():
    from selenium.webdriver.chrome.service import Service as ChromeService
    from webdriver_manager.chrome import ChromeDriverManager

    # if we want to download the file in desired location we need to use dictionary
    preferences = {"download.default_directory": location, "plugins.always_open_pdf_externally": True}
    ops = webdriver.ChromeOptions()
    ops.add_experimental_option("prefs", preferences)

    drivers = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=ops)
    return drivers


def edge_setup():
    from selenium.webdriver.edge.service import Service as EdgeService
    from webdriver_manager.microsoft import EdgeChromiumDriverManager

    # if we want to download the file in desired location we need to use dictionary
    preferences = {"download.default_directory": location, "plugins.always_open_pdf_externally": True}
    ops = webdriver.EdgeOptions()
    ops.add_experimental_option("prefs", preferences)

    drivers = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()), options=ops)
    return drivers


def firefox_setup():
    from selenium.webdriver.firefox.service import Service as FirefoxService
    from webdriver_manager.firefox import GeckoDriverManager

    # settings and adding the preferences
    ops = webdriver.FirefoxOptions()
    ops.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/pdf")     # file --> MIME Types
    ops.set_preference("browser.download.manager.showWhenStarting", False)
    ops.set_preference("browser.download.folderList", 2)
    ops.set_preference("browser.download.dir", location)
    ops.set_preference("pdfjs.disabled", True)

    # if we pass 0, the file will be download in desktop
    # if we pass 1, the file will be download in download folder
    # if we pass 2, the file will be download in desired folder

    drivers = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=ops)
    return drivers


# Automation Code for Chrome Browser
# driver = chrome_setup()

# Automation Code for edge Browser
# driver = edge_setup()

# Automation Code for firefox Browser
driver = firefox_setup()


driver.get("https://file-example.com/en/sample-documents-files/sample-pdf-download")
driver.maximize_window()
driver.find_element(By.XPATH, "//tbody/tr[1]/td[3]/a[1]").click()

time.sleep(3)
driver.close()
