# edit_xml.py


import xml.etree.cElementTree as ET

def edit_xml(xml_file, output_file, from_person):
    tree = ET.ElementTree(file=xml_file)
    root = tree.getroot()

    for from_element in tree.iter(tag='from'):
        from_element.text = from_person

    tree = ET.ElementTree(root)
    with open(output_file, "wb") as f:
        tree.write(f)

if __name__ == '__main__':
    edit_xml('note.xml', 'output.xml', 'Guido')