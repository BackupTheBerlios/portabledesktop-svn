#!/usr/bin/env python
#Boa:PyApp:main


import os,sys
import wx
from org.egedede.bureau.model import Bureau as bur
from org.egedede.bureau.model import Element as elt
from org.egedede.bureau.managers import FacadeMetier
from org.egedede.bureau.presentation import BureauFrame
from org.egedede.bureau import Configuration as conf

class BureauApp(wx.App):
    def OnInit(self):
        configuration = self.initConfiguration()
        
        print "hello 1 "
        facade = FacadeMetier.FacadeMetier()
        bureau = facade.loadLastLaunched()
        frame = BureauFrame.BureauFrame(None, bureau, facade)
        self.SetTopWindow(frame)
        frame.Show(True)
        return True

    def OnPreInit(self):
        self.RedirectStdio("./log.txt");
        pass
    def initConfiguration(self):
        configuration = conf.Configuration.createInstance('general',os.getcwd()+'\\conf\\desktop.properties')
        configuration.properties['app_directory'] = sys.argv[0]
        return configuration
def main():
    app = BureauApp()
    app.MainLoop()

if __name__ == '__main__':
    main()
