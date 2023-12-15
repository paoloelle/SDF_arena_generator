# main file of the project

import xml.etree.ElementTree as ET
import xml.dom.minidom

from utils import modify_xml_declaration


def create_arena():
    sdf = ET.Element('sdf')

    world = ET.SubElement(sdf, 'world', name='arena')

    scene = ET.SubElement(world, 'scene')

    ambient = ET.SubElement(scene, 'ambient')
    ambient.text = '1 1 1 1'

    grid = ET.SubElement(scene, 'grid')
    grid.text = 0

    # load ground.sdf file
    include_ground = ET.SubElement(scene, 'include')
    uri_ground = ET.SubElement(include_ground, 'uri')
    uri_ground.text = 'ground.sdf'

    # load walls.sdf file
    include_walls = ET.SubElement(scene, 'include')
    uri_walls = ET.SubElement(include_walls, 'uri')
    uri_walls.text = 'walls.sdf'

    # output file with customized xml declaration for SDF files
    modify_xml_declaration(sdf, 'arena.sdf')


if __name__ == '__main__':
    create_arena()
    print('SDF arena successfully created')
