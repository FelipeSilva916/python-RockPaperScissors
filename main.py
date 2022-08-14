
from operator import ge
from random import choices


def get_choices():
    """
    Asks the user for a choice and returns it.
    """
    player_choice = input("Choose rock, paper or scissors: ")
    computer_choice = 'paper'
    choices = {'player': player_choice, 'computer': computer_choice}
    return choices


choices = get_choices()
print(choices)
