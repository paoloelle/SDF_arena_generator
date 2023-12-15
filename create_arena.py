# main file of the project

import xml.etree.ElementTree as et

from utils import get_custom_xml_declaration


def create_arena():
    sdf = et.Element('sdf', version='1.9')

    world = et.SubElement(sdf, 'world', name='arena')

    scene = et.SubElement(world, 'scene')

    ambient = et.SubElement(scene, 'ambient')
    ambient.text = '1 1 1 1'

    grid = et.SubElement(scene, 'grid')
    grid.text = 0

    # load ground.sdf file
    include_ground = et.SubElement(scene, 'include')
    uri_ground = et.SubElement(include_ground, 'uri')
    uri_ground.text = 'ground.sdf'

    # load walls.sdf file
    include_walls = et.SubElement(scene, 'include')
    uri_walls = et.SubElement(include_walls, 'uri')
    uri_walls.text = 'walls.sdf'

    # output file with customized xml declaration for SDF files
    get_custom_xml_declaration(sdf, 'arena_automated.sdf')


if __name__ == '__main__':
    create_arena()
    print('SDF arena successfully created')
