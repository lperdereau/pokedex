from PyQt5.QtWidgets import QWidget,QPushButton,QGridLayout
from PyQt5.QtCore import Qt
from pokemon import find_pokemon_by_id,Pokemon

class NavLayout(QWidget):

    def __init__(self, liste, callback, index = 0) :
        super().__init__()
        self.liste = liste
        self.index = index
        self.callback = callback
        
        # Boutons de navigation entre les Pokémons
        self.btnLeft = QPushButton('←')
        #self.btnLeft.setShortcut('Qt.Key_LEFT')
        self.btnLeft.clicked.connect(self.previous)
        
        self.btnRight = QPushButton('→')
        # self.btnRight.setShortcut(Qt.Key_RIGHT)
        self.btnRight.clicked.connect(self.next)

        if self.index == 0:
            self.btnLeft.setEnabled(False)
        
        if self.index == len(self.liste)-1:
            self.btnRight.setEnabled(False)

        layout = QGridLayout()

        layout.addWidget(self.btnLeft, 0, 0)
        layout.addWidget(self.btnRight, 0, 1)

        self.setLayout(layout)


    # Passer pour pokémon précédent
    def previous(self):
        print(str(self.index))
        # Si on va vers index 0, on désactive le bouton précédent(btnLeft)
        if self.index == 1 :
            self.index = self.index - 1
            self.callback(self.index)
            self.btnLeft.setEnabled(False)
        # Si on va vers l'index len(liste)-1, on active le bouton suivant(btnRight)
        elif self.index == len(self.liste) :
            self.index = self.index - 1
            self.callback(self.index)
            self.btnRight.setEnabled(True)
        else :
            self.index = self.index - 1
            self.callback(self.index)

            
    # Passer au pokémon suivant
    def next(self):
        print(str(self.index))
        # si on va vers l'index 1, on active le bouton précédent
        if self.index == 0 :
            self.index = self.index + 1
            self.callback(self.index)
            self.btnLeft.setEnabled(True)
        # Si on arrive au dernier index on désactive le bouton suivant    
        elif self.index == len(self.liste) -1:
            self.index = self.index + 1
            self.callback(self.index)
            self.btnRight.setEnabled(False)
        else :
            self.index = self.index + 1
            self.callback(self.index)
        