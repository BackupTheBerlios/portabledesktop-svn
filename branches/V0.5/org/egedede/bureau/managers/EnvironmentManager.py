import os
import subprocess
class EnvironmentManager:
    def __init__(self):
        pass
    
    def init(self):
        for var in os.environ :
            print var,'=',os.environ[var]
        
