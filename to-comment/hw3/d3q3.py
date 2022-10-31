
def compte_positifs(): #On définit la fonction compte_positif
    index = 0
    valPos = 0
    valListe = str(input("Veuillez entrer une liste de valeur séparées par des virgules: "))
    liste = valListe.split(",")
    while index < len(liste): #Tant que l'index est plus petit que la longueur de la liste:
        if int(liste[index]) > 0: #Si le chiffre est plue grand que zero:
            valPos = valPos + 1 #+1 valeur positive
        index = index+1 #Index = index plus 1
        
    print("Il y a", valPos, "valeur(s) positive(s).") #On imprise la réponse

compte_positifs() #On appelle la fonction
