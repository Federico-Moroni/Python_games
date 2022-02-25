from player import Human_player, Random_computer_player
import time

# ----- GAME CLASS START -----

class Tictactoe:

    def __init__(self):
        self.board = [' ' for _ in range(9)] # for _ in range(9): Basically it means you are not interested in how many times the loop is run till now, just that it should run some specific number of times overall. I'm not using for i in some list.. just run the loop and fill with a space ' ' the "board" that will be a list from 0 to 8. 
        self.current_winner = None # This variable will keep track if there is or not a winner. We initialize it with None value and after there is a winner, the value will be true and the while loop in the game function will break and return the winner.

# ----- STATIC METHOD START -----

    @staticmethod # This is a static method because it doesn't relate to any specific board. We don't need to pass in a self. There is only one board. Static methods in Python are extremely similar to python class level methods, the difference being that a static method is bound to a class rather than the objects for that class. This means that a static method can be called without an object for that class.

    def print_board_nums():
        # This is going to be used to show only the first time the board and the numbers for each position. 
        number_board = [[str(i) for i in range(j * 3, (j + 1) * 3)] for j in range(3)] # str() will convert converts values to a string form so they can be combined with other strings. I do this because I don't want to be printing a int into my board.. just a string representation of the value. 
        # str(i) This will print the numbers in my board so its easier to pick a square when playing. If I use [['-' for i in range(j * 4, (j + 1) * 4)] for j in range(4)] this will generate a 4x4 board. And if I use [['-' for i in range(j * 4, (j + 1) * 4)] for j in range(3)] it will generate a 3x4 range with '-' instead of i. 
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')

# ----- STATIC METHOD END -----

# ----- CLASS METHODS START -----

    # Now, we need to create a method to print the board.
    def print_board(self):
        # This is going to be used to print the board after each time a player makes a move. 
        for row in [self.board[i * 3 : (i + 1) * 3] for i in range (3)]: # So i * 3 is the quantity of rows and i in range(3) is quantity of columns.
            '''
            0 3   The upper formula is doing this: Creating 3 lines that will have the next index numbers [0,1,2]               
            3 6                                                                                           [3,4,5]               
            6 9                                                                                           [6,7,8]               

            If I want to have 16 places I should use the following formula: for row in [board[i * 4 : (i + 1) * 4] for i in range (4)]. Always remind you need a 16 item list for this. So in self.board = [' ' for _ in range(16)]

            [0 , 1 , 2 , 3 ]
            [4 , 5 , 6 , 7 ]
            [9 , 10, 11, 12]
            [13, 14, 15, 16]
            '''
            print('| ' + ' | '.join(row) + ' |') # In this formula, the first and last | are strings.. nothing to say. But ' | '.join(row) is saying to join the rows and use ' | ' as the separator. So, I could just do this to remove left and right borders from the board: print(' | '.join(row))


    def available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == ' '] # This is going to loop over the board and search one by one which spots are available. An available spot will match with spot == ' '. At last, it's going to return i positions that are available. 
        # for (i, spot) in enumerate(self.board): # Lets you write Pythonic for loops when you need a count and the value from an iterable. The big advantage of enumerate() is that it returns a tuple with the counter and value, so you don't have to increment the counter yourself. So an example would be ['x', 'x', 'o'] ==> [(0,'x'), (1,'o'), (2,'o')]. In this for loop we are going through each of these tuples assigning the 1st item to i and 2nd to spot.


    def empty_squares(self):
        return ' ' in self.board # This will return a boolean. If there is an empty space it will return True, if not, False. We are going to use this one to evaluate the while in play() function. If it's false, the while loop will break and will return that it's a tie. 


    def make_move(self, square, letter):
        # We need the return output from get_move (it's in player.py as a class method for each player) that will return the square chosen that will recieve this function as parameter. When we have the square parameter, know we know where the player wants to move at.
        # The letter we need it to know which player is making the move. So we will know which letter (player) wants to move to which square.
        # We know the move will be valid because in get_move we've already evaluated this. So, we make the move and return True. If not, then we return False.
        # We also need to check if somebody won. We only win AFTER we make a move and then, we can toggle current_winner to the winner if there is one. 
        if self.board[square] == ' ':
            self.board[square] = letter # This is where the blank square is replaced with the letter of the player playing. 
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False


    def winner(self, square, letter):
        # We need to check if there is a winner. So check if row, column or diagonal has 3 equal values of the letter playing. 

        # Row check
        row_ind = square // 3 # Make this calc. and you will see this works! It will give me the row index 0, 1 or 2
        row = self.board[row_ind * 3 : (row_ind + 1) * 3] # This will return the row where the player placed it's square. This calculation is going to look for the complete board and  will return the first, second or third row [0:3] [3:6] [6:9]. Then we will evaluate if that row has the same values (values = letter) tocheck if the player won. 
        if all([squares == letter for squares in row]): # We are checking if all are equal
            return True

        # Column check
        col_ind = square % 3 # Make this calc. and you will see this works! It will give me the column index 0, 1 or 2.
        col = [self.board[col_ind + i * 3] for i in range(3)] # We look up for the column where the player placed its square and then look if it won. 
        if all([squares == letter for squares in col]): # We are checking if all are equal
            return True

        # Diagonal Check
        if square % 2 == 0: # All squares in diagonals are even index numbers. So square % 2 == 0. 
            diagonal1 = [self.board[i] for i in [0,4,8]] # Left to right diagonal.
            if all ([squares == letter for squares in diagonal1]): # We are checking if all are equal
                return True
            diagonal2 = [self.board[i] for i in [2,4,6]] # Right to left diagonal. 
            if all ([squares == letter for squares in diagonal2]): # We are checking if all are equal
                return True
        return False # If all the checks above fail, then we don't have a winner and we return false. 

# ----- CLASS METHODS END -----

# ----- GAME CLASS END -----

# ----- PLAY() FUNCTION START -----

def play(game, x_player, o_player, print_game = True):
    if print_game: # We will show this board with all numbers only when the game starts. 
        game.print_board_nums()


    letter = 'X' # It will start with this letter just because.
    # Now we are going to do this iterate while the game still has empty squares.
    # We don't have to worry about the winner because we'll just return that and the loop will break.


    while game.empty_squares(): # empty_squares() will return True or False.
        # We want to get the move from the appropiate player.
        if letter == 'O':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)


        # Let's define a function to make a move.
        if game.make_move(square, letter):
            if print_game:
                print(letter + f' makes a move to square {square}')
                game.print_board() # We want to se how the board is after the move
                print('') # Just print an empty line

            if game.current_winner:
                if print_game:
                    print(letter + ' Wins!')
                return letter

            # After we make the move, we need to alternate letter
            letter = 'O' if letter == 'X' else 'X' #We assign letter to O if the letter was X, otherwise, we assign it to X


        # Break after every move
        time.sleep(0.8)

    if print_game:
        print('It\'s a tie!')

# ----- PLAY() FUNCTION END -----

if __name__ == '__main__':
    x_player = Human_player('X') # Instantiate human player
    o_player = Random_computer_player('O') # Instantiate computer player
    t = Tictactoe() # Game initialization 
    play(t, x_player, o_player, print_game=True)