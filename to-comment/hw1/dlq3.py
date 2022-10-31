pieces25, pieces10, pieces5 = 0, 0, 0 #mettre toutes les valeurs a zero par defaut
dollars_v = float(input("Entrez le montant en dollars.")) #demander une valeur

dollars = dollars_v * 100 #enlever les decimales par multiplier par 100

if dollars >= 25: #si la valeur est plus grand ou egal a 25, elle va touver...
    pieces25 = dollars//25 #..combien de 25 cents on peut enter dans la valeur
reste = dollars % 25 #ensuite on calcule les restes pour les passer au 10

if reste >= 10: #si la valeur est plus grand ou egal a 10, elle va trouver...
    pieces10 = reste//10 #..combien de 10 cents on peut enter dans le reste
reste2 = reste % 10 #ensuite on calcule les restes pour les passer au 5

if reste2 >= 5: #si la valeur est plus grand ou egal a 5, elle va trouver...
    pieces5 = reste2//5 #..combien de 5 cents on peut enter dans le reste
reste = reste % 5 #ensuite on calcule les restes, qui serons des 1 cents

piecestotal = pieces25 + pieces10 + pieces5 + reste
print("Pieces de 25 cents:", pieces25)
print("Pieces de 10 cents:", pieces10)
print("Pieces de 5 cents:", pieces5)
print("Pieces de 1 cents:", reste) #on ajoute les pieces ensemble pour trouver..
print("Pieces total:", piecestotal) #..le total et on imprime les resultats
