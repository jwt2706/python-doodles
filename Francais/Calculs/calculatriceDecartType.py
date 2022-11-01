#calculatrice de l'ecart type
import math

n = list(map(int,input("Entrez des valeurs et separer les par un espace: ").split())) #demande des valeurs
a = (sum(n)/len(n))#on trouve 'a', qui les la moyenne des valeurs

x = 0
i = 0
for i in range(len(n)): #on trouve le nominateur de la premiere division...
    x = x + ((n[i] - a)**2) #...et on les ajoute ensemble
    
s = math.sqrt(x/n[-1]) #on complete la formule pour trouver 's'
print("L'ecart-type est", s, ".") #on imprime le resultat
