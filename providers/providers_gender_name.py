import json

from config.conf_gender import ConfGender

# Home work! v2

class GenderProvider:
    with open (ConfGender.path_to_provider) as file:
        get_gender_type = json.load(file)
