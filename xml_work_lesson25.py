import xml.etree.ElementTree as ET


def parseXML(xml_str):
    root = ET.fromstring(xml_str)

    for child in root:
        print(child.tag, child.attrib['id'])
    # колличество книг
    print(len(root))
    # price sort books
    els = root.findall("book")
    new_els = sorted(els, key=lambda el: float(el.find('price').text))
    print('sorted by price')
    for i in new_els:
        print(i.attrib['id'], i.find('price').text)



# if __name__ == "__main__":
#     xml_string = """<?xml version="1.0" encoding="UTF-8"?>
#     <books>
#         <book name="Harry Potter and the Philosopher’s Stone">
#            <author>J. K. Rowling</author>
#            <year>1997</year>
#         </book>
#         <book name="Harry Potter and the chamber of secrets">
#            <author>J. K. Rowling</author>
#            <year>1987</year>
#         </book>
#     </books>
#     """
#
#     parseXML(xml_string)


if __name__ == "__main__":
    with open("library.xml", "r") as f:
        xml_string = f.read()
    parseXML(xml_string)
