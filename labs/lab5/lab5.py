"""
Garrett Lail
lab5.py
I certify this lab is my own work
"""
from graphics import GraphWin, Polygon, Text, Point, Circle, Entry, color_rgb

def triangle():
    triwin = GraphWin('Triangle', 900, 900)
    tclick1 = triwin.getMouse()
    tclick2 = triwin.getMouse()
    tclick3 = triwin.getMouse()
    triangle = Polygon(tclick1, tclick2, tclick3)
    triangle.draw(triwin)
    side1 = ((tclick1.x-tclick2.x)** 2 + (tclick1.y-tclick2.y)**2) ** (1/2)
    side2 = ((tclick2.x-tclick3.x)** 2 + (tclick2.y-tclick3.y)**2) ** (1/2)
    side3 = ((tclick1.x-tclick3.x)** 2 + (tclick1.y-tclick3.y)**2) ** (1/2)
    perimeter = side1 + side2 + side3
    per = Text(Point(450, 800), perimeter)
    pertext = Text(Point(300, 800), 'Perimeter =')
    per.draw(triwin)
    pertext.draw(triwin)
    sides = (side1 + side2 + side3) / 2
    area = (sides * (sides - side1) * (sides - side2) * (sides - side3)) ** (1/2)
    ar = Text(Point(450, 850), area)
    artext = Text(Point(300, 850), 'Area =')
    ar.draw(triwin)
    artext.draw(triwin)
    triwin.getMouse()
    triwin.close()

def color_shape():
    '''Create code to allow a user to color a shape by entering rgb amounts'''

    # create window
    win_width = 400
    win_height = 400
    win = GraphWin("Color Shape", win_width, win_height)
    win.setBackground("white")

    # create text instructions
    msg = "Enter color values between 0 - 255\nClick window to color shape"
    inst = Text(Point(win_width / 2, win_height - 20), msg)
    inst.draw(win)

    # create circle in window's center
    shape = Circle(Point(win_width / 2, win_height / 2 - 30), 50)
    shape.draw(win)

    # redTexPt is 50 pixels to the left and forty pixels down from center
    red_text_pt = Point(win_width / 2 - 50, win_height / 2 + 40)
    red_text = Text(red_text_pt, "Red: ")
    red_text.setTextColor("red")

    # green_text_pt is 30 pixels down from red
    green_text_pt = red_text_pt.clone()
    green_text_pt.move(0, 30)
    green_text = Text(green_text_pt, "Green: ")
    green_text.setTextColor("green")

    # blue_text_pt is 60 pixels down from red
    blue_text_pt = red_text_pt.clone()
    blue_text_pt.move(0, 60)
    blue_text = Text(blue_text_pt, "Blue: ")
    blue_text.setTextColor("blue")

    # display rgb text
    red_text.draw(win)
    green_text.draw(win)
    blue_text.draw(win)

    red_entry = Entry(Point(200, 240), 3)
    green_entry = Entry(Point(200, 270), 3)
    blue_entry = Entry(Point(200, 300), 3)
    red_entry.draw(win)
    green_entry.draw(win)
    blue_entry.draw(win)

    for color in range(5):
        win.getMouse()
        rtext = red_entry.getText()
        gtext = green_entry.getText()
        btext = blue_entry.getText()
        shape.setFill(color_rgb(int(rtext), int(gtext), int(btext)))

    # Wait for another click to exit
    win.getMouse()
    win.close()


def process_string():
    string = input("Enter a string: ")
    print(string[0])
    print(string[-1])
    print(string[1:5])
    print(string[0] + string[-1])
    print(string[:3]*10)
    for character in string:
        print(character)
    print(len(string))


def process_list():
    pt = Point(5,10)
    values = [5, "hi", 2.5, "there", pt, "7.2"]
    x = values[1] + values[3]
    print(x)
    x = values[0] + eval(values[5])
    print(x)
    x = values[1] * 5
    print(x)
    x = [values[2], values[3], pt]
    print(x)
    x = [values[2], values[3], values[0]]
    print(x)
    x = [values[2], values[0], float(values[5])]
    print(x)
    x = values[0] + values[2] + float(values[5])
    print(x)
    x = len(values)
    print(x)

def another_series():
    terms = eval(input('How many terms would you like? '))
    sum = 0
    for i in range(terms):
        series = (i % 3 + 1) * 2
        print(series, end=" ")
        sum = series + sum
    print("\n", "sum =", sum)


def target():
    winheight = 500
    winwidth = winheight
    tarwin = GraphWin('Target', winheight, winwidth)
    center = Point(winheight/2, winwidth/2)
    radius = winheight/2
    whcirc = Circle(center, radius)
    whcirc.setFill("white")
    blkcirc = Circle(center, radius * (4/5))
    blkcirc.setFill("black")
    blucirc = Circle(center, radius * (3/5))
    blucirc.setFill("blue")
    redcirc = Circle(center, radius * (2/5))
    redcirc.setFill("red")
    yelcirc = Circle(center, radius * (1/5))
    yelcirc.setFill("yellow")
    whcirc.draw(tarwin)
    blkcirc.draw(tarwin)
    blucirc.draw(tarwin)
    redcirc.draw(tarwin)
    yelcirc.draw(tarwin)
    tarwin.getMouse()
    closetxt = Text(center, 'Click to close')
    closetxt.draw(tarwin)
    tarwin.getMouse()
    tarwin.close()

