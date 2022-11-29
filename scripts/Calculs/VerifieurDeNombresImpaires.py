n = int(input("Entrez une valeur pour 'n': "))
p = int(input("Entrez une valeur pour 'p': "))
#demande des valeurs pour n et p^
print("Les valeurs de 'n' qui son inferieurs a 'p' sont:")
for x in range(n, p):
    print(x)
#utilise l'instruction range pour imprimer tous les nombres^
if (n//2) == (n/2):#regarde qui n est un nombre pair par diviser par deux
    n = n + 1 #si oui, on ajoute 1 a 'n' pour qu'on lis les nombre impaire
print("Les valeurs de 'p' qui sont impairs sont:")
for x in range(n, p, 2):
    print(x)
#utilise l'instruction range pour imprimer les nombre impaire avec bond de deux
