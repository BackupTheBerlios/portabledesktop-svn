
class Bureau:
    
    def __init__(self,name='',elements=[]):
        self.name=name
        self.elements=elements
    def getName(self):
        return self.name
    def getElements(self):
        return self.elements