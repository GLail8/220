"""
Garrett Lail
lab7.py
This lab is my own work
"""

def weighted_average(in_file_name, out_file_name):
    in_file = open(in_file_name, 'r')
    out_file = open(out_file_name, 'w')
    list = in_file.readlines()
    print(list)
    for i in range(len(list)):







    in_file.close()


weighted_average('grades.txt', 'avg.txt')
