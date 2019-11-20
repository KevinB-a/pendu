
import random

from functions import *

from data import *


username=name_choice()
continue_game=True
while continue_game== True:

    word =random.choice(words_list) # choose random word in words_list
    list1=[]
    your_list=[]

    for el in word:
        list1.append(el) # add every letter in list1
        your_list.append('*') # add * for every letter in word

    print("".join(your_list)) # change your_list in str

    nb_error = 0 # initialize number of error
    while nb_error < 8 :
        letter = input("Enter your letter").lower()

        if len(letter) > 1:
            if letter == word:
                print("you find the word")
                break

        if letter in list1:
            for index,element in enumerate(list1): 
                if element==letter:
                    your_list[index] = element # change * by letter if letter is in word
            good_letter = ''.join(your_list)
            print("good letter ",good_letter)

            if list1==your_list:
                print("you find the word")
                break
        else:
            nb_error +=1
            print('wrong letter,you still have %s try'%(8-nb_error))

    if nb_error ==8:
        print("you don't find the word")

    your_score=8-nb_error
    print("your score is",your_score)
    restart=input("do you want to play again ? enter yes for restart and no for quit").lower()
    if restart =="yes" or rematch == "y" or rematch =="oui" or rematch == "o" :
        continue_game = True #if user choose stop the game continue_game become false and while loop stop
    else:
        continue_game = False #restart the game if user wants
