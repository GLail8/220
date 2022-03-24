"""
Garrett Lail
lab9.py

I certify this lab is entirely my own work
"""

def build_board():
    list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    return list

def fill_spot(board, position, shape):
    board[position-1] = shape

def is_legal(board, position):
    if str(board[position-1]).isnumeric():
        return True
    else:
        return False

def game_is_won(board):
    if board[0] == board[1] == board[2]:
        return True
    elif board[3] == board[4] == board[5]:
        return True
    elif board[6] == board[7] == board[8]:
        return True
    elif board[0] == board[3] == board[6]:
        return True
    elif board[1] == board[4] == board[7]:
        return True
    elif board[2] == board[5] == board[8]:
        return True
    elif board[0] == board[4] == board[8]:
        return True
    elif board[2] == board[4] == board[6]:
        return True
    else:
        return False

def game_over(board):
    no_moves = []
    for i in range(len(board)):
        numeric = str(board[i]).isnumeric()
        no_moves.append(numeric)
    if game_is_won(board) == True:
        return True
    elif no_moves.count(False) == 9:
        return True
    else:
        return False

def get_winner(board):
    if board.count('X') > board.count('O'):
        return 'x'
    elif board.count('O') == board.count('X'):
        return 'o'
    else:
        return None

def play():
    print('This is a class game of tictactoe. The two players alternate, starting with X, '
          'inputting the number on the board to replace with their shape. The player who'
          'gets three of their shapes in a row wins.')
    board = build_board()
    user_input = 'y'
    while user_input[0] == 'y':
        print('\t', board[0], '|', board[1], '|', board[2], '\n', '\t-----------', '\n',
              '\t', board[3], '|', board[4], '|', board[5], '\n', '\t-----------', '\n',
              '\t', board[6], '|', board[7], '|', board[8])
        while game_over(board) == False:
            x_input = eval(input("X's turn, choose a position: "))
            if is_legal(board, x_input):
                fill_spot(board, x_input, 'X')
                print('\t', board[0], '|', board[1], '|', board[2], '\n', '\t-----------', '\n',
                      '\t', board[3], '|', board[4], '|', board[5], '\n', '\t-----------', '\n',
                      '\t', board[6], '|', board[7], '|', board[8])
                o_input = eval(input("O's turn, chose a position: "))
                if is_legal(board, o_input):
                    fill_spot(board, o_input, 'O')
                    print('\t', board[0], '|', board[1], '|', board[2], '\n', '\t-----------', '\n',
                          '\t', board[3], '|', board[4], '|', board[5], '\n', '\t-----------', '\n',
                          '\t', board[6], '|', board[7], '|', board[8])
                else:
                    print('That is not a legal move, pick another one')
                    o_input = eval(input("O's turn, choose a position: "))
                    fill_spot(board, o_input, 'O')
                    print('\t', board[0], '|', board[1], '|', board[2], '\n', '\t-----------', '\n',
                          '\t', board[3], '|', board[4], '|', board[5], '\n', '\t-----------', '\n',
                          '\t', board[6], '|', board[7], '|', board[8])
            else:
                print('That is not a legal move, pick another one')
                x_input = eval(input("X's turn, choose a position: "))
                fill_spot(board, x_input, 'X')
                print('\t', board[0], '|', board[1], '|', board[2], '\n', '\t-----------', '\n',
                      '\t', board[3], '|', board[4], '|', board[5], '\n', '\t-----------', '\n',
                      '\t', board[6], '|', board[7], '|', board[8])
        print("{}'s win!".format(get_winner(board)))
        user_input = input("play again? (y or yes to continue)")
        board = build_board()