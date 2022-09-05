from selenium import webdriver
from config.qa_conf import Conf
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from providers.user_providers import UserProvider

class UIGitHUB: # homework v2
    
    def __init__(self, login_url, driver):
        self.login_url = login_url
        self.driver = driver

    def login(self,username, userpassword):
        self.driver.get(self.login_url)

        elem = self.driver.find_element(By.ID, "login_field")
        elem.send_keys(username)
        elem = self.driver.find_element(By.ID, "password")
        elem.send_keys(userpassword)
        elem.send_keys(Keys.ENTER)
        return True
        
    def error_login(self):
        elem = self.driver.find_element(By.ID, 'js-flash-container').text
        return elem

    def close_browser(self):
        self.driver.close()
