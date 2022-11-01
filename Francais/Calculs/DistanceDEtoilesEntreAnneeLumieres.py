def anneessiderales_en_secondes(annees):#multiplie les annees par 525600 qui..
    secondes = (annees*525600)*60 #.. donne les minutes (365,26J * 24H * 60Min)
    return secondes #..et ensuite par 60 encore pour avoir les secondes. J'ai..
#..multiplie les secondes apres car le nombre de seconde dans une annee est trop eleve
def secondelumieres_en_kilometres(secondes):
    kilometres = secondes*300000 #multiplie les secondes par km/s de la lumiere
    return kilometres

annees1 = float(input("Etrez le nombre d'annes lumiere entre la Terre et la premiere etoile."))
annees2 = float(input("Etrez le nombre d'annes lumiere entre la Terre et la deuxieme etoile."))
#demander des valeurs en annees lumieres^
secondes1 = anneessiderales_en_secondes(annees1)
secondes2 = anneessiderales_en_secondes(annees2)
#convertire les annees lumieres en secondes lumieres^
kilometres1 = secondelumieres_en_kilometres(secondes1)
kilometres2 = secondelumieres_en_kilometres(secondes2)
#convertir les secondes lumieres en kilometres^
kilometres_t = kilometres1 + kilometres2
#ajoutes les kilos ensembles et imprime le resutlat
print("Il y a ", kilometres_t, "kilometres entres les deux etoiles via la Terre.")

