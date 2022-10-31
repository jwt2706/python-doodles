def histo_n(x):
    dict_t = {} #cree un dictionnaire
    for key in range(len(x)): #pour chaque valeur, on compte le nombre de fois qu'il apparait et on ajoute le resultat dans le dictionnaire
        dict_t[x[key]] = x.count(x[key])
    return dict_t #on retourne le dictionnaire

t = tuple((input("Entrez des nombres separe par des viglues: ")).split(",")) #on demande un tuple
t = histo_n(t) #on le converti en histogramme (dictionnaire)
t_liste = list(t.items()) #on place les 'items' dans une liste
t_liste.sort() #on .sort() la liste
print(t_liste) #on imprime les resultats
