"""
Garrett Lail
lab13.py
I certify this lab is my own work
"""

from lab12.algorithms import is_in_binary, selection_sort, rect_sort, star_find
from graphics import Rectangle, Point

if __name__ == '__main__':
    is_in_binary(2, [1, 2, 3, 4, 5, 6])
    selection_sort([9, 45, 3, 42, 50, 41, 31, 15])
    rect_sort([Rectangle(Point(3, 29), Point(15, 16)),
               Rectangle(Point(12, 46), Point(24, 41)),
               Rectangle(Point(34, 40), Point(16, 45))])
    star_find('signals.txt')

