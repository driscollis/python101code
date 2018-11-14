from lxml import etree
from StringIO import StringIO

def parseXML(xmlFile):
    """
    Parse the xml
    """
    f = open(xmlFile)
    xml = f.read()
    f.close()
    
    tree = etree.parse(StringIO(xml))
    context = etree.iterparse(StringIO(xml))
    for action, elem in context:
        if not elem.text:
            text = "None"
        else:
            text = elem.text
        print(elem.tag + " => " + text)
    
if __name__ == "__main__":
    parseXML("example.xml")