"""
Garrett Lail
lab10.py
This lab is entirely my own work
"""
from graphics import GraphWin, Rectangle, Point
from Door import Door
from Button import Button
def main():
    win = GraphWin('Test', 800, 800)
    door = Door(Rectangle(Point(250, 300), Point(550, 800)), 'Closed')
    door.draw(win)
    door.close('red')
    button = Button(Rectangle(Point(250, 100), Point(550, 275)), 'Exit')
    button.draw(win)
    point = win.getMouse()
    while not button.is_clicked(point):
        point = win.getMouse()
        if door.is_clicked(point):
            if door.get_label() == 'Closed':
                door.open('white', 'Open')
            else:
                door.close('red')
        else:
            None
    win.close()

main()

