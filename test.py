# Import necessary libraries
import numpy as np
from keras.models import Sequential
from keras.layers import Dense, Dropout

# Define the game board
board = np.zeros((3, 3))

# Define the dataset
X_train = []
y_train = []


# Simulate games and create the dataset
def play_game():
    global board
    global X_train
    global y_train

    # Start a new game
    board = np.zeros((3, 3))
    player = 1

    # Play until the game is over
    while True:
        # Generate the game state
        state = board.reshape(9)

        # Generate the optimal move
        optimal_move = np.random.choice(np.where(state == 0)[0])

        # Add the game state and optimal move to the dataset
        X_train.append(state)
        y_train.append(optimal_move)

        # Make the move
        row = optimal_move // 3
        col = optimal_move % 3
        board[row][col] = player

        # Check if the game is over
        if check_win() != 0:
            break

        # Switch to the other player
        player = 3 - player


# Check if there is a winner
def check_win():
    global board

    # Check rows
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2] != 0:
            return board[row][0]

    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != 0:
            return board[0][col]

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != 0:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != 0:
        return board[0][2]

    # Check for a tie
    if np.all(board != 0):
        return -1

    # No winner yet
    return 0


# Simulate many games to create the dataset
for i in range(100000):
    play_game