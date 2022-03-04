"""
Name: Garrett Lail
hw7.py

Problem: <Brief, one or two sentence description of the problem that this program solves, in your own words.>

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


def number_words(in_file_name, out_file_name):
    words = open(in_file_name, 'r')
    numbered_words = open(out_file_name, 'w')
    word_list = (words.read()).split()
    for i in range(len(word_list)):
        print(i+1, word_list[i], file=numbered_words)

def hourly_wages(in_file_name, out_file_name):
    employee_list = open(in_file_name, 'r')
    raise_list = open(out_file_name, 'w')
    for line in employee_list.readlines():
        list = line.split()
        firstname = list[0]
        lastname = list[1]
        wage_raise = (eval(list[2]) + 1.65) * eval(list[3])
        print(firstname, lastname, '{:.2f}'.format(wage_raise), file=raise_list)

def calc_check_sum(isbn):
    isbn_digits = isbn.replace('-', '')
    check = 10
    sum = 0
    for j in range(len(isbn_digits)):
        checksum = eval(isbn_digits[j]) * (check - j)
        sum = sum + checksum
    print(sum)

def send_message(file_name, friend_name):
    message = open(file_name, 'r')
    friend_file = friend_name + '.txt'
    friend = open(friend_file, 'w')
    for line in message:
        line_strip = line.rstrip('\n')
        print(line_strip, file=friend)
    message.close()


# key is a number
def encode(message, key):
    cipher = ''
    for letter in range(len(message)):
        encode = ord(message[letter]) + key
        decode = chr(encode)
        cipher = cipher + decode
    return cipher

def send_safe_message(file_name, friend_name, key):
    message_file = open(file_name, 'r')
    friend_file = friend_name + '.txt'
    friend = open(friend_file, 'w')
    message_str = (message_file.read()).replace('\n', ' ')
    safe_message = encode(message_str.upper(), key)
    print(safe_message, file=friend)

def encode_better(message_better, key_better):
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
    return result_better

def send_uncrackable_message(file_name, friend_name, pad_file_name):
    better_message = open(file_name, 'r')
    better_key = open(pad_file_name, 'r')
    friend_file = friend_name + '.txt'
    better_friend = open(friend_file, 'w')
    read_message = better_message.read()
    read_key = better_key.read()
    uncrackable_message = encode_better(read_message, read_key)
    print(uncrackable_message, file=better_friend)

if __name__ == '__main__':
    pass
