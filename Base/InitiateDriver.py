from selenium.webdriver import Chrome
from Library import ConfigReader
def startBrowser():
    global driver
    path = "C:/Python38/Scripts/chromedriver.exe"
    driver = Chrome(executable_path=path)
    driver.get(ConfigReader.readConfigData('Details', 'Application_URL'))
    driver.maximize_window()
    return driver

def closeBrowser():
    driver.close()
