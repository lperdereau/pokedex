# Classe pokemon et fonction de recherche

import requests

# Création de la classe pokemon
class Pokemon:
    def __init__(self,name, id = None, image = None,types=None,height=None,weight=None):
        self.name = name
        self.id = id
        self.image = image
        self.type=types
        self.height=height
        self.weight=weight

# fonction de recherche de pokémon par intervalle
# retourne une liste de pokémons si possible, sinon rien
# 1 - 152 => first gen
def find_pokemon_by_range(start, end):
    if start < 0:
        return None

    r = requests.get(f'https://pokeapi.co/api/v2/pokemon?offset={str(start)}&limit={str(end-start)}')
    if r.status_code !=200:
        return None
    res = []
    count = 1
    for pokemon_json in r.json()['results']:
        pokemon_json['id'] = start+count
        res.append(pokemon_json)
        count = count + 1
    return res

# fonction de recherche de pokémon par le nom
# retourne une instance de Pokemon si trouvé, sinon rien
def find_pokemon_by_name(name,start=0,end=151):
    r = requests.get(f'https://pokeapi.co/api/v2/pokemon/{str(name)}?offset={str(start)}&limit={str(end-start)}')

    if r.status_code !=200 :
        return None

    result = r.json()
    return Pokemon(result["name"],result["id"],result["sprites"]["front_default"],result["types"][0]["type"]["name"],result["height"],result["weight"])

# fonction de recherche de pokémon par id
# retourne une instance de Pokemon si trouvé, sinon rien.
def find_pokemon_by_id(id,start=0,end=151):
    r = requests.get(f'https://pokeapi.co/api/v2/pokemon/{str(id)}?offset={str(start)}&limit={str(end-start)}')

    if r.status_code !=200 :
        return None

    result = r.json()
    return Pokemon(result["name"],result["id"],result["sprites"]["front_default"],result["types"][0]["type"]["name"],result["height"],result["weight"])