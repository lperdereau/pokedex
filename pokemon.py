# Classe pokemon et fonction de recherche

import requests

# Création de la classe pokemon
class Pokemon:
    def __init__(self,name, id = None, image = None):
        self.name = name
        self.id = id
        self.image = image

# fonction de recherche de pokémon par intervalle
# retourne une liste de pokémons si possible, sinon rien
def find_pokemon_by_range(start, end):
    r = requests.get(f'https://pokeapi.co/api/v2/pokemon?offset={str(start)}limit={str(end)}')
    if r.status_code !=200:
        return None
    return r.json()[start:end]

# fonction de recherche de pokémon par le nom
# retourne une instance de Pokemon si trouvé, sinon rien
def find_pokemon_by_name(name):
    r = requests.get(f'https://pokeapi.co/api/v2/pokemon/{str(name)}/')

    if r.status_code !=200 :
        return None

    result = r.json()
    return Pokemon(result["name"],result["id"],result["sprites"]["front_default"])

# fonction de recherche de pokémon par id
# retourne une instance de Pokemon si trouvé, sinon rien.
def find_pokemon_by_id(id):
    r = requests.get(f'https://pokeapi.co/api/v2/pokemon/{str(id)}/')

    if r.status_code !=200 :
        return None

    result = r.json()
    return Pokemon(result["name"], result["sprites"]["front_default"])