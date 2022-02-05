"""
Garrett Lail
Garretthw3.py

Problem: <Brief, one or two sentence description of the problem that this program solves, in your own words.>

I certify that this assignment is entirely my own work.
"""

#finds the average of the grades input
def average():
    grade_total = eval(input("how many grades will you enter? "))
    grade_avg = 0
    for i in range(grade_total):
        grade = eval(input("Enter grade: "))
        grade_avg = grade_avg + grade
    average = grade_avg / grade_total
    print("average is", average)

#calculates the tips from 5 people
def tip_jar():
    tip_total = 0
    for j in range(5):
        tip = eval(input("how much would you like to donate?"))
        tip_total = tip_total + tip
    print("total tips: ", tip_total)

#calculates the approximate root using Newton's method
def newton():
    x = eval(input("What number do you want to square root? "))
    impr = eval(input("How many times should we improve the approximation? "))
    approx = x
    for k in range(impr):
        approx = (approx + (x / approx)) / 2
    print("the square root is approximately", approx)


def sequence():
    pass


#computes the approximate value of pi using the wallis formula
def pi():
    series = eval(input("how may terms in the series?"))
    wallis = 1
    num = 2
    for m in range(series):
        term1 = num / (num -1)
        term2 = num / (num+1)
        wallis = wallis * term1 * term2
        num = num + 2
    pi = wallis * 2
    print(pi)



