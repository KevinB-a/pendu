
import random

from functions import *

from data import *

import pickle
"""save_scores()
if name_choice() not in scores.keys():
    scores[name_choice()] = 0
scores=collect_scores()"""
continue_game=True
while continue_game == True:

    username=name_choice()  # call function name_choice
    number_of_errors()
    restart=input("do you want to play again ? enter yes for restart and no for quit").lower()
    if restart in ["yes","y","oui","o"] :
        continue_game = True #if user choose stop the game continue_game become false and while loop stop
    else:
        continue_game = False #restart the game if user wants

#save_scores()
