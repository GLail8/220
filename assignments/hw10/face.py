"""
Garrett Lail
face.py
This class is my own work
"""

from graphics import GraphWin, Circle, Line, Point, Polygon

class Face:
    def __init__(self):
        self.window = GraphWin('Face', 800, 800)
        self.face = Circle(Point(400,400), 350)
        self.left_eye = Circle(Point(275, 300), 50)
        self.right_eye = Circle(Point(525, 300), 50)
        self.mouth = Line(Point(275, 550), Point(525, 550))
        self.face.draw(self.window)
        self.left_eye.draw(self.window)
        self.right_eye.draw(self.window)
        self.mouth.draw(self.window)
        self.window.getMouse()
    def smile(self):
        self.mouth.undraw()
        self.mouth = Polygon(Point(275, 550), Point(525, 550), Point(400, 600))
        self.mouth.draw(self.window)
        self.window.getMouse()
    def shock(self):
        self.mouth.undraw()
        self.mouth = Circle(Point(400, 550), 50)
        self.mouth.draw(self.window)
        self.window.getMouse()
    def wink(self):
        self.left_eye.undraw()
        self.mouth.undraw()
        self.left_eye = Line(Point(225, 300), Point(325, 300))
        self.mouth = Polygon(Point(275, 550), Point(525, 550), Point(400, 600))
        self.left_eye.draw(self.window)
        self.mouth.draw(self.window)
        self.window.getMouse()

