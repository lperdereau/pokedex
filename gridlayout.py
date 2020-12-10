# Classe GridLayout 
from PyQt5.QtWidgets import QWidget,QPushButton,QGridLayout,QApplication,QLabel,QStatusBar,QAction,qApp,QMainWindow,QLineEdit,QComboBox
from PyQt5.QtGui import QIcon,QPixmap
from pokemon import *


# Création de la classe GridLayout
class GridLayout(QWidget):
    def __init__(self,pokemon):
        self.pokemon= find_pokemon_by_name(pokemon.name)
        super().__init__()
        self.UI()

    def UI(self):
        
        # corps de l'application
        nomLabel = QLabel("Nom :")
        nomValue = QLabel(str(self.pokemon.name))
        print(self.pokemon.image)      
        
        r = requests.get(self.pokemon.image, allow_redirects=True)

        open('img_pokemon.png', 'wb').write(r.content)
        

        label = QLabel(self)
        img = QPixmap('img_pokemon.png')
        imgsmaller = img.scaled(160,160)
        label.setPixmap(imgsmaller)

        grid = QGridLayout()

        
        grid.addWidget(nomLabel,0,1)
        grid.addWidget(nomValue,0,2)

        grid.addWidget(label,1,1)



        # partie exécutée
        self.setLayout(grid)
        self.setGeometry(300,300,200,200)
        self.setWindowTitle('Presentation de '+ self.pokemon.name)
        self.show()