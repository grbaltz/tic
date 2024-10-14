# Simple Tic Tac Toe game with plans to make it goofy
# By Garrett Baltz
import numpy as np
import random

np.random.seed(10072001)

def create_board(size):
    board = np.full((size, size), '_')

    return board

def show_board(board):
    for row in range(len(board)):
        print(board[row])

# Generator to get all sublists from a list
def get_sublist(line, size):
    i = 0
    length = len(line)
    while i <= length - size:
        yield line[i:i+size]
        i += 1

# Gets every possible sublist of a certain size of a board 
def get_all_sublists(board, win_size):
    wsublists = []

    # all sublists of rows
    for row in board:
        wsublists.append(get_sublist(row, win_size))

    # all sublists of columns
    tboard = np.transpose(board)
    for col in tboard.tolist():
        wsublists.append(get_sublist(col, win_size))

    wsublists.append(get_diags(np.array(board), win_size))

    sublists = []
    for l in wsublists:
        for l2 in list(l):
            sublists.append(list(l2))
    
    return sublists


# Checks board state to see if there is a win
def check_win(board, markers, win_size):
    win = False
    winner = ''
    sublists = get_all_sublists(board, win_size)
    
    for line in sublists:
        if line.count(markers[0]) == win_size:
            win = True
            winner = markers[0]
            break
        if line.count(markers[1]) == win_size:
            win = True
            winner = markers[1]
            break

    return win, winner

def get_diags(board, size):
    if size > board.shape[0]:
        raise ValueError(f'Cant get size {size} rows, board is {board.shape}')
    
    # all sublists of diagonals
    for d in range(-size, size + 1):
        yield from get_sublist(np.diag(board, d).tolist(), size)

    # all sublists of flipped diagonals
    for d in range(-size, size + 1):
        yield from get_sublist(np.diag(np.fliplr(board), d).tolist(), size)



# Check if a win is possible
def check_cat(board, markers):
    # Check if any spots available
    for row in board:
        if '_' in row:
            return False
    
    return True

def play_again(board, win_size):
    res = input("Would you like to play again? (y/n) ")
    print(res.lower())
    if res.lower() == 'y' or res.lower() == 'yes' or res.lower() == 'yeah' or res.lower() == 'ye':
        print("Play Again")
        play_tic()

# Play state, rotates through players until win or cat's game
def play_tic():

    print("PLAY TIC-TAC-TOE!")
    # run game
    while True:
        try:
            size = int(input("How big of a board? (x) ")) # Change me for different board sizes
            win_size = int(input("How many in a row to win? (x) ")) # Change me for length of win (in a row)
            board=create_board(size)
            show_board(board)
            break
        except:
            print("Please enter a number, not a string")

    p1 = input("Player 1: Enter piece marker -> ")
    p2 = input("Player 2: Enter piece marker -> ")
    markers = [p1, p2]

    print("Randomly choosing first player...")

    pnum = random.choice([-1, 1])
    print(pnum)

    win, _ = check_win(board, markers, win_size)
    
    # print(win)

    while not win:
        player = 1 if pnum == -1 else 2
        loc_in = input(f"Player {player}'s turn, type target location in form 'row, column' -> ")
        try:
            loc = [int(x.strip()) for x in loc_in.split(',')]
        except:
            print("Invalid input, try again.")
            continue
        print(loc)
        if board[loc[0]][loc[1]] == '_':
            board[loc[0]][loc[1]] = p1 if player == 1 else p2
        else:
            print("Invalid move, try again.")
            continue
        show_board(board)

        win, _ = check_win(board, markers, win_size)
        if check_cat(board, markers):
            print("Cat's game!")
            play_again(board, win_size)
            exit()
        pnum *= -1
    
    _, x = check_win(board, markers, win_size)
    if x == p1:
        winner = 1
    else:
        winner = 2
    
    print(f"Player {winner} Wins!")
    play_again(board, win_size)

# Play state, rotates through players until win or cat's game
def test_tic(board, win_size=3, filled=False):

    print("PLAY TIC-TAC-TOE!")
    show_board(board)
    p1 = 'x'
    p2 = 'o'
    markers = [p1, p2]

    # print("Randomly choosing first player...")

    pnum = np.random.randint(-1, 1)

    win, winner = check_win(board, markers, win_size)

    print(win, winner)
    
    if filled:
        exit()

    # print(win)

    while not win:
        player = 1 if pnum == -1 else 2
        loc_in = input(f"Player {player}'s turn, type target location in form 'row, column' -> ")
        try:
            loc = [int(x.strip()) for x in loc_in.split(',')]
        except:
            print("Invalid input, try again.")
            continue
        print(loc)
        if board[loc[0]][loc[1]] == '_':
            board[loc[0]][loc[1]] = p1 if player == 1 else p2
        else:
            print("Invalid move, try again.")
            continue
        show_board(board)

        win, _ = check_win(board, markers, win_size)
        if check_cat(board, markers):
            print("Cat's game!")
            play_again()
            exit()
        pnum *= -1
    
    _, x = check_win(board, markers, win_size)
    if x == p1:
        winner = 1
    else:
        winner = 2
    
    print(f"Player {winner} Wins!")
    play_again()

play_tic()

brd3 = [['x', 'o', 'x'],
       ['x', 'x', 'o'],
       ['x', 'o', 'x']]

brd4 = [['x', 'o', 'x', 'o'],
       ['x', 'x', 'o', 'x'],
       ['x', 'o', 'x', 'x'],
       ['x', 'o', 'x', 'x']]

# test_tic(brd4, 3, filled=True)