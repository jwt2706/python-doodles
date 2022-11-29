def espaces(s):
    sListe = list(s) #place toutes les caracteres dans une liste
    sEspace = '' #cree une string 'sEspace'
    for i in range(len(sListe)): #reccommence pour chaque caracteres
        sEspace = sEspace + (' ' + sListe[i]) #ajoute chaque caracteres avec un espace en avant dans le stringe 'sEspace'
    sEspace = sEspace.strip() #on enleve les espaces en avant et a la fin
    return sEspace #retourne le resultat


s = str(input("Entrez un message: ")) #demande une chaine
print(espaces(s)) #cherche et imprime le resultat
