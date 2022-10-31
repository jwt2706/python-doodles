import math

def calcule_de_laire_du_triangle(c1, c2, c3):
    p = c1 + c2 + c3
    s = math.sqrt(p*(p-2*c1)*(p-2*c2)*(p-2*c3))/4
    return(s)

cote1 = float(input("Entrez la longeur du premier cote."))
cote2 = float(input("Entrez la longeur du deuxieme cote."))
cote3 = float(input("Entrez la longeur du troisieme cote."))

surface = calcule_de_laire_du_triangle(cote1, cote2, cote3)
print("La surface du triangle est:", surface)
