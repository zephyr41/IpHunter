import xml.etree.ElementTree as ET
tree = ET.parse('output.xml')
root = tree.getroot()
for child in root :
      print(child.tag)

