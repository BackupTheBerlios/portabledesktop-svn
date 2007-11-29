import os
import subprocess
class DesktopExecutor:
    def __init__(self):
        self.pathManager = None
        pass
    
    def execute(self,element):
        print element.commande
        #os.system(self.pathManager.computePath(element.commande))
        process = subprocess.Popen(self.pathManager.computePath(element.commande))