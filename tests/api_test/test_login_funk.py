import requests
def test_lo():
    r =requests.get('https://api.github.com/users/defunkt')

    e = r.json()
    print(e)

    assert r.json()['login'] == 'defunkt'
def test_swapi0():
    r = requests.get('https://swapi.dev/api/people/10/')
    assert r.json()['name'] == 'Obi-Wan Kenobi'

def test_repos():
    r = requests.get('https://api.github.com/users/repos')
    assert r.json()

def test_get_gender_funk():
    r0 = requests.get(f"https://api.genderize.io/?name=ben")


    assert r0.json()['gender'] == "male"
