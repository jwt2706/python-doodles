import math
a = int(input("Entrez une valeur pour le coefficient 'a': "))
b = int(input("Entrez une valeur pour le coefficient 'b': "))
c = int(input("Entrez une valeur pour le coefficient 'c': "))
#demande des valeurs^
while a == 0: #si 'a' est egal a 0, on demande une autre valeur puisque si c'est 0 ce n'est plus une fonction parabolique
    print("La valeur 'a' ne peut pas etre egal a 0, sinon on n'a pas une fonction parabolique.")
    a = int(input("Entrez une autre valeur pour le coefficient 'a': "))
    
delta = (b**2) - (4*a*c) #calcul la valeur de delta

if delta < 0: #si delta est plus petit que 0, dit qu'il n'y a pas de racines reelles
    print("Il n'y a pas de racines reelles.")
elif delta == 0: #si delta est egal a 0, dit qu'il y a une seule racine reellee
    print("Il y a une seule racine reelle.")
elif delta > 0: #si delta est plus grand que 0, dit qu'il y a deux racines reelles
    print("Il y a deux racines reelles.")
