import requests

class Pokemon:
    def __init__(self,name, id = None, image = None):
        self.name = name
        self.id = id
        self.image = image

def find_pokemon_by_range(start, end):
    r = requests.get(f'https://pokeapi.co/api/v2/pokemon?offset={str(start)}limit={str(end)}')
    if r.status_code !=200:
        return None
    return r.json()[start:end]

def find_pokemon_by_name(name):
    r = requests.get(f'https://pokeapi.co/api/v2/pokemon/{str(name)}/')

    if r.status_code !=200 :
        return None

    result = r.json()
    return Pokemon(result["name"], result["sprites"]["front_default"])

def find_pokemon_by_id(id):
    r = requests.get(f'https://pokeapi.co/api/v2/pokemon/{str(id)}/')

    if r.status_code !=200 :
        return None

    result = r.json()
    return Pokemon(result["name"], result["sprites"]["front_default"])