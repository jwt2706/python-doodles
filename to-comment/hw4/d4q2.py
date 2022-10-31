
def nombre_divisible(liste, n): #On définit la variable
    index = 0
    valide = []
    while index < len(liste):
        valeur = int(liste[index]) / n
        arrondis = int(liste[index]) // n
        if valeur == arrondis: #On vérifie si la division est réellement un nombre entier
            valide.append(liste[index]) #Si oui, on ajoute la valeur du diviseur valide
            index = index + 1
        else:
            index = index + 1 #Sinon, on continue la boucle
    return valide #On retourne le nombre de diviseurs valides

#On demande des valeurs à l'utilisateur
n = int( input("Veuillez entrer un nombre entier: ") )
l = input("Veuillez entrer une liste de numéros, séparés par des virgules: \n").split(',')
réponse = nombre_divisible(l, n)
if len(réponse) > 1: #On donne la réponse selon le nombre de diviseurs valides
    print("Il y a", len(réponse), "nombres divisibles par", n, "dans la liste, soit:", réponse)
elif len(réponse) == 1:
    print("Il y a", len(réponse), "nombre divisible par", n, "dans la liste, soit:", réponse)
else:
    print("Aucun élément dans la liste est divisible par", n)
