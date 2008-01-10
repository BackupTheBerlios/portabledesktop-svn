# -*- coding: iso-8859-1 -*- 
import os
import subprocess
import sys
class DesktopExecutor:
    def __init__(self):
        self.pathManager = None
        pass
    
    def execute(self,element):
        print element.commande
        #os.system(self.pathManager.computePath(element.commande))
        try:
            cwd = None
            if element.cwd != None:
                cwd = self.pathManager.computePath(element.cwd)
            print "path translated : ",self.pathManager.computePath(element.commande)
            if cwd:
                process = subprocess.Popen(self.pathManager.computePath(element.commande),cwd=cwd)
            else :
                process = subprocess.Popen(self.pathManager.computePath(element.commande))
        except:
            print "Erreur non prevue:", sys.exc_info()[0]
            raise