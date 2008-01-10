
from org.egedede.bureau.model import Bureau
from org.egedede.bureau.model import Element
from org.egedede.bureau import Configuration

from xml.dom import minidom
from xml.dom.minidom import getDOMImplementation

class BureauStorer:
    
    def __init__(self):
        self.pathManager = None
    
    def store(self,name,bureau):
        
        impl = getDOMImplementation()

        doc = impl.createDocument(None, "desktop", None)
        top_element = doc.documentElement
        text = doc.createTextNode('Some textual content.')
        top_element.appendChild(text)        
        for element in bureau.elements:
            nom=element.nom
            x=element.x
            y=element.y
            commande=element.commande
            icone=element.icone
            xmlElement = doc.createElement("element")
            xmlElement.setAttribute('nom',nom)
            xmlElement.setAttribute('x',str(x))
            xmlElement.setAttribute('y',str(y))
            xmlElement.setAttribute('commande',commande)
            xmlElement.setAttribute('icone',icone)
            top_element.appendChild(xmlElement)
        # writing xml in file
        computedPath = Configuration.Configuration.getInstance('general').getProperty('last_session')
        if self.pathManager:
            computedPath = self.pathManager.computePath(computedPath)
        
        file_object = open(computedPath, "w")
        file_object.write(doc.toprettyxml())
        file_object.close()
