def verifChiffres(A, n):
    if n == 0: #arrete la recursivete si toutes les nombre on ete verifie
        return
    if int(A[n-1]) < 0 or int(A[n-1]) > 9: #regarde si les nombre sont en dehors de 0 et 9
        return False #si oui, retourne False
    return verifChiffres(A, n-1) #rend la fonction une fonction recursive

A = list(input("Entrez une liste avec chaque nombre separe par une virgule: ").split(",")) #demande une liste
if verifChiffres(A, len(A)) == False: #si la fonction a retourne False, pas tout les nombres sont entre 0 et 9
    print("Pas tout les nombres sont entre 0 et 9.")
else: #si la fonction ne retourne pas False, cela veut dire que tout les nombres sont entre 0 et 9
    print("Tous les nombres sont entre 0 et 9.")
