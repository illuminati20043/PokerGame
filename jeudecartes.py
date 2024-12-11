import random
import carte
class JeuDeCartes : 
    valeurs = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Valet', 'Dame', 'Roi', 'As']
    couleurs = ["\u2665","\u2666", "\u2663", "\u2660"]

    def __init__(self):
        self.cartes = [carte.Carte(valeur, couleur) for valeur in self.valeurs for couleur in self.couleurs]
        random.shuffle(self.cartes)
    
    def distribuer(self, nombre):
        cartes_distribuees = []
        for _ in range(nombre):
            cartes_distribuees.append(self.cartes.pop())
        return cartes_distribuees

    
