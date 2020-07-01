# create_xml.py

import xml.etree.ElementTree as ET


def create_xml(xml_file):
    root_element = ET.Element('note_taker')
    note_element = ET.Element('note')
    root_element.append(note_element)

    # add note sub-elements
    to_element = ET.SubElement(note_element, 'to')
    to_element.text = 'Mike'
    from_element = ET.SubElement(note_element, 'from')
    from_element.text = 'Nick'
    heading_element = ET.SubElement(note_element, 'heading')
    heading_element.text = 'Appointment'
    body_element = ET.SubElement(note_element, 'body')
    body_element.text = 'blah blah'

    tree = ET.ElementTree(root_element)
    with open(xml_file, "wb") as fh:
        tree.write(fh)

if __name__ == '__main__':
    create_xml('test_create.xml')