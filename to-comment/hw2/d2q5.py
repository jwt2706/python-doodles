feu_couleur = str(input("Entrez la couleur du feu de circulation: "))
#demande la couleur du feu^
if feu_couleur == 'rouge':
    print("Arretez!")#si c'est rouge, arrete
elif feu_couleur == 'jaune':
    print("Ralentissez!")#si c'est jaune, ralentis
elif feu_couleur == 'vert':
    print("Avancez!")#si c'est vert avance
else:
    print("Faites attention!") #si autre, fait attention
