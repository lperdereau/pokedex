# Classe GridLayout 
from PyQt5.QtWidgets import QWidget,QPushButton,QGridLayout,QApplication,QLabel,QStatusBar,QAction,qApp,QMainWindow,QLineEdit,QComboBox
from PyQt5.QtGui import QIcon,QPixmap
from pokemon import *
from PyQt5.QtCore import Qt


# Création de la classe GridLayout
class AffichagePokemon(QWidget):
    def __init__(self,pokemon):
        self.pokemon= find_pokemon_by_name(pokemon.name)
        super().__init__()
        self.UI()

    def UI(self):
        
        # corps de l'application

        # Création de l'affichage du nom du Pokémon
        nomLabel = QLabel("Nom :")
        nomValue = QLabel(str(self.pokemon.name))      

        # Récupération de l'image lié au Pokémon
        r = requests.get(self.pokemon.image, allow_redirects=True)
        open('img_pokemon.png', 'wb').write(r.content)

        # Création de l'affichage du Pokémon
        label = QLabel(self)
        img = QPixmap('img_pokemon.png')
        imgsmaller = img.scaled(160,160)
        label.setPixmap(imgsmaller)

        # Initialisation du Layout pour l'affichage des données
        grid = QGridLayout()

        #Ajout des composants dans le Layout
        grid.addWidget(nomLabel,0,1)
        grid.addWidget(nomValue,0,2)
        grid.addWidget(label,1,1)
        
        # grid.addWidget(btnLeft, 6,0)
        # grid.addWidget(btnRight, 6,1)
        
        # Affichage du Layout avec les informations de la fenêtre
        self.setLayout(grid)
        self.setGeometry(300,300,200,200)
        self.setWindowTitle('Presentation de '+ self.pokemon.name)
        self.show()
