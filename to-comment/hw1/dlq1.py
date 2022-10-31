livres = float(input("Entrez le nombre de livres."))
onces = float(input("Entrez le nombres d'onces.")) #demande des valeurs

livres_kg = livres / 2.205 #converti livres en kg
onces_kg = onces / 35.274 #converti onces en kg
kilos = onces_kg + livres_kg #ajoutes des deux ensembles

print(livres, "livres et", onces, "onces donne", kilos, "kilogrammes.")
