"""
Name: Garrett Lail
hw8.py

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""
from graphics import GraphWin, Circle, Text, Point
import math

def add_ten(nums):
    for number in range(len(nums)):
        nums[number] = nums[number] + 10


def square_each(nums):
    for number in range(len(nums)):
        nums[number] = nums[number] ** 2
    return nums


def sum_list(nums):
    sum = 0
    for number in range(len(nums)):
        sum = sum + nums[number]
    return sum


def to_numbers(nums):
    for string in range(len(nums)):
        nums[string] = eval(nums[string])
    return nums


def sum_of_square(nums):
    sum_square_list = []
    to_numb = to_numbers(nums)
    for number in range(len(to_numb)):
        nest_list = list(to_numb[number])
        squares = square_each(nest_list)
        sum = sum_list(squares)
        sum_square_list.append(sum)
    return sum_square_list


def starter(weight, wins):
    if weight >= 150 and weight < 160 and wins >= 5:
        return True
    elif weight > 199 or wins > 20:
        return True
    else:
        return False


def leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def circle_overlap():
    width_px = 700
    height_px = 700
    win = GraphWin("Circle", width_px, height_px)
    width = 10
    height = 10
    win.setCoords(0, 0, width, height)

    center = win.getMouse()
    circumference_point = win.getMouse()
    radius = math.sqrt(
        (center.getX() - circumference_point.getX()) ** 2 + (center.getY() - circumference_point.getY()) ** 2)
    circle_one = Circle(center, radius)
    circle_one.setFill("light blue")
    circle_one.draw(win)

    center2 = win.getMouse()
    circumference_point2 = win.getMouse()
    radius2 = math.sqrt(
        (center2.getX() - circumference_point2.getX()) ** 2 + (center2.getY() - circumference_point2.getY()) ** 2)
    circle_two = Circle(center2, radius2)
    circle_two.setFill('light green')
    circle_two.draw(win)

    if did_overlap(circle_one, circle_two):
        overlap_true = Text(Point(5,3), 'The circles overlap.')
        overlap_true.draw(win)
    else:
        overlap_false = Text(Point(5,3), 'The circles do not overlap.')
        overlap_false.draw(win)

    close_text = Text(Point(5,2), 'Click again to close.')
    close_text.draw(win)

    win.getMouse()

def did_overlap(circle_one, circle_two):
    center1 = circle_one.getCenter()
    center2 = circle_two.getCenter()
    distance = math.sqrt(
        (center2.getX() - center1.getX()) ** 2 + (center2.getY() - center1.getY()) ** 2)
    radius1 = circle_one.getRadius()
    radius2 = circle_two.getRadius()
    if distance < radius1 + radius2:
        return True
    else:
        return False

if __name__ == '__main__':
    pass
