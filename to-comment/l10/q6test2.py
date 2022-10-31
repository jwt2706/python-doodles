# METTRE VOTRE NOM ET NUMÉRO D'ÉTUDIANT ICI
# Jacob Taylor 300273062
# En mettant votre nom ici, vous signez la déclaration d'intégrité de q4test2 

#########################
# QUESTION 6
#########################

def baikal(L):
    '''(list of int) -> bool
    Conditions préalables : len(L)>=2

    >>> baikal([4,5,3,0,-4])
    True
    >>> baikal([4,5,-7])
    False'''
    gap = 1 #cette variable est l'espace attendu entre les deux nombres
    for i in range(len(L)): #pour chaque nombre dans la liste
        if i == 0: #on saute la premiere puisqu'il n'y a rien a comparer avec lui
            ''''''
        else:
            if (gap == ((int(L[i])) - (int(L[i-1])))) or (gap == ((int(L[i-1])) - (int(L[i])))): #on soustrait pour calculer le 'gap' (on le fait des deux directions)
                gap += 1 #on agrandi le gap pour la prochaine calculation
            else:
                return False #si le gap n'est pas correct on retourne false
    return True #si tout a bien alle on retourne True

liste = list(input("Entrez une liste avec chaque valeur spepare par une virgule: ").split(","))#on demande une liste
print(baikal(liste))#on affiche le resultat
