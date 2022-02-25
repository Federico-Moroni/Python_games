from multiprocessing.sharedctypes import Value
import random

# First, I'm going to create a parent class that will receive a letter parameter (X or O).

class Player():
    def __init__(self, letter): # The __init__ method lets the class initialize the object's attributes and serves no other purpose.
        self.letter = letter

# Now, we are going to create 2 more classes using inheritance. A random computer player and a human player. 

class Random_computer_player(Player):
    def __init__(self, letter):
        super().__init__(letter) # This is going to call the initialization in the super class (Player) receiving the letter as a parameter.

    def get_move(self, game): 
        # We are going to choose a random spot for the computer player
        square = random.choice(game.available_moves()) # This is going to choose randomly over the available spots returned by function available_moves()
        return square

class Human_player(Player):
    def __init__(self, letter):
        super().__init__(letter) # This is going to call the initialization in the super class (Player).

    def get_move(self, game):
        valid_square = False
        square = None
        while not valid_square:
            square_attemp = input(self.letter + '\'s turn. Choose (0 - 8): ')
            try:
                square = int(square_attemp)
                if square not in game.available_moves():
                    raise ValueError
                valid_square = True
            except ValueError:
                print('Invalid square. Try again!')

        return square