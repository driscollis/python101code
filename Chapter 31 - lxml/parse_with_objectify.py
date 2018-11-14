from lxml import etree, objectify

def parseXML(xmlFile):
    """Parse the XML file"""
    with open(xmlFile) as f:
        xml = f.read()
    
    root = objectify.fromstring(xml)

    # returns attributes in element node as dict
    attrib = root.attrib

    # how to extract element data
    begin = root.appointment.begin
    uid = root.appointment.uid
    
    # loop over elements and print their tags and text
    for e in root.appointment.iterchildren():
        print("%s => %s" % (e.tag, e.text))
    
    # how to change an element's text
    root.appointment.begin = "something else"
    print(root.appointment.begin)
    
    # how to add a new element
    root.appointment.new_element = "new data"
    
    # remove the py:pytype stuff
    objectify.deannotate(root)
    etree.cleanup_namespaces(root)
    obj_xml = etree.tostring(root, pretty_print=True)
    print(obj_xml)
    
    # save your xml
    with open("new.xml", "w") as f:
        f.write(obj_xml)

if __name__ == "__main__":
    f = r'path\to\sample.xml'
    parseXML(f)