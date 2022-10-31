def pgcd(x, y):
    if x%y != 0: #si x mod y n'est pas egal a zero,
        x, y = y, x%y #calcule le plus grand diviseur avec modulo
        return pgcd(x, y) #rend la fonction recursive, et recommance justqu'a que le plus grand commun diviseur soit trouvee
    return y #apres que le pgcd est trouve, on le retoune ici (x mod y devrais etre egal a zero)

x = int(input("Entrez une valeur pour 'x': ")) #demande une valeur pour x
y = int(input("Entrez une valeur pour 'y': ")) #demande une valeur pour y
print("Le pgcd de", x, "et", y, "est:", pgcd(x, y)) #cherche le resultat et l'imprime
