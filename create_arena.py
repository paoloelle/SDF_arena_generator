# main file of the project

import xml.etree.ElementTree as ET


def create_arena():
    sdf = ET.Element('sdf')

    world = ET.SubElement(sdf, 'world', name='arena')

    scene = ET.SubElement(world, 'scene')

    ambient = ET.SubElement(scene, 'ambient')
    ambient.text = '1 1 1 1'

    grid = ET.SubElement(scene, 'grid')
    grid.text = 0

    # load ground.sdf file
    include_ground = ET.SubElement(scene, 'include_ground')
    uri_ground = ET.SubElement(include_ground, 'uri_ground')
    uri_ground.text = 'ground.sdf'

    # load walls.sdf file
    include_walls = ET.SubElement(scene, 'include_walls')
    uri_walls = ET.SubElement(include_walls, 'uri_walls')
    uri_walls.text = 'walls.sdf'

    tree = ET.ElementTree(sdf)
    tree.write('arena.sdf')


if __name__ == '__main__':
    create_arena()
