from applications.ui_api_github import UIGitHUB
from providers.user_providers import UserProvider
from config.qa_conf import Conf
from selenium import webdriver
#homework v2!

def test_ui_login_fall(ui_github):
    ui_github.login(username=UserProvider.data['fakeusername'], userpassword=UserProvider.data['fakeusername'])
    assert ui_github.error_login() == 'Incorrect username or password.'
