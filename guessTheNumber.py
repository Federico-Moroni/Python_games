import random

# Computer picks a number and user guess


def guess(x):
    random_number = random.randint(1, x)
    guess = 0

    while guess != random_number:
        guess = int(input(f"Guess a number between 1 and {x}: "))
        if guess > random_number:
            print("Too high")
        elif guess < random_number:
            print("Too low")
    print(f"Congratulations! You guessed! The number was {random_number}!")


# guess(10)

# User picks a number and computer guess


def computer_guess(x):
    low = 1
    high = x
    feedback = ""

    while feedback != "c":
        if low != high:
            guess = random.randint(low, high)
        else:
            # Esto pasa si ponemos low y high el mismo numero.. entonces la computadora va a resolverlo a la primera.
            guess = low
        feedback = input(
            (f"Is {guess} to high (H), too low (L), or correct (C)?").lower())
        if feedback == "h":
            high = guess - 1
        elif feedback == "l":
            low = guess + 1

    print(f"The computer guessed you number! {guess} correctly")


computer_guess(20)
