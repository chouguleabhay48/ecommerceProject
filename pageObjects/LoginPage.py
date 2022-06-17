import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains

class LoginPage :
    textbox_username_id = "Email"
    textbox_password_id = "Password"
    button_login_xpath = '//button[@class="button-1 login-button"]'
    link_logout_xpath = '/html/body/div[3]/nav/div/ul/li[3]/a'


    def __init__(self, driver ):
        self.driver = driver


    def setUsername(self, username ):
        self.driver.find_element ( By.ID , self.textbox_username_id).clear()
        self.driver.find_element ( By.ID , self.textbox_username_id).send_keys(username)


    def setPassword ( self, password ) :
        self.driver.find_element ( By.ID, self.textbox_password_id).clear()
        self.driver.find_element ( By.ID, self.textbox_password_id).send_keys(password)

    def clickLogin(self) :
        self.driver.find_element ( By.XPATH, self.button_login_xpath).click()


    def clickLogout ( self ) :
        try:
            self.driver.switch_to.alert.accept()
            self.driver.switch_to.alert.accept()
            time.sleep(15)
            self.driver.find_element(By.XPATH, self.link_logout_xpath).click()
        except:
            self.driver.find_element(By.XPATH, self.link_logout_xpath).click()

        
        # action = ActionChains(self.driver)
        # element1 = self.driver.find_element(By.XPATH, self.link_logout_xpath)
        # action.move_to_element(element1).click().perform()

        # try:
        #     action = ActionChains(self.driver)
        #     self.driver.switch_to.alert.accept()
        #     self.driver.switch_to.alert.accept()
        #     WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.XPATH, self.link_logout_xpath))).click()
        # except:
        #     WebDriverWait(self.driver, 30 ).until(EC.visibility_of_element_located((By.XPATH, self.link_logout_xpath))).click()






