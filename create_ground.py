import xml.etree.ElementTree as et

from utils import get_custom_xml_declaration


def create_ground(NEST_SIZE_X, NEST_SIZE_Y, CACHE_SIZE_Y, SLOPE_SIZE_Y, SLOPE_ANGLE):
    # nest position
    NEST_POSE_X = 0
    NEST_POSE_Y = 1
    NEST_POSE_Z = 0

    NEST_SIZE_Z = 0.1

    NEST_COLOR = '0 1 0 1'

    # cache position
    CACHE_POSE_X = NEST_POSE_X
    CACHE_POSE_Y = NEST_SIZE_Y / 2 + CACHE_SIZE_Y / 2
    CACHE_POSE_Z = NEST_POSE_Z

    # cache size
    CACHE_SIZE_X = NEST_SIZE_X
    CACHE_SIZE_Z = NEST_SIZE_Z

    CACHE_COLOR = '0 0.8 0 1'

    # position collision lower area
    COLLISION_LOWER_AREA_POSE_X = NEST_POSE_X
    COLLISION_LOWER_AREA_POSE_Y = (NEST_POSE_Y + CACHE_POSE_Y) / 2
    COLLISION_UPPER_AREA_POSE_Z = NEST_POSE_Z

    # size collision lower area
    COLLISION_LOWER_AREA_SIZE_X = NEST_SIZE_X
    COLLISION_LOWER_AREA_SIZE_Y = NEST_SIZE_Y + CACHE_SIZE_Y
    COLLISION_LOWER_AREA_SIZE_Z = NEST_SIZE_Z

    # slope size
    SLOPE_SIZE_X = NEST_SIZE_X
    SLOPE_SIZE_Z = NEST_SIZE_Z

    SLOPE_COLOR = '0 0.6 0 1'



    sdf = et.Element('sdf', version='1.9')

    model = et.SubElement(sdf, 'model', name='ground')

    static = et.SubElement(model, 'static')
    static.text = 'true'

    ######### LOWER AREA (nest area + cache area) ##########

    # lower area is splitted in nest area and cache area
    link_lower_area = et.SubElement(model, 'link,', name='link_lower_area')

    pose_lower_area = et.SubElement(link_lower_area, 'pose')
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
    diffuse_nest.text = NEST_COLOR

    # visual cache area
    visual_cache = et.SubElement(link_lower_area, 'visual', name='cache_area')

    pose_cache = et.SubElement(visual_nest, 'pose')
    pose_cache.text = f'{CACHE_POSE_X} {CACHE_POSE_Y} {CACHE_POSE_Z} 0 0 0'

    geometry_cache = et.SubElement(visual_cache, 'geometry')
    box_cache = et.SubElement(geometry_cache, 'box')
    size_box_nest = et.SubElement(box_cache, 'size')
    size_box_nest.text = f'{CACHE_SIZE_X} {CACHE_SIZE_Y} {CACHE_SIZE_Z}'

    material_cache = et.SubElement(visual_cache, 'material')
    diffuse_cache = et.SubElement(material_cache, 'diffuse')
    diffuse_cache.text = CACHE_COLOR

    # collision lower area
    collision_lower_area = et.SubElement(link_lower_area, 'collision', name='collision_lower_area')
    pose_collision_lower_area = et.SubElement(collision_lower_area, 'pose')
    pose_collision_lower_area.text = f'{COLLISION_LOWER_AREA_POSE_X} {COLLISION_LOWER_AREA_POSE_Y} {COLLISION_UPPER_AREA_POSE_Z} 0 0 0'

    geometry_collision_lower_area = et.SubElement(pose_collision_lower_area, 'geometry')
    box_collision_lower_area = et.SubElement(geometry_collision_lower_area, 'box')
    size_box_collision_lower_area = et.SubElement(box_collision_lower_area, 'size')
    size_box_collision_lower_area.text = f'{COLLISION_LOWER_AREA_SIZE_X} {COLLISION_LOWER_AREA_SIZE_Y} {COLLISION_LOWER_AREA_SIZE_Z}'

    ########### SLOPE AREA ##########

    link_slope = et.SubElement(model, 'link', name='link_slope')
    pose_slope = et.SubElement(link_slope, 'pose', relative_to='joint_nest_slope')
    pose_slope.text = f'0 {SLOPE_SIZE_Y / 2} 0 0 0 0'

    # visual slope
    visual_slope = et.SubElement(link_slope, 'visual', name='visual_slope')

    geometry_visual_slope = et.SubElement(visual_slope, 'geometry')
    box_visual_slope = et.SubElement(geometry_visual_slope, 'box')
    size_box_visual_slope = et.SubElement(box_visual_slope, 'size')
    size_box_visual_slope.text = f'{SLOPE_SIZE_X} {SLOPE_SIZE_Y} {SLOPE_SIZE_Z}'

    material_slope = et.SubElement(visual_slope, 'material')
    diffuse_slope = et.SubElement(material_slope, 'diffuse')
    diffuse_slope.text = SLOPE_COLOR

    # collision slope
    collision_slope = et.SubElement(link_slope, 'collision', name='collision_slope')
    geometry_collision_slope = et.SubElement(collision_slope, 'geometry')
    box_collision_slope = et.SubElement(geometry_collision_slope, 'box')
    size_box_collision_slope = et.SubElement(box_collision_slope, 'size')
    size_box_collision_slope.text = f'{SLOPE_SIZE_X} {SLOPE_SIZE_Y} {SLOPE_SIZE_Z}'


    ########### SOURCE AREA ##########
    link_source =
