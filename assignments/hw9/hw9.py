"""
Garrett Lail
hw9.py
I certify this assignment is my own work
"""
from random import randint
from graphics import GraphWin, Line, Circle, Text, Entry, Point

def get_words(file_name):
    file = open(file_name, 'r')
    return file.readlines()

def get_random_word(words):
    random = randint(0, len(words)-1)
    random_word = words[random]
    return random_word

def letter_in_secret_word(letter, secret_word):
    if secret_word.count(letter) >= 1:
        return True
    else:
        return False

def already_guessed(letter, guesses):
    if guesses.count(letter) >= 1:
        return True
    else:
        return False

def make_hidden_word(secret_word, guesses):
    blanks = '_' * (len(secret_word) - 1)
    for i in range(len(secret_word)):
        if secret_word[i] in guesses:
            blanks = blanks[:i] + secret_word[i] + blanks[i + 1:]
    return ' '.join(blanks)

def won(guessed):
    if guessed.count('_') == 0:
        return True
    else:
        return False

def play_command_line(secret_word):
    guessed_letters = []
    remaining_guesses = 6
    guessed = make_hidden_word(secret_word, guessed_letters)

    win = GraphWin('hangman', 800, 800)
    gallow1 = Line(Point(400, 200), Point(400, 600))
    gallow2 = Line(Point(250, 200), Point(400, 200))
    gallow3 = Line(Point(250, 600), Point(450, 600))
    gallow4 = Line(Point(250, 200), Point(250, 250))
    gallow1.draw(win)
    gallow2.draw(win)
    gallow3.draw(win)
    gallow4.draw(win)

    guesses_text = Text(Point(200, 100), 'Guessed Letters:')
    guesses_list = Text(Point(400, 100), guessed_letters)
    guesses_text.draw(win)
    guesses_list.draw(win)

    guessed_text = Text(Point(400, 700), guessed)
    guess_letter_txt = Text(Point(300, 750), 'Guess a letter:')
    guess_letter = Entry(Point(400, 750), 1)
    guessed_text.draw(win)
    guess_letter_txt.draw(win)
    guess_letter.draw(win)

    head = Circle(Point(250, 300), 50)
    body = Line(Point(250, 350), Point(250, 500))
    arm1 = Line(Point(250, 400), Point(300, 450))
    arm2 = Line(Point(250, 400), Point(200, 450))
    leg1 = Line(Point(250, 500), Point(300, 550))
    leg2 = Line(Point(250, 500), Point(200, 550))
    index = 0
    body_parts = [head, body, leg1, leg2, arm1, arm2]

    win_txt = Text(Point(600, 400), 'Winner!')
    lose_txt = Text(Point(600, 400), 'Sorry, you did not win, the word was:')
    secret_text = Text(Point(600, 450), secret_word)


    while not won(guessed) and remaining_guesses > 0:
#        print('already guessed: ', guessed_letters)
#        print('guesses remaining: ', remaining_guesses)
#        print(guessed)
#        letter = input('guess a letter: ')
        win.getKey()
        letter = guess_letter.getText()
        guess_letter.setText('')
        if not already_guessed(letter, guessed_letters):
            guessed_letters.append(letter)
            guesses_list.setText(guessed_letters)
            if letter in secret_word:
                guessed = make_hidden_word(secret_word, guessed_letters)
                guessed_text.setText(guessed)
            else:
                remaining_guesses = remaining_guesses - 1
                body_parts[index].draw(win)
                index = index + 1
    if won(guessed):
        guess_letter.undraw()
        guess_letter_txt.undraw()
        win_txt.draw(win)
        secret_text.draw(win)
#        print('winner!')
#        print(secret_word)
    else:
        guess_letter.undraw()
        guess_letter_txt.undraw()
        lose_txt.draw(win)
        secret_text.draw(win)
#        print('sorry, you did not guess the word.')
#        print('the secret word was {}'.format(secret_word))

    win.getMouse()
    win.close()

