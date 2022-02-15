# sdev400_hw4
## Rock Paper Scissors Lizard Spock
This assignment uses AWS and the Cloud9 environment to develop a simple Rock-Paper-Scissors menu-driven game written in Python. The application uses a DynamoDB table to save game scores. The table description and initial scores are saved in an S3 bucket.

## Concept of Development
Rock-Paper-Scissors is a classic children’s game which almost everyone is familiar with. This made the decision to use the game as the central theme for the application an easy one. This implementation of the game takes a little twist and adds two additional weapons to the original three. Also included is a leader board which saves the top 10 high scores to a DynamoDB table which is built from a table definition and initial scores saved in an S3 bucket.

#### DynamoDB Table
The application looks for the DynamoDB table ‘highscores’ when launched. If it is not found, it creates the table by first reading the definition stored in an S3 bucket, then populates the table with default values. This table will be used to store scores after the program exits to provide persistence. The next time the program launches, the scores will be read from the table. Scores can be manually saved to the table, or will be automatically saved on exit.

#### The Main Menu
The Main Menu is the central point of execution for the remainder of the application. From here, users can navigate to the options available to them. The menu is a simple while loop which continues to run if the sentinel value is zero.

The user is presented with 6 choices: Play Game, High Score, Rules, Save Scores, Reset High Scores, and Exit. The user makes their selection by entering the number of their choice and pressing ‘enter’. If the user enters something other than one of the choices, the application will alert them to their mistake and allow them to try again.

Before being processed, the user input is stripped to allow only the first character to be entered, effectively denying a chance to inject code. Then the user input is compared against an allow list of valid inputs. If the input is not on the list, it is discarded, and the user is prompted to make a valid entry.

#### The Game
All game functions are contained in the game_lib.py file which borrows ideas and code from realpython.com. The game is played by calling the play() function which calls other supporting functions within the library. The game runs in a loop until the user chooses to quit, at which time their cumulative game score is recorded with their initials and returned to the caller. 

#### High Scores
The high scores are held in memory as key-value pairs during runtime. As each game is played, the scores are updated to reflect any new high scores that have been achieved. Users can see the current high scores by selecting menu option 2 which simply iterates through the scores and prints them out using a formatted string. Users also have the option of saving the scores currently held in memory to the DynamoDB table by selecting option 4 on the Main Menu.

The table which holds the scores requires a unique key for each item. The key used is the attribute ‘ID’ since any number of players could potentially have the same name and same score. 
In order to simplify updating and retrieving scores from the table, the number of items in the table can be limited to 10 by changing the ID of each score and overwriting the scores already in the table.

The high scores held in memory will be automatically saved to the DynamoDB table when the user chooses to exit the application.

Users also have the option of resetting the high scores table back to the initial values by selecting option 5 on the Main Menu. 

## User Manual
Rock-Paper-Scissors-Lizard-Spock is a twist on the classic game of Rock-Paper-Scissors (also known as "Rochambeau", "roshambo", or "ro-sham-bo"). It is a two-player game with only two possible outcomes: Either one player wins and the other loses, or the game ends in a tie.

Choose your weapon and face-off against the computer opponent in this battle for playground supremacy! Table 1 shows which weapon wins.
##### Table 1
*Weapons*
| Weapon | ...beats |
| --- | --- | --- |
Rock | Smashes Scissors | Crushes Lizard
Paper | Covers Rock | Disproves Spock
Scissors | Cut Paper | Decapitates Lizard
Lizard | Eats Paper | Poisons Spock
Spock | Vaporizes RRock | Smashes Scissors

#### Starting the Application
Launch the application by typing python3 homework4 and pressing ‘Enter’ or ‘Return’ on the command line.

If this is the program’s first time running, you will be presented with a message letting you know that the High Scores table is being built and set up which may take a moment. Afterwards, you will be presented with the Main Menu as shown below.

Main Menu
![Main Menu](/images/image001.png "Main Menu")

#### Main Menu Options
The Main Menu is how you navigate the application. The menu presents you with the following options:
1.	Play Game
2.	High Scores
3.	Rules
4.	Save Scores
5.	Reset High Scores
6.	Exit
The user can select their choice by typing the number of their choice and pressing ‘Enter’ or ‘Return’.

#### Playing the Game
The Game Menu displays your choices as shown below. Enter the number of your choice and press enter to play.

Game Menu
![Game Menu](/images/image002.png "Game Menu")

The computer will select a random weapon to play against you, a winner will be determined, your cumulative score will be updated, and you will be asked if you wish to play again as shown below.

Game Play
![Game Play](/images/image003.png "Game Play")

Enter ‘n’ when you are finished playing. You will be asked for your initials as shown below and your score will be compared against the high scores. If your score is in the Top 10, it will be added to the high scores list. You will be returned to the Main Menu when the game is finished.

Finishing the Game
![Finishing the Game](/images/image004.png "Finishing the Game")

#### Viewing the High Scores
You can view the high scores by selecting option 2 on the Main Menu. When selected, the top ten high scores will be displayed as shown below. Pressing ‘enter’ will return you to the Main Menu.

High Scores
![High Scores](/images/image005.png "High Scores")

#### In-Game Rules
You can review the rules while playing the game by selecting option 3 from the Main Menu as shown below. Pressing ‘enter’ will return you to the Main Menu

Rules
![Rules](/images/image006.png "Rules")

#### Saving High Scores
High scores will be automatically saved to the cloud when you exit the application. However, you may save the scores manually before you exit by selecting option 4 on the Main Menu as shown below.

Saving Scores
![Saving Scores](/images/image007.png "Saving")

#### Resetting High Scores
You may reset the high scores saved in the cloud back to default values by selecting option 5 from the Main Menu as shown below. 
<span style="color:red;font-weight:700;font-size:20px">WARNING:</span> Resetting scores is permanent and cannot be undone.

Resetting Scores
![Resetting Scores](/images/image008.png "Resetting Scores")

#### Exiting the Game
You may exit the application by selecting option 6 from the Main Menu. Before exiting, the high scores will be saved to the cloud. You will then be returned to the command prompt.