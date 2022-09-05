import json
from config.conf_gender import ConfGender
# Home work! v2

class GenderProvider:
    with open (ConfGender.path_to_provider) as file:
        data = json.load(file)
