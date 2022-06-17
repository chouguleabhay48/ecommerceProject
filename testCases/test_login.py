import pytest
import xdist
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import logGen
import pytest_html


class Test_001_Login:
    baseUrl = ReadConfig.getApplicationUrl()
    username = ReadConfig.getUserEmail()
    password = ReadConfig.getPassword()

    logger = logGen.loggen()

    @pytest.mark.sanity
    def test_homePageTitle(self, setup):

        self.logger.info("***************** test_homePageTitle   started   ***********************")
        self.driver = setup
        self.driver.get(self.baseUrl)
        act_title = self.driver.title
        if act_title == "Your store. Login":
            self.driver.close()
            self.logger.info("***************** test_homePageTitle   passed   ***********************")
            assert True
        else:
            self.driver.save_screenshot("C:\\Users\\Abhay\\Documents\\abhay_imp\\ecommerceProject\\Screenshots\\test_homePageTitle.png")
            self.driver.close()
            self.logger.error("***************** test_homePageTitle   failed   ***********************")
            assert False

        # if act_title != 'Your store. Login':

    def test_login(self, setup):
        self.logger.info("***************** test_login   started   ***********************")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.lp = LoginPage(self.driver)
        self.lp.setUsername(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_title = self.driver.title
        time.sleep(15)
        self.lp.clickLogout()
        if act_title == 'Dashboard / nopCommerce administration':
            self.driver.close()
            self.logger.info("***************** test_login   passed   ***********************")
            assert True
        else:
            self.driver.save_screenshot("C:\\Users\\Abhay\\Documents\\abhay_imp\\ecommerceProject\\Screenshots\\Test_login.png")
            self.driver.close()
            self.logger.error("***************** test_login   failed   ***********************")
            assert False

    # @pytest.fixture
    # def setup(self):
    #     self.baseUrl = 'https://admin-demo.nopcommerce.com/'
    #     self.username = 'admin@yourstore.com'
    #     self.password = 'admin'
    #     self.driver = webdriver.Chrome()
    #     self.driver.get(self.baseUrl)
    #     yield
    #     self.driver.close()


