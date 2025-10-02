from ast import main
from datetime import date


def exercice1():
    print("Exercice 1 : Bonjour le monde !")
    print("Hello World !")

def exercice2():
   prenom = input("exercice 2 : entrer votre prénom ?")
   print("Bonjour", prenom)

def exercice3():
    print("première ligne\ndeuxieme ligne\ntroisieme ligne")

def exercice4():
    annee = int(input("Entrez votre année de naissance : "))
    annee_actuelle = date.today().year
    age = annee_actuelle - annee
    print("Vous avez environ", age, "ans.")

   
def main():
    # Demande à l'utilisateur quel exercice exécuter
    choix = input("Entrez le numéro de l'exercice à exécuter : ")
    if choix == "1":
        exercice1()
    elif choix == "2":
        exercice2()
    elif choix == "3":
        exercice3()
    elif choix == "4":
        exercice4()
    else:
        print("Exercice non reconnu.")

if __name__ == "__main__":

    main()