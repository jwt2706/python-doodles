def moyenne(valeurs): #
    total = sum(valeurs)#cherche le total des notes
    moyenne = total / len(valeurs)#divise par le nombre de notes donne
    listeEnOrdre = list(sorted(valeurs)[:len(valeurs)])#met les notes en ordre
    valeurs = [moyenne, listeEnOrdre[len(valeurs)-1], listeEnOrdre[0]]#trouve le dernier et le premier (la meilleur et la pire note)
    return valeurs #retourne les resultats

liste = list(map(int, input("Entrez toutes valeurs separee par un espace: ").split()))#demander des valeurs
res = moyenne(liste)#cherche les resultats
print("La moyenne est", res[0], ", la note la plus eleve est", res[1], "et la note la plus base est", res[2])#affiche les resultats
