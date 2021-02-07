# SuperDataBase
An AI database generator, Integrating objects into random backgrounds.

Requirements: make sure to pip install all of the important packages and you will need a python between 3.5 to 3.8, We used 3.7.0
tensorflow needs to be 1.15 
pip install tensorflow==1.15
and object detection 0.1

To use the project, make sure to clone the raw database from team 900. 
https://github.com/FRC900/tensorflow_workspace

After that, use xml_handler.py and use your videos folder path.

For create_tf_record.py file make sure when you see flags.DEFINE_string in the code to change the paths to the videos folder, the data folder and the label map file inside the data folder
