
class Element:
    
    def __init__(self,nom,x,y,commande,icone,selected=False):
        self.nom=nom
        self.x=x
        self.y=y
        self.commande = commande
        self.icone=icone
        self.selected=selected
    
    def getX(self):
        return self.x
    def getY(self):
        return self.y
    def getNom(self):
        return self.nom
    def getCommande(self):
        return self.commande
    def getIcone(self):
        return self.icone
    def isSelected(self):
        return self.selected