import xml.etree.ElementTree as ET
import xml.dom.minidom


def modify_xml_declaration(xml_root, file_name):
    tree = ET.tostring(xml_root)
    tree = xml.dom.minidom.parseString(tree).toprettyxml()
    with open(file_name, 'w') as file:
        file.write(tree)
