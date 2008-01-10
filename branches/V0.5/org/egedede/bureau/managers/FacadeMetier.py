from org.egedede.bureau.managers import BureauLoader as load
from org.egedede.bureau.managers import BureauStorer as save
from org.egedede.bureau.managers import DesktopExecutor as execute
from org.egedede.bureau.managers import PathManager as path



class FacadeMetier:
    def __init__(self):
        self.loader = load.BureauLoader()
        self.saver = save.BureauStorer()
        self.executor = execute.DesktopExecutor()
        self.pathManager = path.PathManager()
        self.loader.pathManager = self.pathManager
        self.saver.pathManager = self.pathManager
        self.executor.pathManager = self.pathManager

    def load(self, fileName):
        return self.loader.load(fileName)
        
    def loadLastLaunched(self):
        return self.loader.loadLastLaunched()
        
    def execute(self, element):
        return self.executor.execute(element)

    def save(self, fileName, desktop):
        return self.saver.store(fileName,desktop)

    def computePath(self, path):
        return self.pathManager.computePath(path)

    def computeFile(self, path):
        return self.pathManager.computeFile(path)