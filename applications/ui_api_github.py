from applications.ui.pages.PageLogin import PageLogin


class UIGitHUB:

    def __init__(self, login_url, driver):
        self.login_url = login_url
        self.driver = driver

        self.login_page = PageLogin(self.driver, self.login_url)

    def login(self, username, userpassword):
        return self.login_page.login(username, userpassword)

    def close_browser(self):
        self.driver.close()

    def get_title(self):
        return self.driver.title()

    def error_login(self):
        return PageLogin.error_login(self)
