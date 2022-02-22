import random
# r>s, s>p, p>r


def play():
    user = input(
        "What's your choice? 'r' for rock, 'p' for paper and 's' for scissors\n")
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return f"It's a tie, the computer also chose {computer}"

    if is_win(user, computer):
        return f"You won! The computer chose {computer}"

    return f"You lost! The computer chose {computer}"


def is_win(player, opponent):
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True


print(play())
