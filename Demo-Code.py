import numpy as np
from PIL import Image
import os
import random
        
def main():
    gen = pic_generator(10, 4, 80, 250, 1280, 720)
    rand_pic_np, ball_set = gen.__next__()
    Image.fromarray(rand_pic_np).save("result.png")
    print(ball_set)

def pic_generator(yields_num, max_balls, min_diam, max_diam, bg_width, bg_height):
    for i in range(yields_num):
        yield get_random_pic(max_balls, min_diam, max_diam, bg_width, bg_height)

def get_random_pic(max_balls, min_diam, max_diam, bg_width, bg_height):
    bg_file = random.choice(os.listdir("Demo-BGSet"))
    bg_image = Image.open("Demo-BGSet" + os.sep + bg_file) 
    bg_arr = np.array(bg_image.resize((bg_width, bg_height)))
    ball_list = randomize_balls(max_balls, min_diam, max_diam, bg_width, bg_height) #the balls are min_diam - max_diam pixels wide, and there is a max of max_balls balls.
    for i in range(len(ball_list)):
        ball_file = random.choice(os.listdir("Demo-BallSet"))
        ball_image = Image.open("Demo-BallSet" + os.sep + ball_file)
        bg_arr = circle_copy_stupid(np.array(ball_image.resize((ball_list[i][2], ball_list[i][2]))), bg_arr, ball_list[i][0], ball_list[i][1], ball_list[i][2])
        ball_list[i] = (ball_list[i][0] + ball_list[i][2] / 2.0 - 0.5, ball_list[i][1] + ball_list[i][2] / 2.0 - 0.5, ball_list[i][2] / 2.0)
    ball_list.sort(key = lambda item: item[0] + item[1])
    return (bg_arr, np.array(ball_list))

def randomize_balls(max_balls, min_diam, max_diam, bg_width, bg_height):
    ball_count = random.randint(0, max_balls)
    tup_list = []
    for i in range(ball_count):
        legal = False
        while not legal:
            tup = create_ball(bg_width, bg_height, max_diam, min_diam)
            legal = is_ball_legal(tup_list, tup)
        tup_list.append(tup)
    return tup_list

def create_ball(bg_width, bg_height, max_diam, min_diam):
    diam = random.randint(min_diam, max_diam)
    x = random.randint(0, bg_width - (diam + 1))
    y = random.randint(0, bg_height - (diam + 1))
    tup = (x, y, diam)
    return tup

def is_ball_legal(tup_list, tup):
    for i in tup_list:
        if (((i[0] + i[2] / 2.0) - (tup[0] + tup[2] / 2.0)) * ((i[0] + i[2] / 2.0) - (tup[0] + tup[2] / 2.0)) +
            ((i[1] + i[2] / 2.0) - (tup[1] + tup[2] / 2.0)) * ((i[1] + i[2] / 2.0) - (tup[1] + tup[2] / 2.0)) <=
            ((tup[2] + i[2]) / 2.0 + 1) * ((tup[2] + i[2]) / 2.0 + 1)):
            return False
    return True
    
def circle_copy_stupid(ball_arr, bg_arr, x_top_left, y_top_left, diameter):  # diameter equals to width
    r = diameter / 2.0
    x_center, y_center = int(r - 0.25) + 0.5, int(r - 0.25) + 0.5
    for x_counter in range(diameter + 1):
        for y_counter in range(diameter + 1):
            if (r * r) >= (x_center - x_counter) ** 2 + (y_center - y_counter) ** 2:
                bg_arr[y_top_left + y_counter, x_top_left + x_counter] = ball_arr[y_counter, x_counter]
    return bg_arr

if __name__ == "__main__":
    main()
