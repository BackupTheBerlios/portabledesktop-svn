import wx,os
from org.egedede.bureau.presentation import EditElementPanel  as elementPanel
from org.egedede.bureau import Configuration
from org.egedede.bureau.model import Element

class DesktopMenu(wx.Menu):

    def __init__(self, parent, desktop, element, facade,position):
        self.desktop = desktop
        self.facade = facade
        self.element = element
        self.parent = parent
        self.position = position
        wx.Menu.__init__(self)
        self.buildMenu()
    
    def buildMenu(self):
        if self.element:
        # add some other items
            self.Append(1, "Supprimer "+self.element.nom)
            self.Append(2, "Modifier "+self.element.nom)
            self.Append(3, "Executer "+self.element.nom)
            self.Bind(wx.EVT_MENU, self.OnDelete, id=1)
            self.Bind(wx.EVT_MENU, self.OnModify, id=2)
            self.Bind(wx.EVT_MENU, self.OnExecute, id=3)
        else :
            self.Append(4, "Ajouter")
            self.Append(5, "Charger")
            self.Append(6, "Sauver")
            self.Append(7, "Propriete")
            self.Bind(wx.EVT_MENU, self.OnAdd, id=4)
            self.Bind(wx.EVT_MENU, self.OnLoad, id=5)
            self.Bind(wx.EVT_MENU, self.OnSave, id=6)
            self.Bind(wx.EVT_MENU, self.OnConfigure, id=7)

    def OnDelete(self, event):
        if self.element:
            self.desktop.elements.remove(self.element)
        pass
        
    def OnModify(self, event):
        confPath = self.facade.computePath(Configuration.Configuration.getInstance('general').getProperty('element.description'))
        panel = elementPanel.EditElementPanel (parent = self.parent,conf=confPath, element = self.element,facade = self.facade)
        panel.SetPosition(self.position)
        result = panel.ShowModal()
        if result== wx.ID_OK:
            panel.OnAddModify()
        pass
        
    def OnExecute(self, event):
        self.facade.execute(self.element)
        pass
        
    def OnAdd(self, event):
        element = Element.Element()
        confPath = self.facade.computePath(Configuration.Configuration.getInstance('general').getProperty('element.description'))
        panel = elementPanel.EditElementPanel (parent = self.parent,conf=confPath, element = element,facade = self.facade)
        panel.SetPosition(self.position)
        result = panel.ShowModal()
        if result== wx.ID_OK:
            panel.OnAddModify()
            self.desktop.elements.append(panel.element)
        pass
        
    def OnLoad(self, event):
        dlg = wx.FileDialog(
            self.parent, message="Choose a file",
            defaultDir=os.getcwd(), 
            defaultFile="",
            style=wx.OPEN
            )
        # Show the dialog and retrieve the user response. If it is the OK response, 
        # process the data.
        if dlg.ShowModal() == wx.ID_OK:
            # This returns a Python list of files that were selected.
            paths = dlg.GetPaths()
            for path in paths:
                self.panel.bureau = self.facade.load(path)
            self.parent.Refresh()
        dlg.Destroy()       
        pass
        
    def OnSave(self, event):
        self.facade.save('blabla',self.desktop)
        pass
        
    def OnConfigure(self, event):
        pass
        
  