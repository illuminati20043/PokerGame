class Joueur :
    def __init__(self, nom, main, tapis):
        self.nom = nom
        self.tapis = tapis
        self.main = []
    
    def recevoir(self, cartes):
        self.main.extend(cartes)
    
    def miser(self, montant):
        if(montant<= self.tapis):
            self.tapis -= montant
            return montant
        else:
            raise ValueError("Pas assez de jetons")
        
    def coucher(self):
        self.main = []
    