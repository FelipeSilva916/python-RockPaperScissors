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
