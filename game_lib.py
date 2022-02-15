"""
game_lib.py

Jonathan Mainhart
SDEV 400
12 October 2021

Game functions for Rock Paper Scissors Lizard Spock

Heavily borrowed from https://realpython.com/python-rock-paper-scissors/
"""
import random
import os
from enum import IntEnum

INVALID_SELECTION = '\nPlease make a valid selection.\n'
CONTINUE = '... press enter to continue ...'

# 1. define actions
# Real Python
class Action(IntEnum):
    Rock = 1
    Paper = 2
    Scisssors = 3
    Lizard = 4
    Spock = 5

# 2. define victories - dictionary key: value pairs. Keys are winners, values are
# what the key Action beats.
# Real Python
victories = {
    Action.Scisssors: [Action.Lizard, Action.Paper],
    Action.Paper: [Action.Spock, Action.Rock],
    Action.Rock: [Action.Lizard, Action.Scisssors],
    Action.Lizard: [Action.Spock, Action.Paper],
    Action.Spock: [Action.Scisssors, Action.Rock]
}

# 3. create a game score
game_score = {
    "wins": 0,
    "ties": 0,
    "losses": 0
}

# get user input
# adapted from Real Python
def get_user_selection():
    choices = [f"{action.value}. {action.name}" for action in Action]
    choices_str = "\n".join(c for c in choices)
    selection = int(input(f"CHOOSE YOUR CHAMPION!\n{choices_str}\nEnter a choice >>> "))
    action = Action(selection)
    return action
	
# get computer selection
# adapted from Real Python
def get_computer_selection():
    selection = random.randint(1, len(Action))
    action = Action(selection)
    return action

# determine winner - update score
# Adapted from Real Python
def determine_winner(user_action, computer_action):
    defeats = victories[user_action]
    if user_action == computer_action:
        print(f"Both players selected {user_action.name}. It's a tie!")
        game_score["ties"] += 1
    elif computer_action in defeats:
        print(f"{user_action.name} beats {computer_action.name}! You win!")
        game_score["wins"] += 1
    else:
        print(f"{computer_action.name} beats {user_action.name}! You lose.")
        game_score["losses"] += 1

# play the game until the user quits
# Adapted from Real Python
def play():
    """
    play the game
    """
    
    game = True
    
    while game:
        os.system('clear')
        try:
            user_action = get_user_selection()
        except ValueError as e:
            range_str = f"1 to {len(Action)}"
            print(f"Invalid selection. Enter a value between {range_str}")
            input(CONTINUE)
            continue
    
        computer_action = get_computer_selection()
        determine_winner(user_action, computer_action)
        
        # show score
        print("Your win-tie-loss record is: {}-{}-{}".format(game_score["wins"], game_score["ties"], game_score["losses"]))
        
        # play again
        user_input = False
        while not user_input:
            
            user_input = input('Would you like to play again? (y/n)>>> ')[:1].lower()
            # discard bad input
            if user_input not in ('y', 'n'):
                print(INVALID_SELECTION)
                user_input = False
            
            if user_input == 'n':
                game = False

    # pass score to score_lib to see if it is a high score
    player_name = input('Enter your initials (e.g. ABC) >>> ')[:3].upper()
    
    final_score = {
        "name": player_name,
        "wins": game_score["wins"],
        "ties": game_score["ties"],
        "losses": game_score["losses"]
    }
    

    return final_score

def reset_game():
    # reset score
    game_score.update({
    "wins": 0,
    "ties": 0,
    "losses": 0
    })
