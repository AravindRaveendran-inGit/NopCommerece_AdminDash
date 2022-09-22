import pytest
from selenium import webdriver
from selenium.webdriver.edge.service import Service

@pytest.fixture()
def setup(browser):
    if browser == "chrome":
        srvcObj = Service("C:/Softwares/WebDrivers/chromedriver_win32/chromedriver.exe")
        driver = webdriver.Chrome(service=srvcObj)
        print("Lauching chrome...")
        driver.maximize_window()

    elif browser == "edge":
        srvcObj = Service("C:/Softwares/WebDrivers/edgedriver_win64/msedgedriver.exe")
        driver = webdriver.Edge(service=srvcObj)
        print("Lauching Ms Edge...")
        driver.maximize_window()

    else:
        print("You have not selected a browser, running the script on chrome")
        srvcObj = Service("C:/Softwares/WebDrivers/chromedriver_win32/chromedriver.exe")
        driver = webdriver.Chrome(service=srvcObj)
        print("Lauching chrome...")
        driver.maximize_window()

    return driver


def pytest_addoption(parser): # This will get the value from CLI.
    parser.addoption("--browser")

@pytest.fixture()
def browser(request): # This will return the Browser value to setup method
    return request.config.getoption("--browser")

# """ Hook for adding environment info in HTML Report """ #

def pytest_configure(config): #Hook for adding environmental info to the HTML report
    config._metadata['Project'] = "Nop Commerce Admin"
    config._metadata['Module'] = "Customers"
    config._metadata['Tester'] = "Aravind"

@pytest.mark.optionalhook #Hook for deleting or modifying environment info to HTML report
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)
