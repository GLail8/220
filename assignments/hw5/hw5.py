"""
Garrett Lail
hw5.py
Certification of Authenticity:
This assignment was entirely completed by me
"""

#reverses the users name to last name, first name order
def name_reverse():
    reverse = input('enter a name (first last): ')
    name_list = reverse.split()
    print(name_list[1], name_list[0], sep=", ")

#takes the company name out of a domain name
def company_name():
    company = input('enter a domain: ')
    company_list = company.split(".")
    print(company_list[1])

#takes the initials for each name that is input
def initials():
    students = eval(input('how many students are in the class? '))
    for i in range(students):
        student_name = input('what is the name of student {}?'.format(i+1))
        name_split = student_name.split()
        print((name_split[0])[0] + (name_split[1])[0])

#takes the initials from a list of names
def names():
    name_list = input('enter a list of names: ')
    names_list = name_list.split()
    for l in range(int(len(names_list)/2)):
        firstindex = (names_list[l*2])[0]
        lastindex = (names_list[l*2+1])[0]
        print(firstindex + lastindex, end=" ")

#outputs every third letter of each sentence a user inputs
def thirds():
    sentence_number = eval(input('enter the number of sentences: '))
    sentence_list = []
    for j in range(sentence_number):
        sentence = input('enter sentence {}: '.format(j+1))
        sentence_list.append(sentence)
    for k in range(sentence_number):
        print((sentence_list[k])[::3])

#takes the average word length of a sentence
def word_average():
    average_sentence = input('enter a sentence: ')
    average_split = average_sentence.split()
    average_replace = average_sentence.replace(" ", "")
    average = len(average_replace) / len(average_split)
    print(average)

#translates a sentence into pig latin
def pig_latin():
    latin = input('enter a sentence to convert to pig latin: ')
    latin_split = latin.split()
    pig_latin = ""
    for m in range(len(latin_split)):
        remove = (latin_split[m])[1:]
        end = remove + (latin_split[m])[0]
        ay = end + 'ay'
        pig_latin = pig_latin + ay + " "
    print(pig_latin.lower())

if __name__ == '__main__':
    # name_reverse()
    # company_name()
    # initials()
    # names()
    # thirds()
    # word_average()
    # pig_latin()
    pass
