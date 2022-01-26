"""
Garrett Lail
lab2.py
Solved problems for lab 2
I certify that this assignment is entirely my own work.
"""
def means():
    number = eval(input("enter the values to be entered: "))
    rms_average = 0
    harmonic_mean = 0
    geometric_mean = 1
    for i in range(number):
        value = eval(input("enter value: "))
        rms_average = rms_average + (value ** 2)
        harmonic_mean = harmonic_mean + (1/value)
        geometric_mean = geometric_mean * value
    rms_average = (rms_average / number) ** (1/2)
    harmonic_mean = number / harmonic_mean
    geometric_mean = geometric_mean ** (1/number)
    print("RMS Average:", round(rms_average,3))
    print("Harmonic Average:", round(harmonic_mean,3))
    print("Geometric Average:", round(geometric_mean,3))


