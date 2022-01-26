"""
Name: <Garrett Lail>
GarrettHW1.py
Solved problems for Homework 1
I certify that this assignment is entirely my own work.
"""

#this program allows users to calculate the area of a rectangle
def calc_rec_area():
    length = eval(input("Enter the length: "))
    width = eval(input("Enter the width: "))
    area = length * width
    print("Area =", area)


#this program allows the user to calculate the volume of a rectangular solid
def calc_volume():
    length = eval(input("Enter the length: "))
    width = eval(input("Enter the width: "))
    height = eval(input("Enter the height:"))
    volume = length * width * height
    print("volume=", volume)


#this program calculates a players shooting percentage
def shooting_percentage():
    total = eval(input("Enter the player's total shots: "))
    made = eval(input("Enter how many shots the player made: "))
    shooting = (made / total) * 100
    print("Shooting Percentage: ", shooting, "%")


#this calculates the total cost of coffee per pound
def coffee():
    order = eval(input("How many pounds of coffee would you like? "))
    cost = 10.50
    shipping = 0.86
    fixed = 1.50
    total = (cost * order) + (shipping * order) + fixed
    print("Your total is: ", total)


#this program converts kilometers to miles
def kilometers_to_miles():
    km = eval(input("How many kilometers did you travel?"))
    mile = 1.61
    convert = km / mile
    print("That's", convert, "miles!")
