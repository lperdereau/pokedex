from PyQt5.QtWidgets import QWidget,QPushButton,QGridLayout,QLineEdit, QLabel
from PyQt5.QtCore import Qt
from pokemon import find_pokemon_by_id,Pokemon

class teamLayout(QWidget) :
    def __init__(self):
        self.team = []
        self.listWidget = []
        
    def ui(self) :

        listLayout = QGridLayout()

        

        self.setLayout(listLayout)


class itemTeam(QWidget) :
    def __init__(self):
        self.name
        self.btnDelete
        self.btnAdd
        self.labelName

    def ui(self) :
        itemLayout = QGridLayout()

        self.labelName = QLabel(str(self.name))

        self.btnDelete = QPushButton("X")
        self.btnDelete.clicked.connect(self.delete())

        self.btnAdd = QPushButton("+")
        self.btnAdd.clicked.connect(self.add(pokemon))

        itemLayout.addWidget(labelNom, 0,0)
        itemLayout.addWidget(btnSupprimer, 0,1)
        itemLayout.addWidget(btnAjouter, 0,2)

        self.setLayout(itemLayout)
    
    def add(self, pokemon) :
        self.name = pokemon.nom
        self.btnDelete.setEnabled(True)

    def delete(self) :
        self.name = ""
        self.btnDelete.setEnabled(False)

    
