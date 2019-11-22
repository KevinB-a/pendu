import os

import random

import pickle

from data import *

def name_choice():
    """this function allow the player to choose enter a name or pseudo """
    username=""
    while username =="": #if value of user is empty the loop continue
        username=input("please enter your name or pseudo")
    print("welcome on pendu game ",username," !")
    return username


def random_choice():
    word=random.choice(words_list) # choose random word in words_list
    return word

def number_of_errors():
    word_letter_list=[]
    hidden_word=[]
    for el in random_choice():
        word_letter_list.append(el) # add every letter in list1
        hidden_word.append('*') # add * for every letter in word
    print("".join(hidden_word)) # change your_list in str
    nb_error = 0 # initialize number of error
    while nb_error < 8 :
         letter = input("Enter your letter :").lower()# if user enter upper letter convert to lower
         if len(letter) == 0:
            letter = input("Enter your letter :").lower()

         if len(letter) > 1:
             if letter == random_choice():
                 print("you find the word")
                 break

         if letter in word_letter_list:
             for index,element in enumerate(word_letter_list): # list index and element in list
                if element==letter:
                    hidden_word[index] = element # change * by letter if letter is in word
             good_letter = ''.join(hidden_word) # convert hidden_word in str
             print("good letter ",good_letter)

             if word_letter_list==hidden_word:
                 print("you find the word")
                 break
         else:
             nb_error +=1
             print('wrong letter,you still have %s try'%(8-nb_error))

    if nb_error ==8:
        print("you don't find the word")
    your_score=8-nb_error
    # scores[username] = your_score
    print("your score is",your_score)
    return hidden_word ,your_score


def save_scores():
    """this function save score on scores"""
    score={name_choice() : 0}
    with open("scores", "wb") as file : # open the file
        save_file = pickle.Pickler(file) # save file
        save_file.dump(score)


def collect_scores():
    """this function collect score of the player"""

    with open("scores", "rb") as file :
        collect_file = pickle.Unpickler(file) # read element in the file
        scores = collect_file.load()
         # close file
