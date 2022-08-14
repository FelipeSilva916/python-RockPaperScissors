import random


def get_choices():
    """
    Asks the user for a choice and returns it.
    """
    player_choice = input("Choose rock, paper or scissors: ")
    options = ["rock", "paper", "scissors"]
    computer_choice = random.choice(options)
    choices = {'player': player_choice, 'computer': computer_choice}
    return choices


def check_win(player, computer):
    """
    Checks if the player or computer won.
    """
    print(f'You chose {player} and the computer chose {computer}.')
    if player == computer:
        return "It's a tie!"
    if player == "rock":
        if computer == "paper":
            return "Computer wins!"
        else:
            return "Player wins!"
    if player == "paper":
        if computer == "scissors":
            return "Computer wins!"
        else:
            return "Player wins!"
    if player == "scissors":
        if computer == "rock":
            return "Computer wins!"
        else:
            return "Player wins!"


check_win('rock', 'paper')
