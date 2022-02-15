#! python3
"""
Jonathan Mainhart
Homework 4
12 October 2021

Rock-Paper-Scissors-Lizard-Spock

An updated version of the beloved children's game of Rack-Paper-Scissors.

Paper covers Rock
Rock smashes Scissors
Scissors cut Paper
Paper disproves Spok
Spock vaporizes Rock
Rock crushes Lizard
Lizard poisons Spock
Spock smashes Scissors
Scissors decapitates Lizard
Lizard eats Paper

Original concept courtesy of the hit Television Program 'The Big Bang Theory'
"""
import logging
import sys
import os
import menu
import dynamo_lib
import scores_lib

def main():
    """
    main() function of homework1 project.
    """
    # set up logging
    LOG_FILE = os.path.abspath(os.path.join(os.path.dirname(__file__), 'log/homework4.log'))
    logging.basicConfig(level=logging.INFO,
                        filename=LOG_FILE,
                        datefmt='%d-%b-%y %H:%M:%S',
                        format='%(levelname)s: %(asctime)s: %(message)s')
    logging.info('starting')

    
    # check for high scores - build if needed
    if not dynamo_lib.table_exists('highscores'):
        print('The high scores table is missing.... building a new one')
        scores_lib.generate_scores()
    
    # present the main menu - all functions are accessed via the main and sub menus
    menu.main_menu()

    # clear the screen then exit
    os.system('clear')
    logging.info('finishing')
    sys.exit(0)

if __name__ == '__main__':
    main()
