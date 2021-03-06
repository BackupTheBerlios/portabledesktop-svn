import wx
import os
from org.egedede.bureau.presentation import DesktopMenu as defmenu
from org.egedede.bureau.presentation import ElementPanel as elementPanel
from org.egedede.bureau import Configuration
class BureauPanel (wx.Panel):
    def __init__(self,parent=None,bureau=None, facade=None):
        self.parent = parent
        self.bureau = bureau
        self.elements = []
        wx.Panel.__init__(self, parent = parent, id=-1, size = parent.GetClientSize())
        for element in self.bureau.elements:
            pass
#            self.elements.append(elementPanel.ElementPanel(parent=self,element=element,facade=facade))
        self.facade = facade
        self.startPosition = wx.Point(0,0)
        self.selectedElement=None
        self.font = wx.Font(10,wx.FONTFAMILY_MODERN,wx.FONTSTYLE_NORMAL,wx.FONTWEIGHT_NORMAL)
        self.background = wx.Image(self.facade.computePath(Configuration.Configuration.getInstance('general').getProperty('background')))
        image = self.background.Scale(self.GetClientSize()[0],self.GetClientSize()[1])
        self.bitmap = wx.BitmapFromImage(image)
        #        self.Bind(wx.EVT_ERASE_BACKGROUND, self.OnEraseBackground)
        self.Bind(wx.EVT_PAINT, self.OnPaint)
        self.Bind(wx.EVT_LEFT_DOWN, self.OnLeftDown)
        self.Bind(wx.EVT_LEFT_UP, self.OnLeftUp)
        self.Bind(wx.EVT_MOTION, self.OnMotion)
        self.Bind(wx.EVT_LEAVE_WINDOW, self.OnLeaveWindow)
        self.Bind(wx.EVT_LEFT_DCLICK, self.OnLeftDclick)
        self.Bind(wx.EVT_CONTEXT_MENU, self.OnContextMenu)
        self.Bind(wx.EVT_SIZE,self.OnResize)
        
    def OnContextMenu(self, evt):
        point = evt.GetPosition()
        point = self.ScreenToClient(point)
        menu = defmenu.DesktopMenu(self,self.bureau,self.findElement(point),self.facade,evt.GetPosition())


        # Popup the menu.  If an item is selected then its handler
        # will be called before PopupMenu returns.
        self.PopupMenu(menu)
        menu.Destroy()
        self.Refresh();

    def OnResize(self,evt):
        image = self.background.Scale(self.GetClientSize()[0],self.GetClientSize()[1])
        self.bitmap = wx.BitmapFromImage(image)
        self.Refresh()
        
    def OnLeaveWindow(self, evt):
        pass

    def OnLeftDclick(self, evt):
        element = self.findElement(evt.GetPosition())
        if element:
            self.facade.execute(element)

    def drawElements(self, dc):
        dc.SetFont(self.font)
        for element in self.bureau.getElements():
            imagePath = element.getIcone()
            imagePath = self.facade.computePath(imagePath)
            image = wx.Image(imagePath)
            image = image.Scale(40,40)
            bitmap = wx.BitmapFromImage(image)
            textWidth = dc.GetFullTextExtent(element.getNom(),dc.GetFont())[0]
            textHeight = dc.GetFullTextExtent(element.getNom(),dc.GetFont())[1]
            if element.isSelected():
                if textWidth<50:
                    dc.DrawRectangle(element.x-5,element.y-5,50,50+10)
                else:
                    dc.DrawRectangle(element.x+15-textWidth/2,element.y-5,textWidth,50+textHeight)
            dc.DrawBitmap(bitmap, element.getX(), element.getY())
            dc.DrawText(element.getNom(), element.getX()+20-textWidth/2, element.getY()+40)
        pass

    def findElement(self, point):
        for element in self.bureau.getElements():
            rect = wx.Rect(element.getX()-5, element.getY()-5, 50,60)
            if rect.InsideXY(point.x,point.y) :
                return element
        return None

    # Fired whenever a paint event occurs
    def OnPaint(self, evt):
        dc = wx.PaintDC(self)
        dc.SetBackgroundMode(wx.TRANSPARENT)
        self.PrepareDC(dc)
        dc.DrawBitmap(self.bitmap, 0,0)
        self.drawElements(dc)

    # Left mouse button is down.
    def OnLeftDown(self, evt):
        # Did the mouse go down on one of our shapes?
        element = self.findElement(evt.GetPosition())
        if element:
            element.selected=True
            self.selectedElement = element
            self.startPosition = evt.GetPosition()
            self.Refresh()
        # Left mouse button up.
    def OnLeftUp(self, evt):
  				if self.selectedElement:
   						self.selectedElement = None

    # The mouse is moving
    def OnMotion(self, evt):
        if not self.selectedElement or not evt.Dragging() or not evt.LeftIsDown():
            return
        # if we have a shape, but haven't started dragging yet
        diff = self.startPosition-evt.GetPosition()
        self.startPosition = evt.GetPosition()
        self.selectedElement.x = self.selectedElement.x-diff[0]				
        self.selectedElement.y = self.selectedElement.y-diff[1]
        rect = wx.Rect(self.selectedElement.x-50,self.selectedElement.y-50,100,100)
        #self.Refresh(True,rect)
        self.Refresh()
