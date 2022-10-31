import random

def devine(devine, reponse):
    if devine == reponse: #si la valeur devinee est egal a la reponse return true. sinon, false
        return True
    else:
        return False

reponse = random.randint(1, 10) #choisis un nombre entre 1 et 10 inclusivement
partieGagne = False #partiGagne est mis a false pour que le jeux est fonctionnel
nombre_dessais = 1 #le nombre d'essais est mis a 1 pour commencer

while partieGagne == False: #repete justqu'a que le jeux est termine
    devine_v = int(input("Devinez le nombre entre 1 et 10: ")) #demande une valeur
    reponse_c = devine(devine_v, reponse) #utilise la fonction pour voir si la valeur est la bonne ou non
    if reponse_c == True: #si oui, le jeux se termine et on dit bravo
        partieGagne = True
        print("Bravo vous avez gagne! Avec", nombre_dessais, "essais.")
    else: #si non, on ajoute q a le nombre d'essais et on dit si la valeur est plus grande ou petite que la reponse
        nombre_dessais = nombre_dessais + 1
        if devine_v < reponse:
            print("La valeur est plus grande.")
        else:
            print("La valeur est plus petite.")
