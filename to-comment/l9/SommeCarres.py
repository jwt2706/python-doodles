# 1*1 + 2*2 + ... + n*n

def sommeCarees(n):
 valeur = 1
 somme = 0
 while valeur <= n:
   somme = somme + valeur * valeur
   valeur = valeur + 1
 return somme  


n = int(input("SVP entrer un entier : "))
print("La somme des carres de 1 à",n, "est", sommeCarees(n)) 
 
