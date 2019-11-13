
import random
from functions import *
continue_game=True
while continue_game==True:

    words_list = ["armoire","boucle","buisson","bureau","chaise","carton","couteau","fichier","garage"
    ,"glace","journal","kiwi","lampe","liste","montagne","remise","sandale","taxi","vampire","volant",]
    word =random.choice(words_list)
    list1=[]
    your_list=[]

    for el in word:
        list1.append(el)
        your_list.append('*')

    print("".join(your_list))

    nb_error = 0
    while nb_error < 8 :
        letter = input("Enter your letter")

        if len(letter)>1:
            if letter == word:
                print("you find the word")
                break

        if letter in list1:
            for (index,element) in enumerate(list1):
                if element==letter:
                    your_list[index] = element
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
    rematch=input("do you want to play again ? enter yes for rematch and no for quit").lower()
    if rematch =="no" or rematch == "n" or rematch =="quit" or rematch == "q" or rematch== "stop":
        continue_game = False #if user choose stop the game continue_game become false and while loop stop
    else:
        continue_game = True #restart the game if user wants
