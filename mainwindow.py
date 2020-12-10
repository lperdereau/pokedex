import requests
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon,QPixmap
from gridlayout import GridLayout
from pokemon import *

class MainWindow(QMainWindow):
    def __init__(self,liste):
        super().__init__()
        self.liste = liste
        self.grid = GridLayout(self.liste[0])
        self.UI()

    def UI(self):
        # partie menu
        #ACTIONS
        exitAct = QAction(QIcon('images/exit.jpg'),'Quitter',self)
        exitAct.setShortcut('Ctrl+Q')
        exitAct.setStatusTip("Quitter l'application")
        exitAct.triggered.connect(qApp.quit)

        suivAct = QAction(QIcon('images/droite.png'),'Next',self)
        suivAct.setShortcut('Ctrl+N')
        suivAct.setStatusTip("Personnage suivant")
        suivAct.triggered.connect(self.SuivantClick)
        
        precAct = QAction(QIcon('images/gauche.jpg'),'Before',self)
        precAct.setShortcut('Ctrl+B')
        precAct.setStatusTip("Perssonnage précédent")
        precAct.triggered.connect(self.PrecedentClick)

        suppAct = QAction(QIcon('images/supprimer.jpg'),'Delete',self)
        suppAct.setShortcut('Ctrl+D')
        suppAct.setStatusTip("Supprimer le personnage")
        suppAct.triggered.connect(self.SupprimerClick)


        #LIAISON ACTIONS ET MENUS
        self.statusBar()
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('Pokédex')
        fileMenu.addAction(exitAct)
        fileMenu.addAction(suppAct)

        fileMenu = menubar.addMenu('Equipe de pokémon')
        fileMenu.addAction(suivAct)
        fileMenu.addAction(precAct)

        self.setCentralWidget(self.grid)
        self.setGeometry(300,300,450,200)
        self.setWindowTitle('Presentation de '+ self.liste[0].name)
        self.show()
    
    def SuivantClick(self):
        self.close()
        self.cpm+=1
        if self.cpm > len(self.liste)-1:
            self.cpm=0
        self.grid = MainWindow(self.liste,self.cpm)
        
    
    def PrecedentClick(self):
        self.close()
        self.cpm-=1
        if self.cpm < 0:
            self.cpm=len(self.liste)-1
        self.grid = MainWindow(self.liste,self.cpm)

    def SupprimerClick(self):
        self.close()
        self.liste.remove(self.liste[self.cpm])
        if self.cpm > len(self.liste)-1:
            self.cpm=0
        self.grid = MainWindow(self.liste,self.cpm)

def main():
    listPokemon = []
    pokemon_first_gen = 151
    r = requests.get(f'https://pokeapi.co/api/v2/pokemon?limit={str(pokemon_first_gen)}')
    if r.status_code ==200:
        result = r.json()
        for i in range(0, pokemon_first_gen):
            p = Pokemon(result['results'][i]["name"])
            listPokemon.append(p)
    else :
        print("erreur")    
    app= QApplication(sys.argv)
    mw=MainWindow(listPokemon)
    #gr = GridLayout(listPokemon[0])
    sys.exit(app.exec_())

if __name__ =='__main__' :
    main()