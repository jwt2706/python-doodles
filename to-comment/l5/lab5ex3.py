import math

def calculeDistance(v):
    teta = 0
    resultats = []
    while teta <= 90: #pour chaque bond de 10 degrees, on calcule la distance
        teta_r = (math.pi/180)*teta #on trouve teta_r
        distance = (2*(v**2)*(math.cos(teta_r))*(math.sin(teta_r)))/9.8 #on trouve la distance
        teta = teta + 10 #on se prepare pour le prochain bond de 10 degrees
        resultats.append(distance) #on ajoute la reponse calcule dans la liste 'resultats'
    return resultats #on retourne la liste


v = float(input("Entrez une vitesse (metres par secondes): ")) #demande une vitesse
listeDistance = calculeDistance(v) #calcules des valeurs
n = 0
while n < 10: #imprime tous les resultats
    print("Si la balle est lancee a", n*10, "degres au-dessus de l'horizontale, la distance est de", listeDistance[n], "metres.")
    n = n + 1
