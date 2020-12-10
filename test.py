import requests
from PyQt5.QtWidgets import QWidget,QPushButton,QGridLayout,QApplication,QLabel,QStatusBar,QAction,qApp,QMainWindow,QLineEdit,QComboBox
from PyQt5.QtGui import QIcon,QPixmap
from PyQt5.QtCore import Qt
from pokemon import *

listPokemon = []
pokemon_first_gen = 151
r = requests.get(f'https://pokeapi.co/api/v2/pokemon?limit={str(pokemon_first_gen)}')

if r.status_code ==200:
    result = r.json()
    for i in range(0, pokemon_first_gen):
        p = Pokemon(result['results'][i]["name"])
        listPokemon.append(p)
        
else :
    print(str(r.status_code))


print(find_pokemon_by_id(1).name)


"""  
for i in range(1, pokemon_first_gen):
    r = requests.get(f'https://pokeapi.co/api/v2/pokemon/{str(i)}/') 
    
    if r.status_code ==200:
        result = r.json()

    print(result["name"])

    p = Pokemon(i, result["name"], result["sprites"]["front_default"])
    listPokemon.append(p)
     """
      
#print(listPokemon)