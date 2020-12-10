import sys
from PyQt5.QtWidgets import QWidget,QPushButton,QGridLayout,QApplication,QLabel,QStatusBar,QAction,qApp,QMainWindow,QLineEdit,QComboBox
from PyQt5.QtCore import Qt

class GridLayout(QWidget):
    def __init__(self,pokemon):
        self.pokemon = pokemon
        super().__init__()
        self.UI()

    def UI(self):
        
        # corps de l'application
        nomLabel = QLabel("Nom :")
        nomValue = QLabel(str(self.pokemon.name))

        grid = QGridLayout()

        
        grid.addWidget(nomLabel,0,1)
        grid.addWidget(nomValue,0,2)



        # partie exécutée
        self.setLayout(grid)
        self.setGeometry(300,300,200,200)
        self.setWindowTitle('Presentation de '+ self.pokemon.name)
        self.show()