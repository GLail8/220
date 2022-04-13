"""
Garrett Lail
algorithms.py
I certify this lab is my own

"""

def read_data(filename):
    in_file = open(filename, 'r').readlines()
    data_list = []
    i = 0
    while i < len(in_file):
        data_list += in_file[i].split()
        i += 1
    return data_list

def is_in_linear (search_val, values):
    i = 0
    bool = False
    while i < len(values):
        if values[i] == search_val:
            bool = True
        i += 1
    print(bool)
