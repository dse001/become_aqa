from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class PageLogin:

    def __init__(self, driver, login_url):
        self.driver = driver
        self.login_url = login_url

    def navigate(self):
        self.driver.get(self.login_url)

    def login_field(self):
        return self.driver.find_element(By.ID, "login_field")

    def pass_filed(self):
        return self.driver.find_element(By.ID, "password")

    def login_btp(self):
        return self.driver.find_element(By.NAME, "commit")

    def login(self, username, userpassword):
        self.navigate()
        self.login_field().send_keys(username)
        self.pass_filed().send_keys(userpassword)
        self.login_btp().click()

        return True

    def error_login(self):
        return self.driver.find_element(By.ID, 'js-flash-container').text

    def proceed_to_signup_page(self):
        self.sign_up_link.click()

        return True

    def get_title(self):
        return self.driver.title
