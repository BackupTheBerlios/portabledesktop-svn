import wx


class ElementPanel (wx.Panel):
    def __init__(self,parent,element,facade):
        self.element=element
        self.facade = facade
        print 'Parent name : ',parent.__class__.__name__
        wx.Panel.__init__(self,parent, id=-1,pos=(element.x,element.y))
        self.initGraphics()
        self.Bind(wx.EVT_PAINT, self.OnPaint)
        
    def initGraphics(self):
            imagePath = self.element.getIcone()
            imagePath = self.facade.computePath(imagePath)
            image = wx.Image(imagePath)
            image = image.Scale(40,40)
            self.bitmap = wx.BitmapFromImage(image)
            text = wx.StaticText(self,-1,self.element.getNom())
            x = 20-text.GetSize()[0]/2
            y=40
            text.SetPosition(wx.Point(x,y))
        
    def OnPaint(self, evt):
        dc = wx.PaintDC(self)
        self.PrepareDC(dc)
        dc.DrawBitmap(self.bitmap, self.element.getX(), self.element.getY())
        
