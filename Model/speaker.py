from Model.connection import *

class Speaker():

    def __init__(self):
        self.choice = connection()
        self.prenom = None
        self.nom = None
        self.description = None
        self.prefession = None
        self.statut = True 

    def create_speaker(self):
        self.choice.initialize_connection()
        self.prenom = input("Quel est votre prénom ? ")
        self.nom = input("Quel est votre nom ? ")
        self.description = input("Ajoutez une description : ")
        self.profession = input("Quel est votre prefession ? ")
        self.choice.cursor.execute("INSERT INTO Speaker(prenom, nom, description, profession) VALUES (%s, %s, %s, %s)",(self.prenom,self.nom,self.description,self.profession))
        self.choice.connection.commit()
        self.choice.close_connection()


    def delete_speaker(self):
        pass

    def read_speaker(self):
        pass