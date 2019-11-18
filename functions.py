import random

def name_choice():
    """this function allow the player to choose enter a name or pseudo """
    username=""
    while username =="": #if value of user is empty the loop continue
        username=input("please enter your name or pseudo")
        return username
        print("welcome on pendu game ",username," !")

def collect_scores():
    """this function collect score of the player"""

    if os.path.exists(name_file_scores): # Le fichier existe
        # On le récupère
        file_scores = open(name_file_scores, "rb")
        collect_file = pickle.Unpickler(file_scores)
        scores = collect_file.load()
        fichier_scores.close()
    else: # Le fichier n'existe pas
        scores = {}
    return scores

def save_scores(scores):
    """this function save score on score"""

    file_scores = open(name_file_scores, "wb") # 
    save_file = pickle.Pickler(file_scores)
    save_file.dump(scores)
    fichier_scores.close()
