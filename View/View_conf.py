from Model.display import *  

class View():

    def __init__(self, display):
        self.display = display

    def get_all(self):
        liste = self.display.jointure()
        
        for i in liste:
            speak = Speaker(i)
            conf = Conference(i)
            print(speak,conf)

    """presentation of the possible choices for the user
        présentation des choix possible pour l'utilisateur"""

    def lancement(self):

        print("+--------------------------------------------------+")
        print("|---------- GESTIONNAIRE DES CONFERENCES ----------|")
        print("+--------------------------------------------------+")
        print("+-------- Action ----------|-------- Touche -------+")
        print("|     Créer un speaker     |          [P]          |")
        print("|   Supprimer un speaker   |          [Y]          |")
        print("|      Voir un speaker     |          [T]          |")
        print("|   Créer une conférence   |          [H]          |")
        print("| Supprimer une conférence |          [O]          |")
        print("|   Voir une conférence    |          [N]          |")
        print("+--------------------------------------------------+")
        print("|  Quitter le proggramme   |          [Q]          |")
        print("+--------------------------------------------------+")

        
        

