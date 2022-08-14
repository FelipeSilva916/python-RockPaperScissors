
def get_choices():
    """
    Asks the user for a choice and returns it.
    """
    player_choice = 'rock'
    computer_choice = 'paper'
    print('You chose {} and the computer chose {}.'.format(player_choice, computer_choice))
    return player_choice, computer_choice
