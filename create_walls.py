import xml.etree.ElementTree as et
from math import cos, pi

from utils import get_custom_xml_declaration


def create_walls(NEST_SIZE_X, NEST_SIZE_Y, CACHE_SIZE_Y, SLOPE_SIZE_Y, SLOPE_ANGLE, SOURCE_SIZE_Y):
    WALL_THICKNESS = 0.1
    WALL_HEIGHT = 1
    WALL_COLOR = '1 1 1 0.3'

    GROUND_THICKNESS = 0.1

    # nest wall
    NEST_WALL_X = 0
    NEST_WALL_Y = -NEST_SIZE_Y / 2 - WALL_THICKNESS / 2
    NEST_WALL_Z = WALL_HEIGHT / 2 - GROUND_THICKNESS

    NEST_WALL_SIZE_X = NEST_SIZE_X
    NEST_WALL_SIZE_Y = WALL_THICKNESS
    NEST_WALL_SIZE_Z = WALL_HEIGHT

    # source wall (pose relative to nest wall)
    SOURCE_WALL_X = NEST_WALL_Y
    SOURCE_WALL_Y = WALL_THICKNESS / 2 + NEST_SIZE_Y + CACHE_SIZE_Y + SLOPE_SIZE_Y * cos(
        SLOPE_ANGLE) + SOURCE_SIZE_Y + WALL_THICKNESS / 2
    SOURCE_WALL_Z = NEST_WALL_Z

    SOURCE_WALL_SIZE_X = NEST_WALL_SIZE_X
    SOURCE_WALL_SIZE_Y = NEST_WALL_SIZE_Y
    SOURCE_WALL_SIZE_Z = NEST_WALL_SIZE_Z

    # edge wall1
    EDGE_WALL1_X = NEST_SIZE_X / 2 + WALL_THICKNESS / 2
    EDGE_WALL1_Y = (NEST_SIZE_Y + CACHE_SIZE_Y + SLOPE_SIZE_Y * cos(SLOPE_ANGLE) + SOURCE_SIZE_Y) / 2
    EDGE_WALL1_Z = 0
    EDGE_WALL_YAW = pi / 2

    EDGE_WALL1_SIZE_X = NEST_SIZE_Y + CACHE_SIZE_Y + SLOPE_SIZE_Y * cos(SLOPE_ANGLE) + SOURCE_SIZE_Y
    EDGE_WALL1_SIZE_Y = WALL_THICKNESS
    EDGE_WALL1_SIZE_Z = WALL_HEIGHT

    # edge wall 2 (pose relative to edge wall 1)
    EDGE_WALL2_X = 0
    EDGE_WALL2_Y = WALL_THICKNESS / 2 + NEST_SIZE_X + WALL_THICKNESS / 2
    EDGE_WALL2_Z = 0

    #######################
    # start defining code #
    #######################

    sdf = et.Element('sdf', version='1.9')

    model = et.SubElement(sdf, 'model', name='walls')

    static = et.SubElement(model, 'static')
    static.text = 'true'

    # WALL NEST

    link_wall_nest = et.SubElement(model, 'link', name='link_wall_nest')
    pose_wall_nest = et.SubElement(link_wall_nest, 'pose')
    pose_wall_nest.text = f'{NEST_WALL_X} {NEST_WALL_Y} {NEST_WALL_Z} 0 0 0'

    # visual nest wall
    visual_nest_wall = et.SubElement(link_wall_nest, 'visual', name='visual_nest_wall')
    geometry_visual_nest_wall = et.SubElement(visual_nest_wall, 'geometry')
    box_visual_nest_wall = et.SubElement(geometry_visual_nest_wall, 'box')
    size_box_visual_nest_wall = et.SubElement(box_visual_nest_wall, 'size')
    size_box_visual_nest_wall.text = f'{NEST_WALL_SIZE_X} {NEST_WALL_SIZE_Y} {NEST_WALL_SIZE_Z}'

    material_visual_nest_wall = et.SubElement(visual_nest_wall, 'material')
    diffuse_visual_nest_wall = et.SubElement(material_visual_nest_wall, 'diffuse')
    diffuse_visual_nest_wall.text = WALL_COLOR

    # collision nest wall
    collision_nest_wall = et.SubElement(link_wall_nest, 'collision', name='collision_nest_wall')
    geometry_collision_nest_wall = et.SubElement(collision_nest_wall, 'geometry')
    box_collision_nest_wall = et.SubElement(geometry_collision_nest_wall, 'box')
    size_box_collision_nest_wall = et.SubElement(box_collision_nest_wall, 'size')
    size_box_collision_nest_wall.tetx = f'{NEST_WALL_SIZE_X} {NEST_WALL_SIZE_Y} {NEST_WALL_SIZE_Z}'

    # SOURCE WALL

    link_wall_source = et.SubElement(model, 'link', name='link_wall_source')
    pose_wall_source = et.SubElement(link_wall_source, 'pose',
                                     relative_to='link_wall_source')
    pose_wall_source.text = f'{SOURCE_WALL_X} {SOURCE_WALL_Y} {SOURCE_WALL_Z} 0 0 0'

    # visual source wall
    visual_source_wall = et.SubElement(link_wall_source, 'visual', name='visual_source_wall')
    geometry_visual_source_wall = et.SubElement(visual_source_wall, 'geometry')
    box_visual_source_wall = et.SubElement(geometry_visual_source_wall, 'box')
    size_box_visual_source_wall = et.SubElement(box_visual_source_wall, 'size')
    size_box_visual_source_wall.text = f'{SOURCE_WALL_SIZE_X} {SOURCE_WALL_SIZE_Y} {SOURCE_WALL_SIZE_Z}'

    material_visual_nest_wall = et.SubElement(visual_source_wall, 'material')
    diffuse_visual_nest_wall = et.SubElement(material_visual_nest_wall, 'diffuse')
    diffuse_visual_nest_wall.text = WALL_COLOR

    # collision nest wall
    collision_source_wall = et.SubElement(link_wall_source, 'collision', name='collision_source_wall')
    geometry_collision_source_wall = et.SubElement(collision_source_wall, 'geometry')
    box_collision_source_wall = et.SubElement(geometry_collision_source_wall, 'box')
    size_box_collision_source_wall = et.SubElement(box_collision_source_wall, 'size')
    size_box_collision_source_wall.tetx = f'{SOURCE_WALL_SIZE_X} {SOURCE_WALL_SIZE_Y} {SOURCE_WALL_SIZE_Z}'

    # edge wall 1

    link_edge_wall1 = et.SubElement(model, 'link', name='link_edge_wall1')
    pose_edge_wall1 = et.SubElement(link_edge_wall1, 'pose')
    pose_edge_wall1.text = f'{EDGE_WALL1_X} {EDGE_WALL1_Y} {EDGE_WALL1_Z} 0 0 {EDGE_WALL_YAW}'

    # visual edge wall 1
    visual_edge_wall1 = et.SubElement(link_edge_wall1, 'visual', name='visual_edge_wall1')
    geometry_visual_edge_wall1 = et.SubElement(visual_edge_wall1, 'geometry')
    box_visual_edge_wall1 = et.SubElement(geometry_visual_edge_wall1, 'box')
    size_box_visual_edge_wall1 = et.SubElement(box_visual_edge_wall1, 'size')
    size_box_visual_edge_wall1.text = f'{EDGE_WALL1_SIZE_X} {EDGE_WALL1_SIZE_Y} {EDGE_WALL1_SIZE_Z}'

    material_visual_edge_wall1 = et.SubElement(visual_edge_wall1, 'material')
    diffuse_visual_edge_wall1 = et.SubElement(material_visual_edge_wall1, 'diffuse')
    diffuse_visual_edge_wall1.text = WALL_COLOR

    # collision edge wall 1
    collision_edge_wall1 = et.SubElement(link_edge_wall1, 'collision', name='collision_edge_wall1')
    geometry_collision_edge_wall1 = et.SubElement(collision_edge_wall1, 'geometry')
    box_collision_edge_wall1 = et.SubElement(geometry_collision_edge_wall1, 'box')
    size_box_collision_edge_wall1 = et.SubElement(box_collision_edge_wall1, 'size')
    size_box_collision_edge_wall1.text = f'{EDGE_WALL1_SIZE_X} {EDGE_WALL1_SIZE_Y} {EDGE_WALL1_SIZE_Z}'

    # edge wall 2

    link_edge_wall2 = et.SubElement(model, 'link', name='link_edge_wall2')
    pose_edge_wall1 = et.SubElement(link_edge_wall1, 'pose', relative_to=link_edge_wall1)
    pose_edge_wall1.text = f'{EDGE_WALL2_X} {EDGE_WALL2_Y} {EDGE_WALL2_Z} 0 0 0'

    # visual edge wall 2
    visual_edge_wall2 = et.SubElement(link_edge_wall2, 'visual', name='visual_edge_wall2')
    geometry_visual_edge_wall2 = et.SubElement(visual_edge_wall2, 'geometry')
    box_visual_edge_wall2 = et.SubElement(geometry_visual_edge_wall2, 'box')
    size_box_visual_edge_wall2 = et.SubElement(box_visual_edge_wall2, 'size')
    size_box_visual_edge_wall2.text = f'{EDGE_WALL1_SIZE_X} {EDGE_WALL1_SIZE_Y} {EDGE_WALL1_SIZE_Z}'

    material_visual_nest_wall = et.SubElement(visual_edge_wall2, 'material')
    diffuse_visual_nest_wall = et.SubElement(material_visual_nest_wall, 'diffuse')
    diffuse_visual_nest_wall.text = WALL_COLOR

    # collision edge wall 2
    collision_edge_wall2 = et.SubElement(link_edge_wall2, 'collision', name='collision_edge_wall2')
    geometry_collision_edge_wall2 = et.SubElement(collision_edge_wall2, 'geometry')
    box_collision_edge_wall2 = et.SubElement(geometry_collision_edge_wall2, 'box')
    size_box_collision_edge_wall2 = et.SubElement(box_collision_edge_wall2, 'size')
    size_box_collision_edge_wall2.text = f'{EDGE_WALL1_SIZE_X} {EDGE_WALL1_SIZE_Y} {EDGE_WALL1_SIZE_Z}'
