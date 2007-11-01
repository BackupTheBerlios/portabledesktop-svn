#!/usr/bin/env python
#Boa:PyApp:main


import os,sys
import wx
from org.egedede.bureau.model import Bureau as bur
from org.egedede.bureau.model import Element as elt
from org.egedede.bureau.managers import BureauLoader
from org.egedede.bureau.presentation import BureauFrame

class BureauApp(wx.App):
    def OnInit(self):
        print "hello 1 "
        loader = BureauLoader.BureauLoader()
        bureau = loader.load('test')
        frame = BureauFrame.BureauFrame(None, bureau)
        self.SetTopWindow(frame)
        frame.Show(True)
        return True

    def OnPreInit(self):
				# recuperation de la lettre du lecteur.
				path = os.getcwd()
				print path
				print os.path.splitdrive(os.path.splitdrive(path)[1])
				path = os.path.splitdrive(path)[0]
				print path
				pass
def main():
    app = BureauApp()
    app.MainLoop()

if __name__ == '__main__':
    main()
