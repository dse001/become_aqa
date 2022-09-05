import pytest
from providers.user_providers import UserProvider #this users data
import requests

def test_user_exists(git_hub_api_client): #this import fixture

    user = git_hub_api_client.get_user(username=UserProvider.data['username'])
    print(user)
    assert user['login'] == UserProvider.data['username']

def test_user_not_exists(git_hub_api_client):
    with pytest.raises(requests.exceptions.HTTPError):
        user = git_hub_api_client.get_user(username=UserProvider.data['fakeusername'])
        assert user['message'] == 'Not Found'


