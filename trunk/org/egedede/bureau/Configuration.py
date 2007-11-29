class Configuration(object):
    configurations={}
    @staticmethod
    def getInstance(name):
        return Configuration.configurations[name]
    
    @staticmethod
    def createInstance(name, fileName):
        conf = Configuration(fileName)
        Configuration.configurations[name]=conf
        return conf
    def __init__(self,fileName=None):
        self.properties= {}
        if fileName:
            self.initProperties(fileName)
        pass
    
    def initProperties(self, fileName):
        path = open(fileName,'rb') ## Ouverture du fichier de configuration en mode lecture
        lignes = path.readlines()

        ## Traitement ligne par ligne
        for lig in lignes: 
            sp = lig.split('#')[0] 
            sp = sp.split('=') 
            if len(sp)==2: self.properties[sp[0].strip()]=sp[1].strip() 
        path.close() 
    def getProperty(self,key):
        return self.properties[key]
