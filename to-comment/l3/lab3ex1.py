age = int(input("Entrez votre age: "))
#demande l'age de l'utilisateur
if age >= 18 and age <= 55:
    bonage = True #si la valeur est egal ou entre 18 et 55 'bonage' est vrai
else:
    bonage = False #sinon, 'bonage' est faux

if bonage == True:
    print("Acceptee") #si 'bonage' est vrai, l'utilisateur est acceptee
else:
    print("Refuse") #sinon, l'utilisateur est refuse
