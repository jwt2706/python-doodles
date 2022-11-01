def initListe(L, n):
    #print(L, n)
    if n == 0: #si tout les nombres on ete ajoute a 'L', on retourne la liste
        return L
    L.append(n-1) #ajoute 'n' moin un dans la liste (pour rendre la liste tout les nombre de 0 et n-1)
    return initListe(L, n-1) #rend la liste recursive

L = [] #intialise la liste 'L'
n = int(input("Entrez une valeur pour 'n': ")) #demande une valeur pour 'n'
liste = initListe(L, n) #cherche les resultats
listeordre = sorted(liste) #cheche la liste en ordre
print("Voici la liste avec tout les nombre de 0 a n-1:", liste, "\nVoici la meme liste, mais en ordre:", listeordre) #imprime les resultats
