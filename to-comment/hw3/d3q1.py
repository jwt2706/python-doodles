import random
def effectuezTest(typeDeQuestion):
    print("SVP donnez les responses aux questions suivantes: ")
    bonneReponses = 0 #mettre les valeurs a leurs default
    compteur = 0
    while compteur <= 10: #refaire justqu'a que 'compteur' attein a 10
        compteur = compteur + 1 #ajouter 1 au compteur
        a = random.randint(0,9) #choisir une valeur pour 'a' et 'b'
        b = random.randint(0,9)
        if typeDeQuestion == 1: #demande une question dependant du mode
            print(a, "*", b, "=", end=' ')
        else:
            print(a, "+", b, "=", end=' ')
        r = int(input()) #demande une reponse
        if typeDeQuestion == 0 and r == a+b or typeDeQuestion == 1 and r == a*b:
            bonneReponses = bonneReponses + 1 #si la reponse est bonne, on ajoute 1 a 'bonneReponses'
            print("Bravo! On continue...")
        else: #sinon on donne la bonne reponse
            if typeDeQuestion == 0:
                print("Pas de chance! La reponse etait", a+b, ".")
            else:
                print("Pas de chance! La reponse etait", a*b, ".")
    print("Tu as", bonneReponses, "bonne reponses.") #imprime le nombre de bonne responses repondu
    if bonneReponses > 6:
        return True #si on a plus que 6 bonne reponse on retourne 'True'
    else:
        return False #sinon, on retourne 'False'

print("Ce logiciel va effectuez un test avec 10 questions...") #explique l'activite et demande quel type de questions l'utilisateur voudrais faire
reponse = int(input("Entrez '1' si vous voulez faire des multiplications ou '0' si vous voulez faire des additions: "))
resultat = effectuezTest(reponse) #lance l'activite

if resultat == True: #si resultat est 'True', imprime bravo
    print("Felicitation!")
else: #sinon, imprime demande de l'aide
    print("Demandez a votre enseignant(e) de vous aider.")
