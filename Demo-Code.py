import numpy as np
from PIL import Image
import os
import random
        
def main():
    gen = pic_generator(10, 4, 80, 250, 1280, 720)
    rand_pic_np, ball_set = gen.__next__()
    Image.fromarray(rand_pic_np).save("result.png")
    print(ball_set)

def pic_generator(yields_num: int, max_balls: int, min_diam: int, max_diam: int, bg_width: int, bg_height: int):
    """
    :param yields_num: number of yields
    :yield: get_random_pic(max_balls, min_diam, max_diam, bg_width, bg_height)  
    """
    for i in range(yields_num):
        yield get_random_pic(max_balls, min_diam, max_diam, bg_width, bg_height)

def get_random_pic(max_balls: int, min_diam: int, max_diam: int, bg_width: int, bg_height: int):
    """
    :param max_balls: max amount of balls printed on each picture
    :param min_diam: min diameter of each ball
    :param max_diam: max diameter of each ball
    :param bg_width: width of the background
    :param bg_height: height of the background
    :return: a numpy array representing a random background from "Demo-BGSet" resized to bg_width x bg_height with ball_count = 0...max_balls random balls from "Demo-BallSet"
                resized to a random diameter between min_diam and max_diam (including) printed on the background in random places,
                a numpy array of 0...max_balls tuples each representing a ball by it's center coordinates and radius
                when the array is sorted in accending order by the sum of its coordinates.
    """
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

def randomize_balls(max_balls: int, min_diam: int, max_diam: int, bg_width: int, bg_height: int):
    """
    :param max_balls: max amount of balls printed on each picture
    :param min_diam: min diameter of each ball
    :param max_diam: max diameter of each ball
    :param bg_width: width of the background
    :param bg_height: height of the background
    :return: a list of ball_count = 0...max_ball tuples containing randomized top left corner coordinates of the ball and it's randomized diameter
    """
    ball_count = random.randint(0, max_balls)
    tup_list = []
    for i in range(ball_count):
        legal = False
        while not legal:
            tup = create_ball(bg_width, bg_height, max_diam, min_diam)
            legal = is_ball_legal(tup_list, tup)
        tup_list.append(tup)
    return tup_list

def create_ball(bg_width: int, bg_height: int, max_diam: int, min_diam: int):
    """
    :param min_diam: min diameter of each ball
    :param max_diam: max diameter of each ball
    :param bg_width: width of the background
    :param bg_height: height of the background
    :return: a tuple containing the randomized top left corner coordinates and the randomized diameter of the ball
    """
    diam = random.randint(min_diam, max_diam)
    x = random.randint(0, bg_width - (diam + 1))
    y = random.randint(0, bg_height - (diam + 1))
    tup = (x, y, diam)
    return tup

def is_ball_legal(tup_list: list, tup: tuple):
    """
    :param tup_list: list of all balls olready created
    :param tup: a new ball
    :return: true if the ball does not interrupt other balls, else false
    """
    for i in tup_list:
        if (((i[0] + i[2] / 2.0) - (tup[0] + tup[2] / 2.0)) * ((i[0] + i[2] / 2.0) - (tup[0] + tup[2] / 2.0)) +
            ((i[1] + i[2] / 2.0) - (tup[1] + tup[2] / 2.0)) * ((i[1] + i[2] / 2.0) - (tup[1] + tup[2] / 2.0)) <=
            ((tup[2] + i[2]) / 2.0 + 1) * ((tup[2] + i[2]) / 2.0 + 1)):
            return False
    return True
    
def circle_copy_stupid(ball_arr: np.ndarray, bg_arr: np.ndarray, x_top_left: int, y_top_left: int, diameter: int):  # diameter equals to width
    """
    :param ball_arr: numpy array representing the background picture
    :param bg_arr: numpy array representing a ball picture
    :param x_top_left: the top left x coordinate of the location the ball is pasted on the background
    :param y_top_left: the top left y coordinate of the location the ball is pasted on the background
    :param diameter: the diameter of the ball
    """
    r = diameter / 2.0
    x_center, y_center = int(r - 0.25) + 0.5, int(r - 0.25) + 0.5
    for x_counter in range(diameter + 1):
        for y_counter in range(diameter + 1):
            if (r * r) >= (x_center - x_counter) ** 2 + (y_center - y_counter) ** 2:
                bg_arr[y_top_left + y_counter, x_top_left + x_counter] = ball_arr[y_counter, x_counter]
    return bg_arr

if __name__ == "__main__":
    main()
