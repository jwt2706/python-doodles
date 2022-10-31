# METTRE VOTRE NOM ET NUMÉRO D'ÉTUDIANT ICI
# Jacob Taylor 300273062
# En mettant votre nom ici, vous signez la déclaration d'intégrité de q4test2 


#########################
# QUESTION 5
#########################            
    
def tanganyika(L):
    '''(list of int)->list
    Precondition: len(L)>=1
    Cette fonction doit renvoyer une nouvelle liste Q. 

    >>> tanganyika([1,2,0,0,0,3,0])
    [1, 2, 0, 3, 0]
    >>> tanganyika([1,2,0,0,0,3,0,0,0,0])
    [1, 2, 0, 3, 0] 
    >>> tanganyika([0,0,1,0,2,0,0,0,3,0,0,0,0])
    [0, 1, 0, 2, 0, 3, 0]
    >>> tanganyika([1,2,0,3,0])
    [1, 2, 0, 3, 0]
    '''
    Q = []
    varZero = False #variable qui est 'True' si la valeur avant etait un zero
    for i in range(len(L)): #repete pour tous les nombres dans la liste 
        if int(L[i]) != 0 or varZero == False: #si le nombre n'est pas un zero ou il est une zero mais il n'y a pas eu de zero avant lui, on l'ajoute a 'Q'
            Q.append(L[i])
        if int(L[i]) == 0: #si le nombre est un zero, on change/garde 'varZero' a 'True'
            varZero = True
        else:
            varZero = False #sinon on le change/garde a 'False'  
    return Q #on retroune le resultat

liste = list(input("Entrez une liste et separe les nombres avec une virgule: ").split(","))#on demande une liste
print(tanganyika(liste)) #on affiche le resultat
