"""
menu.py

Jonathan Mainhart
SDEV 400
12 October 2021

menu functions for homework 4
"""
import logging
import os
from time import sleep
import game_lib
import scores_lib
import s3lib
import rules

PROMPT = 'Please make a selection >>> '
INVALID_SELECTION = '\nPlease make a valid selection.\n'
CONTINUE = '... press enter to continue ...'

def main_menu():
    
    # get high scores for the game
    global highscores
    highscores = scores_lib.get_recorded_scores()
    
    user_selection = 0

    while user_selection == 0:
        os.system('clear')
        print('Main Menu\n'
              '1. Play Game\n'
              '2. High Scores\n'
              '3. Rules\n'
              '4. Save Scores\n'
              '5. Reset High Scores\n'
              '6. Exit')

        # get user selection
        user_selection = input(PROMPT)[:1]
        if user_selection not in ('1', '2', '3', '4', '5', '6'):
        # discard invalid selections
            print(f'{INVALID_SELECTION}')
            input(CONTINUE)
            user_selection = 0
        if user_selection == '1':
            # play game
            score = game_lib.play()
            # update highscores
            highscores = scores_lib.update_high_scores(highscores, score)
            # reset the game
            game_lib.reset_game()
            # reset user selection
            user_selection = 0
        
        if user_selection == '2':
            # see high scores
            os.system('clear')
            print(f'High Scores (Wins-Ties-Losses):')
            for score in highscores:
                print("{}\t\t{}-{}-{}".format(score["name"], score["wins"], score["ties"], score["losses"]))
            input(CONTINUE)
            user_selection = 0
        
        if user_selection == '3':
            # see rules
            rules.show()
            user_selection = 0
        
        if user_selection == '4':
            # save scores
            print('saving...')
            scores_lib.upload_scores(highscores)
            print('done')
            input(CONTINUE)
            user_selection = 0
            
        if user_selection == '5':
            confirmed = 0
            while confirmed == 0:
                confirmed = input('Are you sure? (y/n) >>> ')
                if confirmed not in ('y', 'n'):
                    print(INVALID_SELECTION)
                    confirmed = 0
                if confirmed == 'y':
                    # reset scores
                    print('resetting scores... this may take a moment...')
                    scores_lib.reset_high_scores()
                    highscores = scores_lib.get_recorded_scores()
                    print('done')
                    input(CONTINUE)
                    user_selection = 0
                elif confirmed == 'n':
                    print('Scores have not been reset.')
                    input(CONTINUE)
                    user_selection = 0
        
        if user_selection == '6':
            # save scores on exit
            print('saving...')
            scores_lib.upload_scores(highscores)
            print('done')
            # return to __main__ to exit
            return

