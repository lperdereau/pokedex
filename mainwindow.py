import requests
import sys
from PyQt5.QtWidgets import QWidget,QPushButton,QGridLayout,QApplication,QLabel,QStatusBar,QAction,qApp,QMainWindow,QLineEdit,QComboBox
from PyQt5.QtGui import QIcon,QPixmap
from pokemonDisplay import AffichagePokemon
from navLayout import NavLayout
from pokemon import *
from teamLayout import *

class MainWindow(QMainWindow):
    def __init__(self,liste):
        super().__init__()
        self.liste = liste
        self.current_pokemon= find_pokemon_by_id(self.liste[0].get('id'))
        self.displayPokemon = AffichagePokemon(self.current_pokemon)
        self.width = 800
        self.height = 800
        
        self.UI()

    def navigation(self, index):
        if index < len(self.liste) and index >= 0:
            self.current_pokemon = find_pokemon_by_id(self.liste[index].get('id'))
            self.displayPokemon.update_UI(self.current_pokemon)
            print(self.current_pokemon.name)
            

    def UI(self):

        # Création des grid layout
        mainGridLayout = QGridLayout()
        #mainGridLayout.setGeometry(0,0,400,400)
        rightGridLayout = QGridLayout()
       
        # Ajout de l'affichage pokemon dans la partie en bas à droite
        rightGridLayout.addWidget(self.displayPokemon,0,0)
        rightGridLayout.addWidget(NavLayout(self.liste,self.navigation),1,0)
           
        
        # Ajout d'un grid layout dans le main layout pour diviser la partie droite du layout principal en deux
        mainGridLayout.addLayout(rightGridLayout,0,1)

        # Ajout de l'affichage de l'équipe dans la partie gauche du mainGridLayout
        #mainGridLayout.addWidget(teamLayout,0,0)

        # self.grid1.addWidget(AffichagePokemon(self.liste[0]),0,0)

        exitAct = QAction(QIcon('images/exit.jpg'),'Quitter',self)
        exitAct.setShortcut('Ctrl+Q')
        exitAct.setStatusTip("Quitter l'application")
        exitAct.triggered.connect(qApp.quit)

        self.statusBar()
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('Pokédex')
        fileMenu.addAction(exitAct)

        widget = QWidget()
        widget.setLayout(mainGridLayout)

        self.setCentralWidget(widget)
        self.setGeometry(300,300,800,500)
        self.setWindowTitle('Pokedex')
        self.show()

def main():
    pokemon_first_gen = [0, 151]
    listPokemon = find_pokemon_by_range(*pokemon_first_gen)
    print(listPokemon)
    app= QApplication(sys.argv)
    mw=MainWindow(listPokemon)
    sys.exit(app.exec_())

if __name__ =='__main__' :
    main()