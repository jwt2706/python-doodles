def calculeFact(n):
    if n == 0: #si la valeur est 0, la factorielle est 1
        return 1
    else:
        nList = list(range(1, n+1)) #creer une liste avec tout les nombre qui serons utilise pour la factorielle
        i = len(nList)
        nMultiplie = 1
        while i > 1: #reccomence justqu'a toutes les multiples sont comptee
            nMultiplie = nMultiplie * nList[i-1] #multiplie les nombres
            i = i - 1 #dessendre 'i' de 1 pour que tout les nombres soient comptee
        return nMultiplie #retourne le tout

n = int(input("Entrez une valeur positive: "))
while n < 0: #demande une valeur positive, si on recois un negative on redemande
    n = int(input("La valeur doit etre positive. SVP reessayer: "))

resultat = calculeFact(n) #calcule la factorielle de la valeur
print("La valeur factorielle de", n, "est", resultat)#imprime le resultat
