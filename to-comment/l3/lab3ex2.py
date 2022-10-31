temp = float(input("Entrez la temperature de l'exterieur: "))
#demande la temperature^
if temp >= 80:
    numactivite = 1 #si la temperature est plus ou egal a 80, 'numactivite' est egal a 1
elif temp >= 60 and temp < 80:
    numactivite = 2 #si la temperature est plus ou egal a 60 mais est plus petit que 80, 'numactivite' est egal a 2
elif temp >= 40 and temp < 60:
    numactivite = 3 #si la temperature est plus ou egal a 40 mais est plus petit que 60, 'numactivite' est egal a 3
elif temp < 40:
    numactivite = 4 #si la temperature est plus petit que 40, 'numactivite' est egal a 4

if numactivite == 1: #si 'numactivite' est egal a 1, on reccomande la natation
    print("L'activite recommande pour vous est la natation.")
elif numactivite == 2: #si 'numactivite' est egal a 2, on reccomande le soccer
    print("L'activite recommande pour vous est le soccer.")
elif numactivite == 3: #si 'numactivite' est egal a 3, on reccomande le volleyball
    print("L'activite recommande pour vous est le volleyball.")
elif numactivite == 4: #si 'numactivite' est egal a 4, on reccomande le ski
    print("L'activite recommande pour vous est le ski.")
