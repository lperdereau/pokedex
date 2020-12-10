# Classe GridLayout 
from PyQt5.QtWidgets import QWidget,QPushButton,QGridLayout,QApplication,QLabel,QStatusBar,QAction,qApp,QMainWindow,QLineEdit,QComboBox
from PyQt5.QtGui import QIcon,QPixmap
from pokemon import *
from PyQt5.QtCore import Qt
import os

# Création de la classe GridLayout
class AffichagePokemon(QWidget):
    def __init__(self, pokemon):
        super().__init__()
        self.pokemon=pokemon
        self.label = QLabel(self)
        self.UI()

    def UI(self):
        
        # corps de l'application

        # Création de l'affichage du nom du Pokémon
        self.numLabel = QLabel("Number :")
        self.numValue = QLabel(str(self.pokemon.id))

        self.nomLabel = QLabel("Name :")
        self.nomValue = QLabel(str(self.pokemon.name))

        self.typeLabel = QLabel("Type :")
        self.typeValue = QLabel(str(self.pokemon.type))  

        self.heightLabel = QLabel("Height :")
        self.heightValue = QLabel(str(self.pokemon.height)) 

        self.weightLabel = QLabel("Weight :")
        self.weightValue = QLabel(str(self.pokemon.weight)) 

        self.Creation_img()
        
        # Initialisation du Layout pour l'affichage des données
        grid = QGridLayout()

        #Ajout des composants dans le Layout
        grid.addWidget(self.numLabel,0,0)
        grid.addWidget(self.numValue,0,1)
        grid.addWidget(self.nomLabel,1,0)
        grid.addWidget(self.nomValue,1,1)
        grid.addWidget(self.typeLabel,2,0)
        grid.addWidget(self.typeValue,2,1)
        grid.addWidget(self.heightLabel,3,0)
        grid.addWidget(self.heightValue,3,1)
        grid.addWidget(self.weightLabel,4,0)
        grid.addWidget(self.weightValue,4,1)

        grid.addWidget(self.label,5,1)
        self.setLayout(grid)
        
        # Affichage du Layout avec les informations de la fenêtre
        # self.setLayout(grid)
        # self.setGeometry(300,300,200,200)
        # self.setWindowTitle('Presentation de '+ self.pokemon.name)
        # self.show()

    def Creation_img(self):
        # Récupération de l'image lié au Pokémon
        os.remove('img_pokemon.png')
        r = requests.get(self.pokemon.image, allow_redirects=True)
        open('img_pokemon.png', 'wb').write(r.content)
        print(len(r.content))

        # Création de l'affichage du Pokémon
        img = QPixmap('img_pokemon.png')
        #imgsmaller = img.scaled(160,160)
        self.label.setPixmap(img)

    def update_UI(self,pokemon):
        self.pokemon=pokemon
        self.nomValue.setText(pokemon.name)
        self.typeValue.setText(pokemon.type)
        self.numValue.setText(str(pokemon.id))
        self.heightValue.setText(str(pokemon.height))
        self.weightValue.setText(str(pokemon.weight))
        
        self.Creation_img()