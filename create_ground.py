import xml.etree.ElementTree as et

from utils import get_custom_xml_declaration



def create_ground(NEST_SIZE_X, NEST_SIZE_Y, CACHE_SIZE_Y, SLOPE_SIZE_Y, SLOPE_ANGLE, SOURCE_SIZE_Y):
    # nest position
    NEST_POSE_X = 0
    NEST_POSE_Y = 1
    NEST_POSE_Z = 0

    NEST_SIZE_Z = 0.1

    NEST_COLOR = '0 1 0 1'

    # cache position
    CACHE_POSE_X = NEST_POSE_X
    CACHE_POSE_Y = (NEST_POSE_Y + NEST_SIZE_Y / 2) + CACHE_SIZE_Y / 2
    CACHE_POSE_Z = NEST_POSE_Z

    # cache size
    CACHE_SIZE_X = NEST_SIZE_X
    CACHE_SIZE_Z = NEST_SIZE_Z

    CACHE_COLOR = '0 0.8 0 1'

    # position collision lower area
    COLLISION_LOWER_AREA_POSE_X = NEST_POSE_X
    COLLISION_LOWER_AREA_POSE_Y = (NEST_POSE_Y*NEST_SIZE_Y + CACHE_POSE_Y*CACHE_SIZE_Y) / (NEST_SIZE_Y+CACHE_SIZE_Y)
    COLLISION_UPPER_AREA_POSE_Z = NEST_POSE_Z

    # size collision lower area
    COLLISION_LOWER_AREA_SIZE_X = NEST_SIZE_X
    COLLISION_LOWER_AREA_SIZE_Y = NEST_SIZE_Y + CACHE_SIZE_Y
    COLLISION_LOWER_AREA_SIZE_Z = NEST_SIZE_Z

    # slope size
    SLOPE_SIZE_X = NEST_SIZE_X
    SLOPE_SIZE_Z = NEST_SIZE_Z

    SLOPE_COLOR = '0 0.6 0 1'

    # source area size
    SOURCE_SIZE_X = NEST_SIZE_X
    SOURCE_SIZE_Z = NEST_SIZE_Z

    SOURCE_COLOR = '0 0.4 0 1'

    # joint cache-slope position relative to link lower area
    JOINT_CACHE_SLOPE_POSE_X = 0
    JOINT_CACHE_SLOPE_POSE_Y = CACHE_POSE_Y + CACHE_SIZE_Y/2
    JOINT_CACHE_SLOPE_POSE_Z = 0

    # joint slope-source position relative to link slope
    JOINT_SLOPE_SOURCE_POSE_X = 0
    JOINT_SLOPE_SOURCE_POSE_Y = SLOPE_SIZE_Y/2
    JOINT_SLOPE_SOURCE_POSE_Z = 0

    #######################
    # start defining code #
    #######################



    sdf = et.Element('sdf', version='1.9')

    model = et.SubElement(sdf, 'model', name='ground')

    static = et.SubElement(model, 'static')
    static.text = 'true'

    ######### LOWER AREA (nest area + cache area) ##########

    # lower area is splitted in nest area and cache area, the splitting is used for visualization purpose.
    # For collisions we can refer to the lower area

    link_lower_area = et.SubElement(model, 'link', name='link_lower_area')

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

    pose_cache = et.SubElement(visual_cache, 'pose')
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

    geometry_collision_lower_area = et.SubElement(collision_lower_area, 'geometry')
    box_collision_lower_area = et.SubElement(geometry_collision_lower_area, 'box')
    size_box_collision_lower_area = et.SubElement(box_collision_lower_area, 'size')
    size_box_collision_lower_area.text = f'{COLLISION_LOWER_AREA_SIZE_X} {COLLISION_LOWER_AREA_SIZE_Y} {COLLISION_LOWER_AREA_SIZE_Z}'

    ########### SLOPE AREA ##########

    link_slope = et.SubElement(model, 'link', name='link_slope')
    pose_slope = et.SubElement(link_slope, 'pose', relative_to='joint_cache_slope')
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
    link_source = et.SubElement(model, 'link', name='link_source_area')
    pose_source = et.SubElement(link_source, 'pose', relative_to='joint_slope_source')
    pose_source.text = f'0 {SOURCE_SIZE_Y / 2} 0 0 0 0'

    # visual source
    visual_source = et.SubElement(link_source, 'visual', name='visual_source_area')
    geometry_visual_source = et.SubElement(visual_source, 'geometry')
    box_visual_source = et.SubElement(geometry_visual_source, 'box')
    size_box_source = et.SubElement(box_visual_source, 'size')
    size_box_source.text = f'{SOURCE_SIZE_X} {SOURCE_SIZE_Y} {SOURCE_SIZE_Z}'

    material_source = et.SubElement(visual_source, 'material')
    diffuse_source = et.SubElement(material_source, 'diffuse')
    diffuse_source.text = SOURCE_COLOR

    # collision source
    collision_source = et.SubElement(link_source, 'collision', name='collision_source_area')
    geometry_collision_source = et.SubElement(collision_source, 'geometry')
    box_collision_source = et.SubElement(geometry_collision_source, 'box')
    size_box_collision_source = et.SubElement(box_collision_source, 'size')
    size_box_collision_source.text = f'{SOURCE_SIZE_X} {SOURCE_SIZE_Y} {SOURCE_SIZE_Z}'

    ########## JOINTS #########

    # joint cache slope
    joint_cache_slope = et.SubElement(model, 'joint', name='joint_cache_slope', type='fixed')

    parent_joint_slope_source = et.SubElement(joint_cache_slope, 'parent')
    parent_joint_slope_source.text = 'link_lower_area'

    child_joint_slope_source = et.SubElement(joint_cache_slope, 'child')
    child_joint_slope_source.text = 'link_slope'

    pose_joint_slope_source = et.SubElement(joint_cache_slope, 'pose', relative_to='link_lower_area')
    pose_joint_slope_source.text = f'{JOINT_CACHE_SLOPE_POSE_X} {JOINT_CACHE_SLOPE_POSE_Y} {JOINT_CACHE_SLOPE_POSE_Z} {SLOPE_ANGLE} 0  0'

    axis_joint_cache_slope = et.SubElement(joint_cache_slope, 'axis')
    xyz_axis_joint_cache_slope = et.SubElement(axis_joint_cache_slope, 'xyz')
    xyz_axis_joint_cache_slope.text = '1 0 0'


    # joint slope source
    joint_slope_source = et.SubElement(model, 'joint', name='joint_slope_source', type='fixed')

    parent_joint_slope_source = et.SubElement(joint_slope_source, 'parent')
    parent_joint_slope_source.text = 'link_slope'

    child_joint_slope_source = et.SubElement(joint_slope_source, 'child')
    child_joint_slope_source.text = 'link_source_area'

    pose_joint_slope_source = et.SubElement(joint_slope_source, 'pose', relative_to='link_slope')
    pose_joint_slope_source.text = f'{JOINT_SLOPE_SOURCE_POSE_X} {JOINT_SLOPE_SOURCE_POSE_Y} {JOINT_SLOPE_SOURCE_POSE_Z} {-SLOPE_ANGLE} 0 0'

    axis_joint_slope_source = et.SubElement(joint_slope_source, 'axis')
    xyz_axis_joint_slope_source = et.SubElement(axis_joint_slope_source, 'xyz')
    xyz_axis_joint_slope_source.text = '1 0 0'

    # output file with customized xml declaration for SDF files
    get_custom_xml_declaration(sdf, 'ground.sdf')

