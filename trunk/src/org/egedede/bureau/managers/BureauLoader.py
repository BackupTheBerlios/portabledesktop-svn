
from org.egedede.bureau.model import Bureau
from org.egedede.bureau.model import Element

from xml.dom import minidom
import os


class BureauLoader:
    
    global _path
    _path='\\..\\conf\\'
    
    def load(self,name):
        print os.getcwd()+_path+name+'.xml'
        bureau = Bureau.Bureau()
        dom = minidom.parse(os.getcwd()+_path+name+'.xml')

        elements = dom.getElementsByTagName('element')
        for element in elements:
            print element.getAttribute('nom')
            nom=element.getAttribute('nom')
            x=int(element.getAttribute('x'))
            y=int(element.getAttribute('y'))
            commande=element.getAttribute('commande')
            icone=element.getAttribute('icone')
            el = Element.Element(nom,x,y,commande,icone)
            bureau.getElements().append(el)
				dom.unlink()
        return bureau
