import pytest
from selenium import webdriver
import pytest_html
# from selenium.webdriver.common.by import By


@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        print("Chrome is launching")
        driver = webdriver.Chrome()
    elif browser == 'firefox':
        driver = webdriver.Firefox()
    else:
        driver = webdriver.Chrome()
    return driver
    # self.driver.get(self.baseUrl)


def pytest_addoption(parser):                     # this will get value from CLI / hooks
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):                               # This will return the Browser value to setup method
    return request.config.getoption("--browser")


###################### HTML Report ##############################

############# It is hook for adding Environment info to HTML
def pytest_configure(config):
    print("Report Hook started")
    config._metadata['Project Name'] = 'nop commerce'
    config._metadata['Module Name']  = 'Customers'
    config._metadata['Tester'] = 'Abhay'
    config._metadata['Created On'] = '16-06-2022'

############# It is hook for delete / Modify Environment info to HTML
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    print("Report Optional Hook started")
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)
    metadata.pop("Packages", None)