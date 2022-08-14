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
    elif player == "rock":
        if computer == "paper":
            return "Paper covers rock! You lose."
        else:
            return "Rock smashes scissors! You win!"

    elif player == "paper":
        if computer == "scissors":
            return "Scissors cuts paper! You lose."
        else:
            return "Paper covers rock! You win!"

    elif player == "scissors":
        if computer == "rock":
            return "Rock smashes scissors! You lose."
        else:
            return "Scissors cuts paper! You win!"


choices = get_choices()
result = check_win(choices['player'], choices['computer'])
print(result)