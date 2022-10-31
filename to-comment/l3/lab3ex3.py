def estDivisible(nombre):
    if nombre/2 == nombre//2:
        nombreDiv2 = True
    else:
        nombreDiv2 = False
#si le nombre divise et le nombre divise arrondi est le meme, c'est divisible par 2^
    if nombre/3 == nombre//3:
        nombreDiv3 = True
    else:
        nombreDiv3 = False
#si le nombre divise et le nombre divise arrondi est le meme, c'est divisible par 3^
    if nombreDiv2 == True and nombreDiv3 == True:
        return 1 #si le nombre est divisible par 2 et 3, on retourne 1
    elif nombreDiv2 == True and nombreDiv3 == False:
        return 2 #si le nombre est divisible par 2 mais pas par 3, on retourne 2
    elif nombreDiv2 == False and nombreDiv3 == True:
        return 3 #si le nombre est divisible par 3 mais pas par 2, on retourne 3
    elif nombreDiv2 == False and nombreDiv3 == False:
        return 0 #si le nombre est ni divisible par 2 ou 3, on retourne 0

nombre = int(input("Entrez un nombre: ")) #demande un nombre
divisibilite = estDivisible(nombre) #cherche si le nombre est divisible par 2 ou 3

if divisibilite == 1: #si 'divisibilite' est egal a 1, le nombre est divisble par 2 et 3
    print(nombre, "est divisible par 2 et par 3.")
elif divisibilite == 2: #si 'divisibilite' est egal a 2, le nombre est divisble par 2 mais pas par 3
    print(nombre, "est divisible par 2 mais pas par 3.")
elif divisibilite == 3: #si 'divisibilite' est egal a 3, le nombre est divisble par 3 mais pas par 2
    print(nombre, "est divisible par 3 mais pas par 2.")
elif divisibilite == 0: #si 'divisibilite' est egal a 0, le nombre est ni divisble par 2 ou 3
    print(nombre, "n'est pas divisible ni par 2 ni par 3.")
