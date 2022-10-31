def move_zeros(x):
    nombresDeZeros = x.count("0")#compte le nombre de '0' qui se trouve dans la liste
    for i in range(nombresDeZeros):#pour chaque '0', on l'enleve et ensuite on le rajoute a la fin
        x.remove("0")
        x.append("0")
    print(x)#on imprime le resultat sans retourner une valeur
   
t = list(input("Entrez des valeurs spare par des vigules: ").split(","))#on demande une liste
move_zeros(t)#on bouge les zeros a la fin
