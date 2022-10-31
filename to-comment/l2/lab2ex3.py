def calcule_de_note_finale(devoirsMoyenne, partiel, examen):
    note = devoirsMoyenne*25/100 + partiel*25/100 + examen*50/100
    return(note)

devoirsMoyenne = float(input("Entrez la note de la moyenne des devoirs."))
partiel = float(input("Entrez la note partiel."))
examen = float(input("Entrez la note de l'examen."))

noteFinale = calcule_de_note_finale(devoirsMoyenne, partiel, examen)
print("La note finale est:", noteFinale)
