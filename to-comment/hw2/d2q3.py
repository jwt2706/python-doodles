import math
valeur_recu = int(input("Entez une valeur entiere: "))
#demande une valeur^
carre = math.sqrt(valeur_recu)#fait la racine carre du nombre donne
carre_r = round(carre)#arrondire le carre et le sauvegarder dand une autre variable
if carre_r == carre: #compare qui l'arrondi et le carre est le meme, si oui c'est un carre parfait
    print(valeur_recu, "est un carre parfait et sa racine est de", carre_r)
else:#si non, ce n'est pas un carre parfait
    print(valeur_recu, "n'est pas un carre parfait")
