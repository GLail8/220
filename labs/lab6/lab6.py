"""
Garrett Lail
lab6.py
Solved cipher code for lab 6

This lab is entirely my own work
"""
from graphics import GraphWin, Text, Point, Entry, Rectangle

def vigenere():
    #this creates the graphic window, text objects, entry objects, and the 'encode' button
    vig_win = GraphWin('Vigenere', 800, 600)
    code_message = Text(Point(200, 100), 'Message to code:')
    code_entry = Entry(Point(500, 100), 40)
    keyword_message = Text(Point(200, 200), 'Enter Keyword:')
    keyword_entry = Entry(Point(415, 200), 20)
    code_message.draw(vig_win)
    code_entry.draw(vig_win)
    keyword_message.draw(vig_win)
    keyword_entry.draw(vig_win)
    box = Rectangle(Point(350, 275), Point(450, 325))
    encode_text = Text(Point(400, 300), 'Encode')
    box.draw(vig_win)
    encode_text.draw(vig_win)

    #this undraws the encode button after a user has input text into the entry objects
    vig_win.getMouse()
    box.undraw()
    encode_text.undraw()

    #this code gets the text and puts it in readable form for my cipher
    code = code_entry.getText()
    code = code.replace(' ', '')
    code = code.upper()
    keyword = keyword_entry.getText()
    keyword = keyword.replace(' ', '')
    keyword = keyword.upper()

    #this lengthens the keyword to the length of the message
    #making it a readable form for the cipher code
    keyword = list(keyword)
    for i in range(len(code) - len(keyword)):
        keyword.append(keyword[i % len(keyword)])

    #encrypts each letter of the message using vigenere cipher
    vigenere_cipher = []
    for j in range(len(code)):
        encrypt = (ord(code[j]) + ord(keyword[j])) % 26
        encrypt = encrypt + ord('A')
        vigenere_cipher.append(encrypt)

    #translates the encrypted message into characters
    result = []
    for k in range(len(vigenere_cipher)):
        decrypt = chr(vigenere_cipher[k])
        result.append(decrypt)
    vigenere_result = ''.join(result)

    #displays the resulting message in the window
    #and prompts the user to close the window
    result_message = Text(Point(400, 300), 'Resulting Message')
    result_text = Text(Point(400, 325), vigenere_result)
    close_text = Text(Point(400, 500), 'Click Anywhere to Close Window')
    result_message.draw(vig_win)
    result_text.draw(vig_win)
    close_text.draw(vig_win)

    vig_win.getMouse()
    vig_win.close()

