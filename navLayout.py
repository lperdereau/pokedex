from PyQt5.QtWidgets import QWidget,QPushButton

class NavLayout(QWidget):

    def __init__(self, liste, callback, index = 0) :
        super().__init__()
        self.liste = liste
        self.index = index
        self.callback = callback
        
    # Boutons de navigation entre les Pokémons
        self.btnLeft = QPushButton('←')
        btnLeft.setShortcut(Qt.LEFT)
        btnLeft.clicked.connect(self.previous)
        
        self.btnRight = QPushButton('→')
        btnRight.setShortcut(Qt.RIGHT)
        btnRight.clicked.connect(self.next)

        

    # Passer pour pokémon précédent
    def previous(self):
        # Si on va vers index 0, on désactive le bouton précédent(btnLeft)
        if self.index == 1 :
            self.index = self.index - 1
            self.callback(index)
            self.btnLeft.setEnable(False)
        # Si on va vers l'index len(liste)-1, on active le bouton suivant(btnRight)
        elif self.index == len(self.liste) :
            self.index = self.index - 1
            self.callback(index)
            self.btnRight.setEnable(True)
        else :
            self.callback(index)
            self.index = self.index - 1

            
    # Passer au pokémon suivant
    def next(self):
        # si on va vers l'index 1, on active le bouton précédent
        if self.index == 0 :
            self.index = self.index + 1
            self.callback(index)
            self.btnLeft.setEnable(True)
        # Si on arrive au dernier index on désactive le bouton suivant    
        elif self.index == len(self.liste) -1:
            self.index = self.index + 1
            self.callback(index)
            self.btnRight.setEnable(False)
        else :
            self.callback(index)
            self.index = self.index + 1
        