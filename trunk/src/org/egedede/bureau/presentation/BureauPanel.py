import wx
import os

class BureauPanel (wx.Panel):
		def __init__(self,parent=None,bureau=None):
				self.bureau = bureau
				wx.Panel.__init__(self, parent, -1, size = parent.GetClientSize())
				self.startPosition = wx.Point(0,0)
				self.selectedElement=None
#        self.Bind(wx.EVT_ERASE_BACKGROUND, self.OnEraseBackground)
				self.Bind(wx.EVT_PAINT, self.OnPaint)
				self.Bind(wx.EVT_LEFT_DOWN, self.OnLeftDown)
				self.Bind(wx.EVT_LEFT_UP, self.OnLeftUp)
				self.Bind(wx.EVT_MOTION, self.OnMotion)
				self.Bind(wx.EVT_LEAVE_WINDOW, self.OnLeaveWindow)
				self.Bind(wx.EVT_LEFT_DCLICK, self.OnLeftDclick)
		def OnLeaveWindow(self, evt):
				pass

		def OnLeftDclick(self, evt):
				shape = self.findElement(evt.GetPosition())
				if shape:
						print shape.commande
						os.system(shape.commande)

		# Go through our list of shapes and draw them in whatever place they are.
		def drawElements(self, dc):
				for element in self.bureau.getElements():
						image = wx.Image(element.getIcone())
						image = image.Scale(40,40)
						bitmap = wx.BitmapFromImage(image)
						print element.nom,'_',element.isSelected(),'_',element.selected
						if element.isSelected():
								dc.DrawRectangle(element.x-5,element.y-5,50,50+10)
						dc.DrawBitmap(bitmap, element.getX(), element.getY())
						dc.DrawText(element.getNom(), element.getX(), element.getY()+40)
				pass

						#blabla
		def findElement(self, point):
				for element in self.bureau.getElements():
						rect = wx.Rect(element.getX()-5, element.getY()-5, 50,60)
						if rect.InsideXY(point.x,point.y) :
								return element
				return None

		# Fired whenever a paint event occurs
		def OnPaint(self, evt):
				dc = wx.PaintDC(self)
				self.PrepareDC(dc)
				self.drawElements(dc)

    # Left mouse button is down.
		def OnLeftDown(self, evt):
				# Did the mouse go down on one of our shapes?
				shape = self.findElement(evt.GetPosition())
				if shape:
						print shape.nom
						shape.selected=True
				# If a shape was 'hit', then set that as the shape we're going to
				# drag around. Get our start position. Dragging has not yet started.
				# That will happen once the mouse moves, OR the mouse is released.
						self.selectedElement = shape
						self.startPosition = evt.GetPosition()
						self.Refresh()
				# Left mouse button up.
		def OnLeftUp(self, evt):
				pass
#				if self.selectedElement:
#						self.selectedElement.selected=False
#						self.selectedElement = None
#						self.Refresh()


				# reposition and draw the shape

				# Note by jmg 11/28/03 
				# Here's the original:
				#
				# self.dragShape.pos = self.dragShape.pos + evt.GetPosition() - self.dragStartPos
				#
				# So if there are any problems associated with this, use that as
				# a starting place in your investigation. I've tried to simulate the
				# wx.Point __add__ method here -- it won't work for tuples as we
				# have now from the various methods
				#
				# There must be a better way to do this :-)
				#

		# The mouse is moving
		def OnMotion(self, evt):
				# Ignore mouse movement if we're not dragging.
				if not self.selectedElement or not evt.Dragging() or not evt.LeftIsDown():
						return
				print "OK, on y est"
				# if we have a shape, but haven't started dragging yet
				diff = self.startPosition-evt.GetPosition()
				self.startPosition = evt.GetPosition()
				print diff
				self.selectedElement.x = self.selectedElement.x-diff[0]				
				self.selectedElement.y = self.selectedElement.y-diff[1]
				self.Refresh()