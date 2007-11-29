import wx

from org.egedede.form import FormElement as formElement
from org.egedede.form import FormConfiguration as formConf

class Form (wx.Dialog):
    def __init__(self,parent=None,object=None, conf=None):
        self.object = object
        self.conf = formConf.FormConfiguration(conf)
        wx.Dialog.__init__(self,parent,-1,"Edition des elements")
        #self.SetSize(wx.Size(200,200))
        self.initGraphics()
        pass
        
    def initGraphics(self):
        sizer = wx.GridBagSizer()
        i = 1
        self.elements = {}
        for confElement in self.conf.elements:
            attribut=confElement['attribut']
            value = ''
            if self.object:
                value = self.object.__dict__[attribut]
            element = formElement.FormElement(self,confElement,value)
            self.elements[attribut]=element
            sizer.Add(element, (i,0,),(1,1), wx.EXPAND)
            i = i+1
        tmp = self.createButtonsPanel()
        sizer.Add(tmp, (i,0),(1,1), wx.EXPAND)
        self.SetSizer(sizer)
        pass

    def createButtonsPanel(self):
        buttonSizer = wx.BoxSizer(wx.HORIZONTAL)
        panel = wx.Panel(self)
        button = wx.Button(panel,id = wx.ID_OK)
        print "Form.py.createButtonsPanel > ids button = ",wx.ID_OK,wx.ID_CANCEL,button.GetId()
#        self.Bind(wx.EVT_BUTTON,self.OnAddModify,button)
        buttonSizer.Add(button, 0, wx.GROW|wx.ALIGN_LEFT|wx.ALL, 5)
        button = wx.Button(panel,id = wx.ID_CANCEL)
        buttonSizer.Add(button, 0, wx.GROW|wx.ALIGN_LEFT|wx.ALL, 5)
        panel.SetSizer(buttonSizer)
        return panel
    
    
    def OnAddModify(self):
        print "Form.py.OnAddModify"
        for attribut in self.elements:
            print "self.",object.__class__.__name__,".__dict__[",attribut,"]=",self.elements[attribut].getValue()
            self.object.__dict__[attribut]=self.elements[attribut].getValue()
        
