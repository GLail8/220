"""
Garrett Lail
hw6.py

Certification of Authenticity:
This assignment is entirely my own work.
"""

# takes an integer input and converts it to a dollar amount
def cash_converter():
    integer = eval(input('enter an integer: '))
    print('That is ${:.2f}'.format(integer))

#takes a message and encodes it using a provided integer key
def encode():
    message = input('enter a message: ')
    key = eval(input('enter a key: '))
    cipher = ''
    for letter in range(len(message)):
        encode = ord(message[letter]) + key
        decode = chr(encode)
        cipher = cipher + decode
    print(cipher)

# this function calculates the surface area of a sphere with the given radius
import math

def sphere_area(radius):
    surface_area = 4 * math.pi * radius ** 2
    return surface_area

# this function calculates the volume of a sphere with the given radius
import math

def sphere_volume(radius):
    volume = (4/3) * math.pi * radius ** 3
    return volume

# returns the sum of the first natural numbers up to the provided integer
def sum_n(number):
    total = 0
    for natural_sum in range(number+1):
        total = total + natural_sum
    return total

# returns the sum of the cubes of the first natural numbers up to the provided integer
def sum_n_cubes(number):
    total = 0
    for natural_cube in range(number+1):
        total = total + (natural_cube ** 3)
    return total

# encodes a message to using a second message to generate a key
def encode_better():
    message_better = input('enter a message: ')
    key_better = input('enter a key: ')
    cipher_better = []
    result = []
    for message in range(len(message_better) - len(key_better)):
        key_better = key_better + (key_better[message % len(key_better)])
    for letter in range(len(message_better)):
        encode_better = ((ord(message_better[letter])-65) + (ord(key_better[letter])-65)) % 58
        encode_better = encode_better + ord('A')
        cipher_better.append(encode_better)
    for number in range(len(cipher_better)):
        decode_better = chr(cipher_better[number])
        result.append(decode_better)
    result_better = ''.join(result)
    print(result_better)


if __name__ == '__main__':
    # cash_converter()
    # encode()
    # res = sphere_area(13)
    # print(res)
    # res = sphere_volume(13)
    # print(res)
    # res = sum_n(100)
    # print(res)
    # res = sum_n_cubes(13)
    # print(res)
    # encode_better()
    pass
