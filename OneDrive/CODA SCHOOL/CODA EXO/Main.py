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

def exercice17():
    euros = float(input("Entrez le montant en euros : "))
    dollars = euros * 1.1
    print("Le montant en dollars est :", dollars)

def exercice18():
    minutes = float(input("Entrez le nombre de minutes : "))
    secondes = minutes * 60
    print("Le nombre de secondes est :", secondes)

def exercice19():
    prix_ht = float(input("Entrez le prix HT : "))
    prix_ttc = prix_ht * 1.2
    print("Le prix TTC est :", prix_ttc)

def exercice20():
    nom = input("Entrez votre nom : ")
    age = input("Entrez votre âge : ")
    print(nom, "a", age, "ans")

def exercice21():
    nombre = float(input("Entrez un nombre : "))
    if nombre > 0:
     print("Le nombre est positif")
    elif nombre < 0:
     print("Le nombre est négatif")
    else:
     print("Le nombre est nul")

def exercice22():    
    age = int(input("Entrez votre âge : "))
    if age >= 18:
     print("Vous êtes majeur(e)")
    else:
     print("Vous êtes mineur(e)")

def exercice23(): 
    note = float(input("Entrez la note : "))
    if note >= 10:
     print("La note permet de valider")
    else:
     print("La note ne permet pas de valider")

def exercice24(): 
    nombre1 = float(input("Entrez le premier nombre : "))   
    nombre2 = float(input("Entrez le deuxième nombre : "))
    if nombre1 > nombre2:
     print(f"{nombre1} est le plus grand")
    elif nombre2 > nombre1:
     print(f"{nombre2} est le plus grand")
    else:
     print("Les deux nombres sont égaux")

def exercice25(): 
    nombre1 = float(input("Entrez le premier nombre : "))
    nombre2 = float(input("Entrez le deuxième nombre : "))
    if nombre1 < nombre2:
     print("Les nombres sont dans l'ordre croissant")
    elif nombre1 > nombre2:
     print("Les nombres ne sont pas dans l'ordre croissant")
    else:
     print("Les nombres sont égaux")

def exercice26():
    nombre = int(input("Entrez un nombre : "))
    if nombre % 5 == 0:
     print(f"{nombre} est divisible par 5")
    else:
     print(f"{nombre} n'est pas divisible par 5")

def exercice27():
    age = int(input("Entrez votre âge : "))
    if age < 12:
     print("Enfant")
    elif 12 <= age <= 17:
     print("Adolescent")
    else:
     print("Adulte")

def exercice28():
    temperature = float(input("Entrez la température de l'eau en °C : "))
    if temperature < 0:
     print("L'eau est solide (glace)")
    elif 0 <= temperature <= 100:
     print("L'eau est liquide")
    else:
     print("L'eau est gazeuse (vapeur)")

def exercice29():
    note = float(input("Entrez la note : "))
    if note < 10:
     mention = "Recalé"
    elif 10 <= note < 12:
     mention = "Passable"
    elif 12 <= note < 14:
     mention = "Assez bien"
    elif 14 <= note < 16:
     mention = "Bien"
    elif 16 <= note < 18:
     mention = "Très bien"
    print(f"Note : {note} → Mention : {mention}")

def exercice30():
    N = int(input("Entrez un nombre N : "))
    for i in range(1, N + 1):
     print(i, end=" ")  # end=" " permet d'ecrire sur la même ligne
     print()  # sautER la ligne à la fin















   
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
    elif choix == "17":
        exercice17()
    elif choix == "18":
        exercice18()
    elif choix == "19":
        exercice19()
    elif choix == "20":
        exercice20()
    elif choix == "21":
        exercice21()
    elif choix == "22":
        exercice22()
    elif choix == "23":
        exercice23()
    elif choix == "24":
        exercice24()
    elif choix == "25":
        exercice25()
    elif choix == "26":
        exercice26()
    elif choix == "27":
        exercice27()
    elif choix == "27":
        exercice27()
    elif choix == "28":
        exercice28()
    elif choix == "29":
        exercice29()
    elif choix == "30":
        exercice30()
    else:
        print("Exercice non reconnu.")

if __name__ == "__main__":

    main()