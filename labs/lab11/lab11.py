"""
Garrett Lail
lab11.py

I certify this lab is my work
"""

from lab10.Button import Button
from lab10.Door import Door
from random import randint
from graphics import GraphWin, Text, Rectangle, Point

def three_door_game():
    win = GraphWin('Three Door Game', 800, 800)
    win.setBackground('light blue')

    wins_box = Rectangle(Point(50, 50), Point(100, 100))
    wins_counter = Text(wins_box.getCenter(), '0')
    loss_box = Rectangle(Point(100, 50), Point(150, 100))
    loss_counter = Text(loss_box.getCenter(), '0')
    wins_box.draw(win)
    wins_counter.draw(win)
    loss_box.draw(win)
    loss_counter.draw(win)

    game_text = Text(Point(400, 200), 'I have a secret door')
    instruction_text = Text(Point(400, 700), 'Click to guess which is the secret door')
    game_text.draw(win)
    instruction_text.draw(win)

    quit_button = Button(Rectangle(Point(600, 50), Point(750, 150)), 'Quit')
    quit_button.draw(win)

    door1 = Door(Rectangle(Point(50, 300), Point(250, 600)), 'Door 1')
    door2 = Door(Rectangle(Point(300, 300), Point(500, 600)), 'Door 2')
    door3 = Door(Rectangle(Point(550, 300), Point(750, 600)), 'Door 3')
    door1.draw(win)
    door2.draw(win)
    door3.draw(win)
    door1.close('brown', 'Door 1')
    door2.close('brown', 'Door 2')
    door3.close('brown', 'Door 3')

    door_list = [door1, door2, door3]
    click = win.getMouse()
    while not quit_button.is_clicked(click):
        door1.close('brown', 'Door 1')
        door2.close('brown', 'Door 2')
        door3.close('brown', 'Door 3')
        game_text.setText('I have a secret door')
        instruction_text.setText('click to guess which is the secret door!')
        secret_door = door_list[randint(0, 2)]
        secret_door.set_secret(True)
        click = win.getMouse()
        if door1.is_clicked(click):
            if door1.is_secret():
                door1.open('green', 'Door 1')
                game_text.setText('you win!')
                instruction_text.setText('click anywhere to play again')
                win_count = eval(wins_counter.getText()) + 1
                wins_counter.setText(str(win_count))
                click = win.getMouse()

            else:
                door1.open('red', 'Door 1')
                secret_door.open('green', str(secret_door.get_label()))
                game_text.setText('sorry, incorrect!')
                instruction_text.setText('click anywhere to play again')
                loss_count = eval(loss_counter.getText()) + 1
                loss_counter.setText(str(loss_count))
                click = win.getMouse()

        elif door2.is_clicked(click):
            if door2.is_secret():
                door2.open('green', 'Door 2')
                game_text.setText('you win!')
                instruction_text.setText('click anywhere to play again')
                win_count = eval(wins_counter.getText()) + 1
                wins_counter.setText(str(win_count))
                click = win.getMouse()

            else:
                door2.open('red', 'Door 2')
                secret_door.open('green', str(secret_door.get_label()))
                game_text.setText('sorry, incorrect!')
                instruction_text.setText('click anywhere to play again')
                loss_count = eval(loss_counter.getText()) + 1
                loss_counter.setText(str(loss_count))
                click = win.getMouse()

        elif door3.is_clicked(click):
            if door3.is_secret():
                door3.open('green', 'Door 3')
                game_text.setText('you win!')
                instruction_text.setText('click anywhere to play again')
                win_count = eval(wins_counter.getText()) + 1
                wins_counter.setText(str(win_count))
                click = win.getMouse()

            else:
                door3.open('red', 'Door 3')
                secret_door.open('green', str(secret_door.get_label()))
                game_text.setText('sorry, incorrect!')
                instruction_text.setText('click anywhere to play again')
                loss_count = eval(loss_counter.getText()) + 1
                loss_counter.setText(str(loss_count))
                click = win.getMouse()
        secret_door.set_secret(False)
    win.close()

three_door_game()


