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
        string_list = in_file[i].split()
        j = 0
        while j < len(string_list):
            data_list.append(eval(string_list[j]))
            j += 1
        i += 1
    return data_list

def is_in_linear(search_val, values):
    i = 0
    bool = False
    while i < len(values):
        if values[i] == search_val:
            bool = True
        i += 1
    return bool

def is_in_binary(search_val, values):
    upper = len(values) - 1
    lower = 0
    while lower < upper:
        midpoint = (upper + lower) // 2
        if search_val > values[midpoint]:
            lower = midpoint + 1
        else:
            upper = midpoint
    if search_val == values[lower]:
        return lower
    else:
        return None

def selection_sort(values):
    i = 0
    while i < len(values) - 1:
        min = i
        j = i + 1
        while j < len(values):
            if values[j] < values[min]:
                min = j
            j += 1
        values[i], values[min] = values[min], values[i]
        i += 1
    return values

def calc_area(rectangle):
    length = abs(rectangle.getP1().getX() - rectangle.getP2().getX())
    height = abs(rectangle.getP1().getY() - rectangle.getP2().getY())
    return length * height

def rect_sort(rectangles):
    area_list = []
    i = 0
    while i < len(rectangles):
        area_list.append(calc_area(rectangles[i]))
        i += 1
    selection_sort(area_list)
    return area_list

def star_find(filename):
    count = 0
    infile = open(filename, 'r')
    list = infile.readline().split()
    signals = []
    i = 0
    while i < len(list) and count < 5:
        if 4000 < eval(list[i]) < 5000:
            count += 1
            signals.append(list[i])
        i += 1
    print('A neutron star was found!')
    print('It took {} searches to find one.'.format(i))
    print('The signals received were {}.'.format(signals))

