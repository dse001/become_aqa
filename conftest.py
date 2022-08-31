import pytest

from config.conf_gender import ConfGender
from config.qa_conf import Conf

from applications.github_api import GitHubAPI
from applications.gendersize_api import GenderAPI
from applications.ui_api_github import UIGitHUB

from selenium import webdriver
from selenium.webdriver.chrome.service import Service




@pytest.fixture(scope='session')
def git_hub_api_client():
    git_hub_api_client = GitHubAPI(base_url=Conf.base_url)
    yield git_hub_api_client

@pytest.fixture(scope='session')
def gender_api_client(): #homework_ API
    gender_api_client = GenderAPI(ConfGender.base_url0)
    yield gender_api_client

@pytest.fixture(scope='session')
def ui_github():  #homework
     driver = webdriver.Chrome()
     ui_github = UIGitHUB(Conf.base_url, driver)
     yield ui_github



