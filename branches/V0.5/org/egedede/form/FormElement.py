import wx
import os
class FormElement(wx.Panel):
    def __init__(self,parent,confElement, value, idElement=-1, nameElement=None):
        label = confElement['label']
        if not nameElement:
            nameElement = label
        wx.Panel.__init__(self,parent,id=idElement,name=nameElement)
        self.label = label
        self.value = value
        sizer = wx.BoxSizer(wx.HORIZONTAL)
        text = wx.StaticText(self,label=self.label)
        sizer.Add(text)
        self.control = wx.TextCtrl(self,value=self.value,name=self.label,size=wx.Size(250,20),style=3)
        sizer.Add(self.control)
        if confElement['type']== 'file':
            button = wx.BitmapButton(self, wx.ID_OPEN, wx.Bitmap('resources\\OPEN.ICO'))
            self.Bind(wx.EVT_BUTTON, self.OnButton, button)
            sizer.Add(button)
        self.SetSizer(sizer)
    def getValue(self):
        return self.control.GetValue()

    def OnButton(self, evt):
        # Create the dialog. In this case the current directory is forced as the starting
        # directory for the dialog, and no default file name is forced. This can easilly
        # be changed in your program. This is an 'open' dialog, and allows multitple
        # file selections as well.
        #
        # Finally, if the directory is changed in the process of getting files, this
        # dialog is set up to change the current working directory to the path chosen.
        dlg = wx.FileDialog(
            self, message="Choose a file",
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
                self.control.SetValue(path)
        dlg.Destroy()