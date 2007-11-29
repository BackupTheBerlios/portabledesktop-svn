import wx
from org.egedede.form import Form

class EditElementPanel (Form.Form):
    def __init__(self,parent=None,conf=None,element=None,facade=None):
        self.element=element
        if conf:
            if facade:
                conf = facade.computeFile(conf)
        Form.Form.__init__(self,parent,element,conf)
