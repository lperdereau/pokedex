from PyQt5.QWidgets import QWidget

class NayLayout(QWidget):

    def __init__(self, liste, index = 0) :
        super().__init__()
        self.liste = liste
        self.index = index
        
    # Boutons de navigation entre les Pokémons
        btnLeft = QPushButton('←')
        btnLeft.setShortcut(Qt.LEFT)
        btnLeft.clicked.connect(precedent)
        
        btnRight = QPushButton('→')
        btnRight.setShortcut(Qt.RIGHT)
        btnRight.clicked.connect(suivant)

    # Passer pour pokémon précédent
    def precedent():
        return None
    # Passer au pokémon suivant
    def suivant():
        return None

        