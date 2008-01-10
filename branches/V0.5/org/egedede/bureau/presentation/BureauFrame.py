import wx
from org.egedede.bureau.presentation import BureauPanel as panel
from org.egedede.bureau import Configuration
class BureauFrame (wx.Frame):
    def __init__(self,parent=None,bureau=None, facade=None):
        self.bureau = bureau
        self.facade = facade
        wx.Frame.__init__(self, parent, -1, "Bureau", wx.DefaultPosition, (400,300))
        self.panel =  panel.BureauPanel(self, self.bureau,self.facade)
#        self.Bind(wx.EVT_PAINT, self.OnPaint)
        self.Bind(wx.EVT_SIZE,self.OnResize)
        self.Bind(wx.EVT_CLOSE, self.EvtClose)
 
    def EvtClose(self, evt):
        dlg = wx.MessageDialog(self, 'Voulez-vous fermer cette fenetre?',
                               'Demande de confirmation',
                               wx.YES_NO | wx.ICON_EXCLAMATION
                               )
        if dlg.ShowModal() == wx.ID_YES:
            dlg.Destroy()
            evt.Skip()
        else:
            dlg.Destroy()        
    def OnResize(self,evt):
        self.panel.SetSize(self.GetClientSize())
        self.Refresh()

    def OnPaint(self,evt):
        print "BureauFrame.OnPaint"
        dc = wx.PaintDC(self)
        self.PrepareDC(dc)
        image = self.background.Scale(self.GetClientSize()[0],self.GetClientSize()[1])
        bitmap = wx.BitmapFromImage(image)
        dc.DrawBitmap(bitmap, 0,0)
        
