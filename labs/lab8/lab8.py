"""
Garrett Lail
lab8.py
I certify that this lab is entirely my own work
"""

from random import randint
from graphics import GraphWin, Circle, Point, color_rgb
import time
from math import sqrt

# generates a random movement for the circles
def get_random():
    move = randint(-5, 5)
    return move

def did_collide(circle_1, circle_2):
    Circle_1 = circle_1.getCenter()
    Circle_2 = circle_2.getCenter()
    distance = sqrt((Circle_1.getX() - Circle_2.getX()) ** 2 + (Circle_1.getY() - Circle_2.getY()) ** 2)
    if distance <= 200:
        return True
    else:
        return False


def hit_vertical(circle, window):
    Circle = circle.getCenter()
    if Circle.getX() >= 100 or Circle.getX() <= 700:
        return True
    else:
        return False

def hit_horizontal(circle, window):
    Circle = circle.getCenter()
    if Circle.getY() >= 100 or Circle.getY() <= 700:
        return True
    else:
        return False

# generates a random color
def get_random_color():
    red = randint(0, 255)
    green = randint(0, 255)
    blue = randint(0, 255)
    color = color_rgb(red, green, blue)
    return color

def bumper():
#creates the window, draws the circles and assigns a random color using get_random_color
    win = GraphWin('Bumper Cars', 800, 800)
    circle_1 = Circle(Point(randint(0, 800), randint(0, 800)), 100)
    circle_2 = Circle(Point(randint(0, 800), randint(0, 800)), 100)
    circle_1.draw(win)
    circle_2.draw(win)
    circle_1.setFill(get_random_color())
    circle_2.setFill(get_random_color())

    circle_1_dx = get_random()
    circle_1_dy = get_random()
    circle_2_dx = get_random()
    circle_2_dy = get_random()

    while True:
        circle_1.move(circle_1_dx, circle_1_dy)
        circle_2.move(circle_2_dx, circle_2_dy)
        time.sleep(.01)
        if did_collide(circle_1, circle_2):
                circle_1_dx = circle_1_dx * -1
                circle_1_dy = circle_1_dy * -1
                circle_2_dx = circle_2_dx * -1
                circle_2_dy = circle_2_dy * -1
        if hit_vertical(circle_1, win):
            circle_1_dx = circle_1_dx * -1
        if hit_vertical(circle_2, win):
            circle_2_dx = circle_2_dx * -1
        if hit_horizontal(circle_1, win):
            circle_1_dy = circle_1_dy * -1
        if hit_horizontal(circle_2, win):
            circle_2_dy = circle_2_dy * -1
        if win.checkMouse():
            win.close()


bumper()