import pytest
import xdist
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import logGen
import pytest_html
from utilities import ExcelUtils


class Test_002_ddt_Login:
    baseUrl = ReadConfig.getApplicationUrl()
    path = "C:\\Users\\Abhay\\Documents\\abhay_imp\\ecommerceProject\\TestData\\loginData.xlsx"

    logger = logGen.loggen()

    def test_login(self, setup):
        self.logger.info("***************** test_login_ddt 002 ***********************")
        self.logger.info("***************** test_login   started   ***********************")
        self.driver = setup
        self.driver.get(self.baseUrl)

        self.lp = LoginPage(self.driver)

        self.rows = ExcelUtils.getRowCount(self.path, "Sheet1")
        print(self.rows)
        self.columns = ExcelUtils.getColumnCount(self.path, "Sheet1")

        status_list = []

        for r in range(2, self.rows+1):
            self.username = ExcelUtils.readData(self.path, r, 1, "Sheet1")
            self.password = ExcelUtils.readData(self.path, r, 2, "Sheet1")
            self.exp = ExcelUtils.readData(self.path, r, 3, "Sheet1")

            self.lp.setUsername(self.username)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()
            time.sleep(15)
            act_title = self.driver.title
            if act_title == 'Dashboard / nopCommerce administration':
                if self.exp == "pass":
                    self.lp.clickLogout()
                    status_list.append("pass")
                elif self.exp == "fail":
                    self.lp.clickLogout()
                    status_list.append("fail")
            elif act_title != 'Dashboard / nopCommerce administration':
                if self.exp == "fail":
                    status_list.append("pass")
                elif self.exp == "pass":
                    status_list.append == "fail"
        if "fail" not in status_list:
            self.logger.info("*************loging_ddt passed *****************")
            self.driver.close()
            assert True
        else:
            self.logger.error("*************loging_ddt failed *******************")
            self.driver.close()
            assert False

        self.logger.info("*************loging_ddt ended *******************")