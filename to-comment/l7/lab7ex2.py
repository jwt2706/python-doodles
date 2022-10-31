def somme_de_trois(x):
    for i in range(len(x)-3):
        total = 0
        for item in range(3): #ajoute les trois premiere valeur consecutives retouvee dans le tuple 't'
            total = total + int(x[item]) #convertis l'item du tuple en int pour pouvoir faire l'addition
        if total == 0: #si le total est '0', on retourne 'True', sinon c'est 'False'
            return True
        else:
            return False

t = tuple(input("Svp entrez au moins 3 nombres separe par des vigrules: ").split(",")) #demande un tuple
print(somme_de_trois(t)) #imprime le resultat


'''exemple:
        >>> Svp entrez au moins 3 nombres separe par des vigrules: 1,2,-3,4,-1,3
        >>> True
'''
