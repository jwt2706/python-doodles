def séquenceDeDeux(): #Définir la fonction
    index = 0
    index1 = 1 #On déclare des valeurs, et on demande des valeurs à l'utilisateur
    valListe = input("Veuillez insérer une liste de valeurs séparées par des virgules: ")
    liste = valListe.split(",")
    while index1 < len(liste): #Tant que index est plus petit que la longueur de la liste:
        valInd = liste[index]
        valInd1 = liste[index1]
        if valInd == valInd1: #Si la valeur de index est égale à la valeur de index1:
            return True #Retourner True
        else: #Sinon:
            index = index+1 #Valeur de index + 1
            index1 = index1+1 #Valeur de index + 1
    return False #Retourner False

print(séquenceDeDeux()) #Appeler la fonction
