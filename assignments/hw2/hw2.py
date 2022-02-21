"""
Garrett Lail
hw2.py
I certify that this assignment is entirely my own work.
"""
import math

#finds the sum of threes for a given integer input
def sum_of_threes():
    bound = eval(input('What is the upper bound? '))
    sum = 0
    for i in range(0, bound, 3):
        sum = sum + i
    print("sum of threes is:", sum)



#generates a multiplication table for the numbers one through ten
def multiplication_table():
    for l in range(1, 11):
        print(l, l * 2, l * 3, l * 4, l * 5, l * 6, l * 7, l * 8, l * 9, l * 10, sep="\t")



#finds the area of a triangle with sides A, B, C
def triangle_area():
    A = eval(input("Enter side a length: "))
    B = eval(input("Enter side b length: "))
    C = eval(input("Enter side c length: "))
    s = (A + B + C) / 2
    Area = math.sqrt(s * (s - A) * (s - B) * (s - C))
    print("area is: ", Area)

#finds the sum of the squared integers of a given range
def sum_squares():
    Lower = eval(input("Enter lower range: "))
    Upper = eval(input("Enter upper range: "))
    squares = 0
    for j in range(Lower, Upper+1):
        squares = squares + j*j
    print(squares)

#Finds the power of an integer using a given base and exponent
def power():
    Base = eval(input("Enter base: "))
    Exponent = eval(input("Enter exponent: "))
    Power = 1
    for k in range(1, Exponent+1):
        Power = Power * Base
    print(Base, "^", Exponent, "=", Power)


if __name__ == '__main__':
    pass
