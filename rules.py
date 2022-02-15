"""
Jonathan Mainhart
SDEV 400

displays the rules and help for the game.
"""
import os
from game_lib import Action

CONTINUE = '... press enter to continue ...'

RULES = [
        "Paper covers Rock",
        "Rock smashes Scissors",
        "Scissors cut Paper",
        "Paper disproves Spock",
        "Spock vaporizes Rock",
        "Rock crushes Lizard",
        "Lizard poisons Spock",
        "Spock smashes Scissors",
        "Scissors decapitates Lizard",
        "Lizard eats Paper"
        ]
        
ABOUT = ('"Rock-Paper-Scissors-Lizard-Spock" is an update to the classic children\'s game of "Rock-Paper-Scissors\n('
        'also known as "Rochambeau", "roshambo", or "ro-sham-bo".\n\n'
        '"Rock-Paper-Scissors-Lizard-Spock" is a two-player game which has two possible outcomes:\n'
        'a tie, or a win for one player and a loss for the other.\n\n'
        'This program allows one human player (presumably you) to face off against the computer in a battle of epic proportions!\n'
        f'You and the computer will choose one of {len(Action)} choices and a winner will be determined.\n'
        )

def show():
    # just did this bit to be a bit clever, but may be usefull to pull the rules into the game at some point...
    os.system('clear')
    print(ABOUT)
    print("The Rules are as Follows:")
    for rule in RULES:
        print(f'{rule}')
    print('\nYou will enter your initials when you are finished playing. \nYour score will be compared to the high scores. '
         '\nYour score will be added to the high scores if it is higher than any of the top ten.')
    print('High scores can be manually saved on the main menu, otherwise scores will save on exit.')
    input(CONTINUE)
    
    