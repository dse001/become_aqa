import pytest
from providers.user_providers import out #this users data

import requests
def test_user_exists(git_hub_api_client): #this import fixture

    #git_hub_api_client = GitHubAPI(base_url=Conf.base_url)
    user = git_hub_api_client.get_user(username=out.username)
    print(user)
    assert user['login'] == out.username

def test_user_not_exists(git_hub_api_client):
    #git_hub_api_client = GitHubAPI(base_url=Conf.base_url)
    #user = git_hub_api_client.get_user(username='fghfhyfhgjgjg78ugjyujh')
    with pytest.raises(requests.exceptions.HTTPError):
        user = git_hub_api_client.get_user(username=out.fakeusername)


    #assert user['message'] == 'Not Found'






