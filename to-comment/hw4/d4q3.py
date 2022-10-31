
index = 100 #On définit les variables de bases
réponses = []

while index < 500:
    chaine = str(index)
    if int(chaine[0])**3 + int(chaine[1])**3 + int(chaine[2])**3 == index:
        réponses.append(index) #On ajoute l'index à la réponse si il est un nombre cube
        index = index + 1
    else:
        index = index + 1

print(réponses)
#On imprime les réponses
