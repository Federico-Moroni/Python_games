'''
First we will define our game logic. What do we need?

Board
    Display board
Play game
    Handle turn
Check win
    Check rows
    Check columns
    Check diagonals
Check tie
    If board full and check win false then tie
Flip player

'''
# ------ START BOARD ------

board = ["-","-","-","-","-","-","-","-","-",]

def display_board():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])

# ------ END BOARD ------

# ------ PLAY GAME ------

# GLOBAL VARIABLES
game_still_going = True
winner = None
# Player X always start
current_player = "X"

def play_game():

    # Display inital board
    display_board()

    while game_still_going:

        # Handle a single turn of an arbitrary player
        handle_turn(current_player)

        # Check if the game has ended
        check_if_game_over()

        # Flip to the other player
        flip_player()

    # The game has ended
    if winner == "X" or winner == "O":
        print(winner + " player won!")

    elif winner == None:
        print("Tie!")

# ------ END GAME ------

# ------ START FUNCTIONS ------

def handle_turn(player):

    print(player + " 's turn")

    # I will substruct 1 to the positon chosen so it matches with the index. Example: Position 1 has index 0. 
    position = input("Choose a position from 1 to 9: ")

    valid = False
    while not valid:

        # Here we are going to allow only integers from 1 to 9 so the, position is parsed to int and substract -1.
        while position not in ["1","2","3","4","5","6","7","8","9"]:
            position = input("Please insert a number between 1 and 9: ")

        position = int(position) - 1

        if board[position] == "-":
            valid = True
        else:
            print("\nYou can't use that space! Choose another one")

    board[position] = player

    display_board()

def check_if_game_over():
    check_for_winner()
    check_if_tie()

def check_for_winner():

    # Setting up global variables
    global winner

    #Check rows
    row_winner = check_rows()
    #Check columns
    column_winner = check_columns()
    #Check diagonals
    diagonal_winner = check_diagonals()

    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        #No winner
        winner = None
    return

# By returning the board[i] that is part of the row, col or diag that won, we will know if it was X or O.
def check_rows():

    # Setting up global variables
    global game_still_going

    # Check if any of the rows have the same value
    row_1 = board[0]  == board[1] == board[2] != "-"
    row_2 = board[3]  == board[4] == board[5] != "-"
    row_3 = board[6]  == board[7] == board[8] != "-"

    # If any of the roads are True, then there is a winner and this will return X or O.
    if row_1 or row_2 or row_3:
        game_still_going = False
    if row_1:
        return board[0]
    if row_2:
        return board[3]
    if row_3:
        return board[6]
    return

def check_columns():
    # Setting up global variables
    global game_still_going

    # Check if any of the rows have the same value
    column_1 = board[0] == board[3] == board[6] != "-"
    column_2 = board[1] == board[4] == board[7] != "-"
    column_3 = board[2] == board[5] == board[8] != "-"

    # If any of the roads are True, then there is a winner and this will return X or O.
    if column_1 or column_2 or column_3:
        game_still_going = False
    if column_1:
        return board[0]
    if column_2:
        return board[1]
    if column_3:
        return board[2]
    return

def check_diagonals():
    # Setting up global variables
    global game_still_going

    # Check if any of the rows have the same value
    diagonal_1 = board[0] == board[4] == board[8] != "-"
    diagonal_2 = board[2] == board[4] == board[6] != "-"

    # If any of the roads are True, then there is a winner and this will return X or O.
    if diagonal_1 or diagonal_2:
        game_still_going = False
    if diagonal_1:
        return board[0]
    if diagonal_2:
        return board[2]
    return

def check_if_tie():

    global game_still_going

    if "-" not in board:
        game_still_going = False
    return

def flip_player():

    # This is starting with a default player X. No when the function is called after function check_if_game_over() and it returns
    global current_player
    
    if current_player == "X":
        current_player = "O"

    elif current_player == "O":
        current_player = "X"

    return current_player

# ------ END FUNCTIONS ------

play_game()

