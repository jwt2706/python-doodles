def move_zeros(x):
    tmp = []
    for key in range(x.count("0")): #pour chaque '0' retrouve, on ajoute un zero a la liste 'tmp' et on l'enleve de la liste 'x'
        tmp.append("0")
        x.remove("0")
    for i in range(len(tmp)): #ensuite on ajoute tous les zeros de la liste 'tmp' dans 'x'
        x.append("0")
    print(x)#on imprime le resultat sans retourner la valeur
   
t = list(input("Entrez des valeurs spare par des vigules: ").split(","))#on demande une liste
move_zeros(t)#on bouge les zeros a la fin
