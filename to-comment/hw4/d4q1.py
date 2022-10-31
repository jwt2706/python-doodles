
def sequenceMax(liste): #On définit la variable
    index = 0
    comboMax = 1
    combo = 1
    while index < len(liste) - 1:
        if liste[index] == liste[index+1]: #Si les deux valeurs de la liste qui se suivent sont égales:
            combo = combo + 1 #On ajoute 1 au compte
            index = index + 1 #On ajoute 1 à l'index
            if combo > comboMax: #Si le compte présent est plus grand que le max:
                comboMax = combo #On le remplace
        else: #Si il y a deux valeurs différentes une après l'autre:
            combo = 1 #Le compte se réinitialise
            index = index + 1
    return comboMax #On retourne le maximum de valeurs qui se suivent

#On demande une valeur à l'utilisateur
l = input("Veuillez entrer une liste de valeurs séparées par des virgules: ").split(',')
print(l)
print(sequenceMax(l)) #On appelle la fonction
