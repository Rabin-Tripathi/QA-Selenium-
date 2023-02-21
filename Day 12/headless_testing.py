import time
from selenium import webdriver


### Headless Mode --> it is just like a real browser with no User Interface
# For Chrome
def headless_chrome():
    from selenium.webdriver.chrome.service import Service as ChromeService
    from webdriver_manager.chrome import ChromeDriverManager

    ops = webdriver.ChromeOptions()
    ops.add_argument("--headless=new")
    drivers = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=ops)
    return drivers


# For Edge
def headless_edge():
    from selenium.webdriver.edge.service import Service as EdgeService
    from webdriver_manager.microsoft import EdgeChromiumDriverManager

    ops = webdriver.EdgeOptions()
    ops.add_argument("--headless=new")
    drivers = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()), options=ops)
    return drivers


# For Firefox
def headless_firefox():
    from selenium.webdriver.firefox.service import Service as FirefoxService
    from webdriver_manager.firefox import GeckoDriverManager

    ops = webdriver.FirefoxOptions()
    ops.add_argument("--headless=new")
    drivers = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=ops)
    return drivers


# Chrome browser
# driver = headless_chrome()

# edge browser
# driver = headless_edge()

# firefox browser
driver = headless_firefox()

driver.get("https://www.dummyticket.com/")
print(driver.title)
print(driver.current_url)

time.sleep(3)
driver.close()
