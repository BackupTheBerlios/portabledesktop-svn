import wx
from org.egedede.bureau.presentation import BureauPanel as panel
class BureauFrame (wx.Frame):
    def __init__(self,parent=None,bureau=None):
        self.bureau = bureau
        wx.Frame.__init__(self, parent, -1, "Bureau", wx.DefaultPosition, (400,300))
        panel.BureauPanel(self, self.bureau)