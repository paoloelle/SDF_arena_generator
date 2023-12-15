import xml.etree.ElementTree as et

from utils import get_custom_xml_declaration


def create_ground(NEST_SIZE_X, NEST_SIZE_Y, CACHE_SIZE_X, CACHE_SIZE_Y):

    # nest postion
    NEST_POSE_X = 0
    NEST_POSE_Y = 1
    NEST_POSE_Z = 0

    NEST_SIZE_Z = 0.1

    # cache position
    CACHE_POSE_X = NEST_POSE_X
    CACHE_POSE_Y = NEST_SIZE_Y/2 + CACHE_SIZE_Y/2
    CACHE_POSE_Z = NEST_POSE_Z

    sdf = et.Element('sdf', version='1.9')

    model = et.SubElement(sdf, 'model', name='ground')

    static = et.SubElement(model, 'static')
    static.text = 'true'

    # lower area is splitted in cache area and nest area
    link_lower_area = et.SubElement(model, 'link,', name='link_lower_area')

    pose_lower_area = et.SubElement(link_lower_area)
    pose_lower_area.text = '0 0 0 0 0 0'

    # visual nest area
    visual_nest = et.SubElement(link_lower_area, 'visual', name='nest_area')

    pose_nest = et.SubElement(visual_nest, 'pose')
    pose_nest.text = f'{NEST_POSE_X} {NEST_POSE_Y} {NEST_POSE_Z} 0 0 0'

    geometry_nest = et.SubElement(visual_nest, 'geometry')
    box_nest = et.SubElement(geometry_nest, 'box')
    size_box_nest = et.SubElement(box_nest, 'size')
    size_box_nest.text = f'{NEST_SIZE_X} {NEST_SIZE_Y} {NEST_SIZE_Z}'

    material_nest = et.SubElement(visual_nest, 'material')
    diffuse_nest = et.SubElement(material_nest, 'diffuse')
    diffuse_nest.text = f'{0} '

    # visual cache area
    visual_cache = et.SubElement(link_lower_area, 'visual', name='cache_area')

    pose_cache = et.SubElement(visual_nest, 'pose')
    pose_cache.text = f'{CACHE_POSE_X} {CACHE_POSE_Y} {CACHE_POSE_Z}'

    geometry_cache = et.SubElement(visual_cache, 'geometry')
    box_cache = et.SubElement(geometry_cache, 'box')
    size_box_nest = et.SubElement(box_nest, 'size')
    size_box_nest.text = f'{NEST_SIZE_X} {NEST_SIZE_Y} {GROUND_Z}'

    material_nest = et.SubElement(visual_nest, 'material')
    diffuse_nest = et.SubElement(material_nest, 'diffuse')
    diffuse_nest.text = ' 0 1 0 1'







