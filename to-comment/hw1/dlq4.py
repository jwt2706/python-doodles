def compte(monnaie, diviseur):
    if monnaie >= diviseur: #regarde si la valaeur est divisible
        nombredepieces = monnaie//diviseur #cherche combien de pieces peut entrer
    else:
        nombredepieces = 0 #sinon, le nombre de pieces est 0
    reste = monnaie % diviseur #cherche le reste
    return nombredepieces, reste

def numMonnaie(dollars_v):
    pieces25, pieces10, pieces5, pieces1 = 0, 0, 0, 0 #mettre toutes les valeurs a zero par defaut
    dollars = dollars_v * 100 #enlever les decimales par multiplier par 100
 
    pieces25, reste = compte(dollars, 25) #cherche combien de 25 cents peut enter
    pieces10, reste = compte(reste, 10) #combien de 10 cents avec le reste
    pieces5, reste = compte(reste, 5) #combien de 5 cents avec le reste 2
    pieces1, reste = compte(reste, 1) #combien de 1 cents avec le reste 3
    piecestotal = pieces25 + pieces10 + pieces5 + pieces1 #ajoute les pieces
    return piecestotal
    
dollars_v = float(input("Entrez le montant en dollars.")) #demander une valeur
piecestotal = numMonnaie(dollars_v) #cherche le resultat
print("Pieces total:", piecestotal) #imprimer le resultat
