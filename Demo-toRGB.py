import os
import numpy as np
from PIL import Image

def main():
    ball_files, bg_files = os.listdir("Demo-BallSet"), os.listdir("Demo-BGSet")
    for ball in (ball_files):
        rgb_ball_image = Image.open("Demo-BallSet" + os.sep + ball).convert('RGB')
        np_ball = np.array(rgb_ball_image)
        Image.fromarray(np_ball).save("Demo-BallSet" + os.sep + ball)
    for bg in (bg_files):
        rgb_bg_image = Image.open("Demo-BGSet" + os.sep + bg).convert('RGB')
        np_bg = np.array(rgb_bg_image)
        Image.fromarray(np_bg).save("Demo-BGSet" + os.sep + bg)

if __name__ == "__main__":
    main()
