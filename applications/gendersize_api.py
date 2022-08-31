import requests

class GenderAPI:
    def __init__(self, url_base_gender: str):
        self.url_base_gender = url_base_gender

    def get_gender(self, name: str):
        r = requests.get(f"{self.url_base_gender}/?name={name}")
        r.raise_for_status()
        # if r.status_code != 200:
        #    raise HTTPError\\
        return r.json()
