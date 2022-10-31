def conversion(kilogrammes, taille):
    IMC = kilogrammes/(taille**2) #converti les donnees en IMC
    return IMC

kilogrammes = float(input("Entrez votres poid en kilogrammes: "))
taille = float(input("Entrez votre taille en metre: ")) #demande des donnees
IMC = conversion(kilogrammes, taille) #on cherche la valeur IMC
print("Votre IMC est ", IMC)

if IMC<18.5: #si c'est plus petit que 18.5, l'utilisateur est maigre
    print("Maigreur")
elif 18.5<=IMC<25:#si c'est entre 18.5 et 25, l'utilisateur est a un poids ideal
    print("Poids ideal")
elif 25<=IMC<30:#si c'est entre 25 et 30, l'utilisateur est est surpoids
    print("Surpoids")
elif 30<=IMC:#si c'est plus grand que 30, l'utilisateur est obese
    print("Obesite")

