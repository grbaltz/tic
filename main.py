# Simple Tic Tac Toe game with plans to make it goofy
# By Garrett Baltz
import numpy as np

np.random.seed(10072001)

def create_board(size):
    board = np.full((size, size), '_')

    return board

def show_board(board):
    for row in range(len(board)):
        print(board[row])

# Checks board state to see if there is a win
def check_win(board, markers, win_size):
    win = False
    winner = ''
    
    # Rows nontransposed
    for row in board:
        row = list(row)
        if row.count(markers[0]) == len(row):
            win = True
            winner = markers[0]
            return win, winner
        elif row.count(markers[1]) == len(row):
            win = True
            winner = markers[1]
            return win, winner
        
    # Rows transposed
    for row in np.transpose(board):
        row = list(row)
        if row.count(markers[0]) == len(row):
            win = True
            winner = markers[0]
            return win, winner
        elif row.count(markers[1]) == len(row):
            win = True
            winner = markers[1]
            return win, winner
        
    # Diagonals
    diag = list(np.diag(board))
    if diag.count(markers[0]) == len(diag):
        win = True
        winner = diag[0]
        return win, winner
    
    tdiag = list(np.diag(np.transpose(board)))
    if tdiag.count(markers[0]) == len(tdiag):
        win = True
        winner = tdiag[0]
        return win, winner
    
    return win, winner

# Check if a win is possible
def check_cat(board, markers):
    # Check if any spots available
    for row in board:
        if '_' in row:
            return False
    
    return True

def play_again():
    res = input("Would you like to play again? (y/n)")
    if res.lower == 'y' or res.lower == 'yes' or res.lower == 'yeah' or res.lower == 'ye':
        play_tic(board=board, win_size=win_size)

# Play state, rotates through players until win or cat's game
def play_tic(board, win_size):

    print("PLAY TIC-TAC-TOE!")
    p1 = input("Player 1: Enter piece marker -> ")
    p2 = input("Player 2: Enter piece marker -> ")
    markers = [p1, p2]

    print("Randomly choosing first player...")

    pnum = np.random.randint(-1, 1)

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

# run game
size = 3 # Change me for different board sizes
win_size = 3 # Change me for length of win (in a row)
board = create_board(size)
show_board(board)
play_tic(board, win_size)