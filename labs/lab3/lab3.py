"""
Garrett Lail
lab3.py
Solved problems for lab 3
I certify that this assignment is entirely my own work.
"""


def traffic():
    road_total = eval(input("How many roads were surveyed?"))
    totalnum = 0
    for i in range(road_total):
        numerator = 0
        print("How many days was road", i+1, "surveyed?")
        days = eval(input(""))
        for j in range(days):
            print("\t How many cars traveled on day", j+1, "?")
            cars = eval(input(" "))
            numerator = numerator + cars
            totalnum = totalnum + cars
        day_average = numerator / days
        print("Road", i+1, "average vehicles per day:", day_average)
    total_average = totalnum / road_total
    print("Total number vehicles traveled on all roads:", numerator)
    print("Average number of vehicles per road:", round(total_average, 2))

traffic()

