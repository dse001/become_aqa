import requests
from config.conf_gender import ConfGender
from applications.gendersize_api import GenderAPI
from providers.providers_gender_name import GenderProvider
# Home work!

def test_get_gender_male(gender_api_client):
    gender_type = gender_api_client.get_gender(name=GenderProvider.data['name_male'])
    assert gender_type['gender'] == "male"


def test_get_gender_female(gender_api_client):
    gender_type = gender_api_client.get_gender(name=GenderProvider.data['name_female'])
    assert gender_type['gender'] == "female"


def test_get_gender_number(gender_api_client):
    gender_type = gender_api_client.get_gender(name=GenderProvider.data['name_number'])
    assert gender_type['gender'] != ("female" or "male")
    assert gender_type['gender'] is None #homework v2

