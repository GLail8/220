"""
Garrett Lail
hw10.py
I certify this assignment is my own work.
"""

def fibonacci(n):
    i, j = 0, 1
    count = 0
    while count < n:
        k = i + j
        i = j
        j = k
        count += 1
    return i

def double_investment(principle, rate):
    year_count = 0
    total = principle
    while total < (principle * 2):
        total = total * (1 + rate)
        year_count += 1
    return year_count

def syracuse(n):
    sequence = []
    sequence.append(n)
    while n > 1:
        if n % 2 == 0:
            n = n / 2
            sequence.append(int(n))
        else:
            n = 3 * n + 1
            sequence.append(int(n))
    return sequence



