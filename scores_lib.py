"""
scores_lib.py

Jonathan Mainhart
SDEV 400
12 October 2021

Score functions for game.
Gets high scores.
Posts 
"""
import json
from time import sleep
from operator import itemgetter
import dynamo_lib
import s3lib

def generate_scores():
    """
    Runs if the highscores table is not found
    """
    
    table_definition = s3lib.read_file('jonathan-mainhart-1', 'homework4/ScoreTableDefinition.json')
    
    
    dynamo_lib.create_table(table_definition)
    
    sleep(6)
    
    
    reset_high_scores()
    

def get_recorded_scores():
    
    recorded_scores = sorted(dynamo_lib.get_items('highscores')["Items"], key=itemgetter("wins", "ties"), reverse=True)

    
    return recorded_scores

def update_high_scores(scores_list, game_score):
    """
    updates scores with new high-scores
    :param scores_list: list of scores
    :param game_score: last game score
    :return: None
    """
    scores_list.append(game_score)
    
    highscores = sorted(scores_list, key=itemgetter('wins', 'ties'), reverse=True)[:10]

    return highscores
    
def upload_scores(scores_list):
    """
    write new high scores to database for persistance
    """
    # iterate through the scores
    for x in range(len(scores_list)):
        # get the index of the score (add 1 since list begins at 0)
        id = x + 1
        # update the ID to the index of the score
        scores_list[x].update({"ID": id})
    
    for score in scores_list[:10]:
        dynamo_lib.update_record('highscores', score)

def reset_high_scores():
    """
    reset high scores
    """
    initial_scores = s3lib.read_file('jonathan-mainhart-1', 'homework4/scores.json')
    sleep(2)
    dynamo_lib.batch_write(initial_scores)
