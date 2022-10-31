def moyenne(valeurs):
    total = sum(valeurs) #'total' est la somme des valeurs dans la liste
    moyenne = total / len(valeurs) # diviser la somme avec le nombre de valeurs dans la liste
    return moyenne

liste = list(map(int,input("Entrez toutes valeurs separee par un espace: ").split()))
#demande plusieurs valeurs pour mettre dans la liste
moyenne = moyenne(liste) #calculer la moyenne
print(moyenne) #imprimer le resultat
