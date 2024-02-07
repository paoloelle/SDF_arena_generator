import xml.etree.ElementTree as et
import xml.dom.minidom


def get_custom_xml_declaration(xml_root, file_name):
    tree = et.tostring(xml_root)
    tree = xml.dom.minidom.parseString(tree).toprettyxml()
    with open(file_name, 'w') as file:
        file.write(tree)

