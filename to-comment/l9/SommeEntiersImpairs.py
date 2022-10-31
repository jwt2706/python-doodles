# 1 + 3 + 5 + ...     (<= n)

def sommeEntiersImpairs(n):
 valeur = 1
 somme = 0
 while valeur <= n:
   somme = somme + valeur
   valeur = valeur + 2
 return somme  



n = int(input("SVP entrer un entier : "))
print("La somme des entiers impairs de 1 à",n, "est", sommeEntiersImpairs(n)) 
 
