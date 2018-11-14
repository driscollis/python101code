from lxml import etree

def parseBookXML(xmlFile):
    """"""
    context = etree.iterparse(xmlFile)
    book_dict = {}
    books = []
    for action, elem in context:
        if not elem.text:
            text = "None"
        else:
            text = elem.text
        print(elem.tag + " => " + text)
        book_dict[elem.tag] = text
        if elem.tag == "book":
            books.append(book_dict)
            book_dict = {}
    return books

if __name__ == "__main__":
    parseBookXML("example3.xml")