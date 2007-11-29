from xml.dom import minidom
class FormConfiguration(object):
    def __init__(self, fileName=None):
        self.elements = []
        if fileName:
          dom = minidom.parse(fileName)
          elements = dom.getElementsByTagName('element')
          for element in elements:
              line = {}
              attribut=element.getAttribute('attribut')
              label=element.getAttribute('label')
              position=int(element.getAttribute('position'))
              type=element.getAttribute('type')
              icone=element.getAttribute('icone')
              line['attribut'] = attribut
              line['label'] = label
              line['position'] = position
              line['type'] = type
              line['icone'] = icone
              self.elements.append(line)
          dom.unlink()
        pass