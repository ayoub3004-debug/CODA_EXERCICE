from ast import main
from datetime import date
from email import message


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

def exercice5():
    nombre1 = int(input("Entrez le premier nombre : "))
    nombre2 = int(input("Entrez le deuxième nombre : "))
    resultat = nombre1 + nombre2
    print("La somme est :", resultat)

def exercice6():
    nombre1 = int(input("Entrez le premier nombre : "))
    nombre2 = int(input("Entrez le deuxième nombre : "))
    resultat = nombre1 - nombre2
    print("La différence est :", resultat)

def exercice7():
    nombre1 = int(input("Entrez le premier nombre : "))
    nombre2 = int(input("Entrez le deuxième nombre : "))
    resultat = nombre1 * nombre2
    print("Le produit est :", resultat)

def exercice8():
    nombre1 = int(input("Entrez le premier nombre : "))
    nombre2 = int(input("Entrez le deuxième nombre : "))
    resultat = nombre1 / nombre2
    print("Le quotient est :", resultat)

def exercice9():
    nombre = int(input("Entrez un nombre : "))
    carre = nombre ** 2
    print("Le carré est :", carre)

def exercice10():
    nombre = int(input("Entrez un nombre : "))
    double = nombre * 2
    print("Le double est :", double)

def exercice11():
    nombre = float(input("Entrez un nombre : "))
    moitie = nombre / 2
    print("La moitié est :", moitie)

def exercice12():
    message = input("Entrez un message : ")
    for i in range(5):
     print(message)

def exercice13():
    for i in range(1, 6):
     print(i)

def exercice14():
    for i in range(1, 6):   # de 1 à 5
     print(f"2 x {i} = {2 * i}")

def exercice15():
    cote = float(input("Entrez la longueur du côté du carré : "))
    perimetre = 4 * cote
    print("Le périmètre du carré est :", perimetre)

def exercice16():
    cote = float(input("Entrez la longueur du côté du carré : "))
    aire = cote * cote
    print("L'aire du carré est :", aire)












   
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
    elif choix == "5":
        exercice5()
    elif choix == "6":
        exercice6()
    elif choix == "7":
        exercice7()
    elif choix == "8":
        exercice8()
    elif choix == "9":
        exercice9()
    elif choix == "10":
        exercice10()
    elif choix == "11":
        exercice11()
    elif choix == "12":
        exercice12()
    elif choix == "13":
        exercice13()
    elif choix == "14":
        exercice14()  
    elif choix == "15":
        exercice15()  
    elif choix == "16":
        exercice16() 



    else:
        print("Exercice non reconnu.")

if __name__ == "__main__":

    main()