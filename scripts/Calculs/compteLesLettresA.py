def compteV1(s, a):
    c = s.count(a) #compte le nombre de fois que 'a' se trouve dans la chaine 's'
    return c #retourne le resultat
def compteV2(s, a):
    c = 0 #on met le compeur a zero
    for i in range(len(s)): #on refait le bloc de code ci-dessous pour chaque caractere
        if s[i] == a: #si le caractere est 'a'...
            c = c + 1 #...on ajoute 1 au compteur
    return c #retourne le resultat

s = str(input("Entrez une chaine de caracteres: "))#demande une chaine

print(compteV1(s, 'a')) #cherche et imprime les reponses
print(compteV2(s, 'a'))
