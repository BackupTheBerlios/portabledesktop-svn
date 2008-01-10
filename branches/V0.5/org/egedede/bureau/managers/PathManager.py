import os
from org.egedede.bureau import Configuration


class PathManager:
    def __init__(self):
        path = os.getcwd()
        path = os.path.splitdrive(path)[0]
        self.root = path
        self.installPath = os.getcwd()
    
    def computePath(self, path):
        computedPath = path
        confRoot = Configuration.Configuration.getInstance('general').getProperty('usb_root')
        confInstall = Configuration.Configuration.getInstance('general').getProperty('installation_directory')
        computedPath = computedPath.replace(confRoot,self.root)
        computedPath = computedPath.replace(confInstall,self.installPath)
        return computedPath
        
    def computeFile(self, path):
        path = open(path,'rb') ## Ouverture du fichier de configuration en mode lecture
        newPath = './tmp/tmp.txt'
        newFile = open(newPath,'w')
        lignes = path.readlines()

        ## Traitement ligne par ligne
        for lig in lignes: 
            lig = self.computePath(lig)
            newFile.write(lig+"\n")
        path.close() 
        newFile.close()
        return newPath
    def packagePath(self, path):
        computedPath = path
        confRoot = Configuration.Configuration.getInstance('general').getProperty('usb_root')
        confInstall = Configuration.Configuration.getInstance('general').getProperty('installation_directory')
        computedPath = computedPath.replace(self.installPath,confInstall)
        computedPath = computedPath.replace(self.root,confRoot)
        return computedPath
