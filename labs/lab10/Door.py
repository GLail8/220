"""
Garrett Lail
Door.py
This class is entirely my own work
"""
from graphics import Text

class Door:
    def __init__(self, shape, label):
        self.shape = shape
        self.text = Text(shape.getCenter(), label)
        self.secret = False
    def get_label(self):
        return self.text.getText()
    def set_label(self, new_label):
        self.text.setText(new_label)
    def draw(self, win):
        self.shape.draw(win)
        self.text.draw(win)
    def undraw(self):
        self.shape.undraw()
        self.text.undraw()
    def is_clicked(self, point):
        p1x = point.getX() >= (self.shape.getP1()).getX()
        p2x = point.getX() >= (self.shape.getP2()).getX()
        p1y = point.getY() >= (self.shape.getP1()).getY()
        p2y = point.getY() >= (self.shape.getP2()).getY()
        if p1x and p2x and p1y and p2y:
            return True
        else:
            return False
    def open(self, color, open_label):
        self.shape.setFill(color)
        self.text.setText(open_label)
    def close(self, color):
        self.shape.setFill(color)
    def is_secret(self):
        return self.secret
    def set_secret(self, secret):
        self.secret = secret