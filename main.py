
from operator import ge
from random import choices


def get_choices():
    """
    Asks the user for a choice and returns it.
    """
    player_choice = 'rock'
    computer_choice = 'paper'

    return player_choice, computer_choice


choices = get_choices()
print(choices)
