import json
from config.qa_conf import Conf
# Home work! v2

class UserProvider:
    with open (Conf.path_provider_conf) as file:
        data = json.load(file)

