import os
import numpy as np
from PIL import Image

def main():
    """
    This function turns all Ball picture and BG pictures to RGB (24 bit per pixel).
    If the files are already RGB, the functions does nothing.
    """
    ball_files, bg_files = os.listdir("Demo-BallSet"), os.listdir("Demo-BGSet")
    for ball in (ball_files): #for each ball in the files
        rgb_ball_image = Image.open("Demo-BallSet" + os.sep + ball).convert('RGB') #set it to RGB
        np_ball = np.array(rgb_ball_image) #turm image to np.ndarray
        Image.fromarray(np_ball).save("Demo-BallSet" + os.sep + ball) #save it in the same file it was before
    for bg in (bg_files): #same for backgrounds...
        rgb_bg_image = Image.open("Demo-BGSet" + os.sep + bg).convert('RGB')
        np_bg = np.array(rgb_bg_image)
        Image.fromarray(np_bg).save("Demo-BGSet" + os.sep + bg)
        
if __name__ == "__main__":
    main()
