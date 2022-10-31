
'''
Je comprends l'importance de l'intégrité professionnelle dans mes études et ma future carrière
en ingénierie ou en informatique. Je certifie par la présente que j'ai effectué et que je ferai tous les travaux
sur cet examen entièrement par moi-même, sans aide extérieure ou utilisation de matériel non autorisé
sources d'informations. De plus, je ne fournirai pas d'aide aux autres.
'''

# LIRE LA DÉCLARATION CI-DESSUS
#
# METTRE VOTRE NOM ET NUMÉRO D'ÉTUDIANT ICI
# Jacob Taylor 300273062
# En mettant votre nom ici, vous signez la déclaration ci-dessus et
# accepter le TEST 2 (règles d'intégrité)

#########################
# QUESTION 4
#########################

def nyasa(L):
    '''list of str->int
    Précondition : len(L)>0 et L ne contient pas de mots identiques

    >>> nyasa(["rat", "war", "sol", "ads"])
    6
    >>> nyasa(["rat", "jazzy", "war", "solei", "pizza"])
    4
    >>> nyasa(["at", "jazz", "war", "solei"])
    0
    '''
    nombreDePaires = 0
    tmp = []
    for i in range(len(L)):
        tmp = [
        for j in range(len(tmp)):
            if j != 0:
                print(L[i:], L[i+1:])
                print(L[i], L[j])
                if len(L[i]) == len(L[j+1]):

                    nombreDePaires += 1

    return nombreDePaires
    
liste = list(input("Entrez une liste et separe les mots avec une virgule: ").split(","))
print(nyasa(liste))
