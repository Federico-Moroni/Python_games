import random
from words import words
import string


def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word.upper()


def hangman():
    word = get_valid_word(words)
    word_letters = set(word)  # letters in word
    alphabet = set(string.ascii_uppercase)
    used_letters = set()  # what the user has guessed

    lives = 6

# Getting user input
    while len(word_letters) > 0 and lives > 0:
        # Letters already used
        print("You have used these letters:", ' '.join(used_letters))

        # What the current word is (Example: H - - P P Y)
        word_list = [
            letter if letter in used_letters else '-' for letter in word]
        print("Current word: ", " ".join(word_list))

        user_letter = input("Guess a letter: ").upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)

            else:
                lives -= 1  # Takes away one life
                print(f"Letter is not in the word \n You have {lives} lives")

        elif user_letter in used_letters:
            print("You've already used that word. Please try again")

        else:
            print("Invalid character")

    # Gets here when len(word_letters) == 0 OR when lives == 0
    if lives == 0:
        print("You're dead! The word was", word)
    else:
        print("You've guessed the word!", word, "!!")


hangman()
