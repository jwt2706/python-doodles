def livres_et_onces_en_kilogrammes(livres, onces):
    livres = onces / 35.274 + livres #convertire les onces en livres et les ajouter ensembles
    kilos = livres / 2.2046 #convertire le tout en kilogrammes
    return kilos

v_livres = float(input("Entrez le nombre de livres."))
v_onces = float(input("Entrez le nombres d'onces.")) #demander des valeurs
kilogrammes = livres_et_onces_en_kilogrammes(v_livres, v_onces) #chercher la reponse converti
print(v_livres, "livres et", v_onces, "onces donne", kilogrammes, "kilogrammes.") #imprimer la reponse
