'''
Various tests of label xml files to find errors
'''
import xml.etree.ElementTree as ET
import glob
import os
max_obj_counts = {
'yellow_control_panel_light',
'blue_power_port_high_goal',
'red_robot',
'red_shield_generator_light' ,
'blue_shield_generator_light',
'blue_robot',
'red_loading_bay_left_graphics',
'blue_black_shield_generator_floor_intersection',
'shield_generator_floor_center_intersection',
'red_loading_bay_tape',
'blue_power_port_low_goal',
'red_black_shield_generator_floor_intersection',
'red_power_port_high_goal',
'red_loading_bay_right_graphics',
'blue_loading_bay_tape',
'control_panel_light',
'blue_power_port_first_logo',
'blue_loading_bay_left_graphics',
'blue_loading_bay_right_graphics',
'red_shield_pillar_intersection',
'blue_shield_pillar_intersection',
'red_ds_light',
'ds_light',
'red_blue_black_shield_generator_floor_intersection',
'red_power_port_low_goal',
'red_power_port_first_logo',
'color_wheel',
'shield_generator_backstop',
'power_port_yellow_graphics',
'blue_ds_light',
'ds_numbers',
'power_port_yellow_graphics',
'power_port_first_logo',
'red_tape_corner',
'blue_tape_corner',
'shield_generator_first_logo',
'shield_generator_yellow_stripe'
}
def findAllObjectsNamed(tree, obj_name):
    find_str = "object[name='" + obj_name +"']"
    return tree.findall(find_str)

def changepath(xml, userpath):
    tree = ET.parse(xml)
    tree.find('path').text = tree.find('path').text.replace('/home/ubuntu/tensorflow_workspace/2020Game/data', userpath) 
    tree.write(xml)


    
xml_files = glob.glob("videos/*.xml")
for xml_file in xml_files:
    tree = ET.parse(xml_file)
    # In each, look for each object type in the
    # XML. Make sure there aren't more labeled
    # images than could possibly be seen in any one image
    for obj in max_obj_counts:
        r = findAllObjectsNamed(tree, obj)
        root = tree.getroot()
        for object1 in r:
            if(object1!='power_cell'):
                root.remove(object1)
    tree.write(xml_file)
    changepath(xml, userpath)


