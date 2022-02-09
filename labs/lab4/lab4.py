"""
Garrett Lail
lab4.py

Problem: <Brief, one or two sentence description of the problem that this program solves, in your own words.>

I certify that this assignment is entirely my own work.
"""
from graphics import GraphWin, Polygon, Point, Text, color_rgb, Rectangle
import time

def greeting_card():
    heartwin = GraphWin('Greeting Card', 1000, 800)
    heartwin.setBackground("light blue")

    banner = Rectangle(Point(150,250), Point(850,350))
    banner1 = Rectangle(Point(0, 250), Point(150, 350))
    banner2 = Rectangle(Point(850, 250), Point(1000, 350))
    banner.draw(heartwin)
    banner1.draw(heartwin)
    banner2.draw(heartwin)
    banner.setFill(color_rgb(233,173,255))
    banner.setOutline(color_rgb(233,173,255))
    banner1.setFill(color_rgb(233,173,255))
    banner1.setOutline(color_rgb(233,173,255))
    banner2.setFill(color_rgb(233,173,255))
    banner2.setOutline(color_rgb(233,173,255))

    message = Text(Point(500, 50), "Happy Valentine's Day!")
    message.setFill("red")
    message.setSize(30)
    message.draw(heartwin)

    p1 = Point(500, 200)
    p2 = Point(600, 100)
    p3 = Point(700, 100)
    p4 = Point(800, 200)
    p5 = Point(800, 300)
    p6 = Point(500, 700)
    p7 = Point(200, 300)
    p8 = Point(200, 200)
    p9 = Point(300, 100)
    p10 = Point(400, 100)
    heart = Polygon(p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p1)
    heart.setFill("pink")
    heart.setOutline("pink")
    heart.draw(heartwin)

    a1 = Point(50, 400)
    a2 = Point(155, 325)
    a3 = Point(150, 375)
    a4 = Point(500, 375)
    a5 = Point(600, 335)
    a6 = Point(650, 335)
    a7 = Point(600,400)
    a8 = Point(650, 465)
    a9 = Point(600, 465)
    a10 = Point(500, 425)
    a11 = Point(150, 425)
    a12 = Point(155, 475)
    arrow = Polygon(a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12)
    arrow.setFill(color_rgb(255,135,135))
    arrow.setOutline(color_rgb(255,135,135))
    arrow.move(1000,0)
    arrow.draw(heartwin)

    hearthalf = Polygon(p1, p6, p7, p8, p9, p10, p1)
    hearthalf.setFill("pink")
    hearthalf.setOutline("pink")
    hearthalf.draw(heartwin)

    for i in range(1,10):
        arrow.move(-100, 0)
        banner.move(0, 25)
        time.sleep(0.3)
        banner.move(0,-25)
        time.sleep(0.2)

    closetxt = Text(Point(500, 750), "Click to Close")
    closetxt.draw(heartwin)
    heartwin.getMouse()
    heartwin.close()

greeting_card()