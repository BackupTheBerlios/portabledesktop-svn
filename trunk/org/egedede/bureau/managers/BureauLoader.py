# -*- coding: iso-8859-1 -*- 
from org.egedede.bureau.model import Bureau
from org.egedede.bureau.model import Element
from org.egedede.bureau import Configuration
from org.egedede.bureau.managers import FramakeyLoader as fLoader

from xml.dom import minidom
import os


class BureauLoader:
    
    global _path
    _path='\\..\\conf\\'
    
    def __init__(self):
        self.pathManager = None
        self.framakeyLoader = fLoader.FramakeyLoader()

    def load(self,name):
        print "nom de l'objet à charger : ",name
        if name[-4:]==".xml":
            bureau = self.loadXML(name)
        else:
            bureau = self.framakeyLaoder.load(name)
        
        return bureau


        
    def loadXML(self,name):
        bureau = Bureau.Bureau()
        dom = minidom.parse(name)
        elements = dom.getElementsByTagName('element')
        for element in elements:
            nom=element.getAttribute('nom')
            x=int(element.getAttribute('x'))
            y=int(element.getAttribute('y'))
            commande=element.getAttribute('commande')
            icone=element.getAttribute('icone')
            el = Element.Element(nom,x,y,commande,icone)
            bureau.getElements().append(el)
        dom.unlink()
        return bureau

    def loadLastLaunched(self):
        bureau = Bureau.Bureau()
        computedPath = Configuration.Configuration.getInstance('general').getProperty('last_session')
        if self.pathManager:
            computedPath = self.pathManager.computePath(computedPath)
        bureau = self.load(computedPath)
        return bureau
