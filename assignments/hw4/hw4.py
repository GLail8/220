"""
Garrett Lail
hw4.py
I certify that this assignment is entirely my own work.
"""
from graphics import Point, GraphWin, Rectangle, Text, Circle

# lets the user click inside a window to draw six squares centered on the mouse
def squares():
    sqwin = GraphWin('Clicks', 1000, 800)
    sqtext = Text(Point(500, 700), 'click to draw a square')
    sqtext.draw(sqwin)
    for k in range(6):
        click = sqwin.getMouse()
        square = Rectangle(Point(click.x+25, click.y+25), Point(click.x-25, click.y-25))
        square.setFill('red')
        square.setOutline('red')
        square.draw(sqwin)
    sqclose = Text(Point(500, 400), 'click again to close')
    sqclose.draw(sqwin)
    sqwin.getMouse()
    sqwin.close()

# lets the user draw a rectangle by clicking two opposide edges
def rectangle():
    win = GraphWin('Rectangle', 1000, 800)
    click1 = win.getMouse()
    click2 = win.getMouse()
    rectangle = Rectangle(click1, click2)
    rectangle.setFill("Green")
    rectangle.draw(win)

    perimeter = (abs(click1.x - click2.x) + abs(click1.y - click2.y)) * 2
    perimstr = Text(Point(500, 740), str(perimeter))
    ptext = Text(Point(430, 740), "Perimeter:")
    ptext.draw(win)
    perimstr.draw(win)

    area = abs(click1.x - click2.x) * abs(click1.y - click2.y)
    areastr = Text(Point(500, 760), area)
    areatxt = Text(Point(430, 760), "Area:")
    areastr.draw(win)
    areatxt.draw(win)

    close = Text(Point(500, 400), "Click again to close")
    close.draw(win)
    win.getMouse()


# lets the user draw a circle by defining the center and the edge via mouse click
def circle():
    cwin = GraphWin('Circle', 1000, 800)
    center = cwin.getMouse()
    circum = cwin.getMouse()

    radius = ((circum.x - center.x) ** 2 + (circum.y - center.y) ** 2) ** (1/2)
    circle = Circle(center, radius)
    circle.draw(cwin)
    circle.setFill("light blue")

    radstr = Text(Point(500, 750), radius)
    radtxt = Text(Point(390, 750), "Radius:")
    radstr.draw(cwin)
    radtxt.draw(cwin)

    cclose = Text(Point(500, 400), "Click again to close")
    cclose.draw(cwin)
    cwin.getMouse()


from math import pi

# approximates pi with the input of the number to terms to sum and output the approximation and the accuracy of the
# approxiation
def pi2():
    terms = eval(input("enter the number of terms to sum:"))
    sum = 0
    sub = 0
    for i in range(0, terms, 2):
        sum = sum + 4/(2*i+1)
    for j in range(1, terms, 2):
        sub = sub + 4/(2*j+1)
    pi2 = sum - sub
    print("pi approximation:", pi2)
    print("accuracy: ", abs(pi2 - pi))


