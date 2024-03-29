# main file of the project


import xml.etree.ElementTree as et

from create_ground import create_ground
from create_walls import create_walls
from utils import get_custom_xml_declaration


def create_arena(file_name,
                 nest_size_x, nest_size_y,
                 cache_size_y,
                 slope_size_y, slope_angle,
                 source_size_y):
    create_ground(nest_size_x, nest_size_y, cache_size_y, slope_size_y, slope_angle, source_size_y)

    create_walls(nest_size_x, nest_size_y, cache_size_y, slope_size_y, slope_angle, source_size_y)

    sdf = et.Element('sdf', version='1.9')

    world = et.SubElement(sdf, 'world', name='arena')

    scene = et.SubElement(world, 'scene')

    ambient = et.SubElement(scene, 'ambient')
    ambient.text = '1 1 1 1'

    grid = et.SubElement(scene, 'grid')
    grid.text = '0'

    # gazebo
    gazebo_contact = et.SubElement(world, 'gazebo')
    plugin_gazebo_contact = et.SubElement(gazebo_contact, 'plugin',
                                          file_name='libignition-gazebo-contact-system.so',
                                          name='ignition::gazebo::systems::Contact')
    gazebo_sensors = et.SubElement(world, 'gazebo')
    plugin_gazebo_sensors = et.SubElement(gazebo_sensors, 'plugin',
                                          file_name='libignition-gazebo-sensors-system.so',
                                          name='ignition::gazebo::systems::Sensors')
    render_engine_plugin_gazebo_sensors = et.SubElement(plugin_gazebo_sensors, 'render_engine')
    render_engine_plugin_gazebo_sensors.text = 'ogre'

    # load ground.sdf file
    include_ground = et.SubElement(world, 'include')
    uri_ground = et.SubElement(include_ground, 'uri')
    uri_ground.text = 'ground.sdf'

    # load walls.sdf file
    include_walls = et.SubElement(world, 'include')
    uri_walls = et.SubElement(include_walls, 'uri')
    uri_walls.text = 'walls.sdf'

    # load objects.sdf file
    include_objects = et.SubElement(world, 'include')
    uri_objects = et.SubElement(include_objects, 'uri')
    uri_objects.text = 'objects.sdf'

    # output file with customized xml declaration for SDF files
    get_custom_xml_declaration(sdf, f'{file_name}.sdf')


if __name__ == '__main__':
    arena_name = input('Insert arena name: ')

    nest_size_x = float(input('Insert nest area size x: '))
    nest_size_y = float(input('Insert nest area size y: '))
    cache_size_y = float(input('Insert cache size y: '))
    slope_size_y = float(input('Insert slope size y: '))
    slope_angle = float(input('Insert slope angle: '))
    source_size_y = float(input('Insert source size y: '))

    create_arena(arena_name,
                 nest_size_x, nest_size_y,
                 cache_size_y,
                 slope_size_y, slope_angle,
                 source_size_y)

    print('SDF arena successfully created')
