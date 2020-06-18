# parse_xml.py

from xml.etree.ElementTree import ElementTree

def parse_xml(xml_file):
    tree = ElementTree(file=xml_file)
    root_element = tree.getroot()
    print(f"The root element's tag is '{root_element.tag}'")

    for child_element in root_element:
        print(f'{child_element.tag=}, {child_element.text=}')
        if child_element.tag == 'note':
            for note_element in child_element:
                print(f'{note_element.tag=}, {note_element.text=}')


if __name__ == '__main__':
    parse_xml('note.xml')

