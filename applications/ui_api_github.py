from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class UIGitHUB:
    def __init__(self, url, driver):
        self.base_url = url
        self.driver = driver
    def login(self,username, userpassword):
        self.driver.get(self.url)

        elem = self.driver.find_element(By.ID, "login_field")
        elem.send_keys("fghfhyfhgjgjg78ugjyujh")

        elem0 = self.driver.find_element(By.ID, "password")
        elem0.send_keys("fghfhyfhgjgjg78ugjyujh")

        elem0.send_keys(Keys.ENTER)
