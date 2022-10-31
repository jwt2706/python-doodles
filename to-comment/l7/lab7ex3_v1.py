def move_zeros(x):
    nombresDeZeros = 0
    tmp = []
    for i in range(len(x)):#pour toutes les valeurs dans la liste...
        if x[i] != "0":#...si c'est pas '0', on ajoute la valeur a la liste 'tmp'
            tmp.append(x[i])
        else:#sinon, on ajoute 1 au 'nombresDeZeros'
            nombresDeZeros = nombresDeZeros + 1
    for key in range(nombresDeZeros):#ensuite on ajoute les zeros a la fin
        tmp.append("0")
    return tmp#on retourne le resultat

t = list(input("Entrez des valeurs separe par des vigules: ").split(","))#on demande une liste
print(move_zeros(t))#on cherche et imprime les resultats
