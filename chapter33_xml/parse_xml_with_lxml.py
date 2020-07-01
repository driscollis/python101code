# parse_xml_with_lxml.py

from lxml import etree, objectify

def parse_xml(xml_file):
    with open(xml_file) as f:
        xml = f.read()

    root = objectify.fromstring(xml)

    # Get an element
    to = root.note.to
    print(f'The {to=}')

    # print out all the note element's tags and text values
    for note in root.getchildren():
        for note_element in note.getchildren():
            print(f'{note_element.tag=}, {note_element.text=}')
        print()

    # modify a text value
    print(f'Original: {root.note.to=}')
    root.note.to = 'Guido'
    print(f'Modified: {root.note.to=}')

    # add a new element
    root.note.new_element = "I'm new!"

    # cleanup the XML before writing to disk
    objectify.deannotate(root)
    etree.cleanup_namespaces(root)
    obj_xml = etree.tostring(root, pretty_print=True)

    # save your xml
    with open("lxml_output.xml", "wb") as f:
        f.write(obj_xml)

if __name__ == '__main__':
    parse_xml('note.xml')