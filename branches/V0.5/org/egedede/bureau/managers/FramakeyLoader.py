# -*- coding: iso-8859-1 -*- 
from org.egedede.bureau.model import Bureau
from org.egedede.bureau.model import Element
from org.egedede.bureau import Configuration
import os
import wx


class FramakeyLoader:
    
    def __init__(self):
        self.pathManager = None
        self.glyphSize = 16
        self.glyphsFile = "$INSTALL_PATH$/resources/FramaKey/glyph/"


    def load(self,name):
        # ouverture du fichier FramaLauncher.ini se trouvant dans $FRAMA_ROOT$\Framakey\FramaLauncher
        glyphsFile = self.pathManager.computePath(self.glyphsFile)
        if not os.path.isdir(glyphsFile):
            os.makedirs(glyphsFile, mode=0777)
        framaRoot = name[:-41]
        print framaRoot
        framaLauncher  = name[:-17]
        
        #les glyph se trouve dans le fichier  : $FRAMA_ROOT$\Framakey\FramaLauncher\FramaLauncher.bmp
        glyphFilePath = framaLauncher+"FramaLauncher.bmp"
        glyphsBitmap = wx.Bitmap(glyphFilePath,wx.BITMAP_TYPE_BMP)
        nbGlyphs = glyphsBitmap.GetWidth()/self.glyphSize
        print nbGlyphs,glyphsBitmap.GetWidth(),self.glyphSize
        for i in range(nbGlyphs):
            glyph = glyphsBitmap.GetSubBitmap(wx.Rect(i*self.glyphSize,0,self.glyphSize,self.glyphSize))
            print i,str(i), glyph.GetSize()
            print glyph.SaveFile(glyphsFile+str(i)+".jpg",wx.BITMAP_TYPE_JPEG)
        
        #Analyse du fichier
        
        # création des éléménts
        return bureau
        
    def getGlyphBitmap(self, index):
        
        pass