import random

def name_choice():
    """this function allow the player to choose enter a name or pseudo """
    username=""
    while username =="": #if value of user is empty the loop continue
        username=input("please enter your name or pseudo")
        return username
        print("welcome on pendu game ",username," !")
