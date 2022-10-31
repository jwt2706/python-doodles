#Question 5 - Devoir 4
# Jeu de cartes appelé "Pouilleux" 

# L'ordinateur est le donneur des cartes.

# Une carte est une chaine de 2 caractères. 
# Le premier caractère représente une valeur et le deuxième une couleur.
# Les valeurs sont des caractères comme '2','3','4','5','6','7','8','9','10','J','Q','K', et 'A'.
# Les couleurs sont des caractères comme : ♠, ♡, ♣, et ♢.
# On utilise 4 symboles Unicode pour représenter les 4 couleurs: pique, coeur, trèfle et carreau.
# Pour les cartes de 10 on utilise 3 caractères, parce que la valeur '10' utilise deux caractères.

import random

def attend_le_joueur():
    '''()->None
    Pause le programme jusqu'au l'usager appui Enter
    '''
    try:
         input("Appuyez Enter pour continuer. ")
    except SyntaxError:
         pass
    
def prepare_paquet():
    '''()->list of str
        Retourne une liste des chaines de caractères qui représente tous les cartes,
        sauf le valet noir.
    '''
    paquet=[]
    couleurs = ['\u2660', '\u2661', '\u2662', '\u2663']
    valeurs = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
    for val in valeurs:
        for couleur in couleurs:
            paquet.append(val+couleur)
    paquet.remove('J\u2663') # élimine le valet noir (le valet de trèfle)
    return paquet

def melange_paquet(p):
    '''(list of str)->None
       Melange la liste des chaines des caractères qui représente le paquet des cartes    
    '''
    random.shuffle(p)

def donne_cartes(p):
     '''(list of str)-> tuple of (list of str,list of str)

     Retournes deux listes qui représentent les deux mains des cartes.  
     Le donneur donne une carte à l'autre joueur, une à lui-même,
     et ça continue jusqu'à la fin du paquet p.
     '''     
    donneur=[]
    autre=[]

    donneaudonneur = False
    for x in range(51): #repete pour toutes les cartes
        if donneaudonneur == True:
            donneur.append(p[x]) #donne un au donneur
            donneaudonneur = False
        else:
            autre.append(p[x])#donne un au joueur
            donneaudonneur = True
    return (donneur, autre) #retourne les cartes de chaqun


def elimine_paires(l):
    '''
     (list of str)->list of str

     Retourne une copy de la liste l avec tous les paires éliminées 
     et mélange les éléments qui restent.

     Test:
     (Notez que l’ordre des éléments dans le résultat pourrait être différent)
     
     >>> elimine_paires(['9♠', '5♠', 'K♢', 'A♣', 'K♣', 'K♡', '2♠', 'Q♠', 'K♠', 'Q♢', 'J♠', 'A♡', '4♣', '5♣', '7♡', 'A♠', '10♣', 'Q♡', '8♡', '9♢', '10♢', 'J♡', '10♡', 'J♣', '3♡'])
     ['10♣', '2♠', '3♡', '4♣', '7♡', '8♡', 'A♣', 'J♣', 'Q♢']
     >>> elimine_paires(['10♣', '2♣', '5♢', '6♣', '9♣', 'A♢', '10♢'])
     ['2♣', '5♢', '6♣', '9♣', 'A♢']
    '''
    
    resultat=[]
    doubles = []

    x = 0
    l.sort() #met 'l' en ordre
    while x < len(l):
        doubles.append(l[x][0])#'doubles' est la meme chose que 'l' mais seulment avec le premier caractere de chaque chaine (cartes)
        x = x + 1
    x = 0
    while x < len(l) - 1:
        if (doubles[x] != doubles[x + 1]): #si une carte n'est pas le meme que son voisin (la liste est en ordre), on l'ajoute a 'resultat'
            resultat.append(l[x])
            x = x + 1
        else:
            x = x + 2 #si oui, on les saute pour qu'ils soivent elimine
    if x == (len(l) - 1):
        resultat.append(l[x]) #ajoute la derniere carte si les deux derniere cartes ne sont pas le meme

    random.shuffle(resultat)#melange les cartes
    return resultat


def affiche_cartes(p):
    '''
    (list)-None
    Affiche les éléments de la liste p séparées par d'espaces
    '''
    print(*p) #imprime la liste avec un espace entre chaque carte

def entrez_position_valide(n):
     '''
     (int)->int
     Retourne un entier du clavier, de 1 à n (1 et n inclus).
     Continue à demander si l'usager entre un entier qui n'est pas dans l'intervalle [1,n]
     
     Précondition: n>=1
     '''
    print("C'est votre tour.")
    print("J'ai", n, "carte(s). Choissisez un nombre entre 1 et", n, ": ", end="")
    choixdecarte = float(input()) #on prend des floats pour prevenir les erreurs si le jouer decide de mettre ca comme choix de carte
    while choixdecarte - int(choixdecarte) != 0 or choixdecarte > n or choixdecarte < 1:
        print("Je n'ai pas cette carte. Choissisez entre 1 et", n, ": ", end="") #redomande justque la reponse donne sois juste
        choixdecarte = float(input())
    choixdecarte = int(choixdecarte) #convertis la reponse en int (raison du float sur la ligne 84)
    print("Vous avez pris ma carte", choixdecarte, ".")
    choixdecarte = choixdecarte - 1 #pour trouver la bonne carte dans la liste (les listes commence a 0 et non 1)
    return choixdecarte

def brise_ligne():
    print("*********************************************************************************")

    
def joue():
    '''()->None
    Cette fonction joue le jeu'''
    
    p=prepare_paquet()
    melange_paquet(p)
    tmp=donne_cartes(p)
    donneur=tmp[0]
    humain=tmp[1]
    print("Bonjour. Je m'appelle Robot et je distribue les cartes.")
    print("Votre main est:")
    affiche_cartes(humain)
    print("Ne vous inquiétez pas, je ne peux pas voir vos cartes ni leur ordre.")
    print("Maintenant défaussez toutes les paires de votre main. Je vais le faire moi aussi.")
    attend_le_joueur()
    brise_ligne()
     
    donneur=elimine_paires(donneur)
    humain=elimine_paires(humain)

    while len(humain) > 1 or len(donneur) > 1:
        carte = entrez_position_valide(len(donneur)) #on choisis la carte qu'on veut
        print("La carte que vous avez recu est le", donneur[carte], ".")
        humain.append(donneur[carte]) #on nous donne la carte
        donneur.pop(carte)
        print("Voici vos cartes:")
        if len(humain) != 0: #s'il ne reste plus de carte, le jeux se termine
            affiche_cartes(humain)
        else:
            joueurgange = False
            break
        humain = elimine_paires(humain)
        print("Et revoici vos cartes apres avoir elimine vos double(s): ")
        affiche_cartes(humain)
        attend_le_joueur()
        brise_ligne()

        cartepris = random.randint(1, len(humain)) #l'ordinateur choisis une carte
        print("Mon Tour.\nJe prend votre carte", cartepris, ", c'est le", humain[cartepris - 1], ".")
        donneur.append(humain[cartepris - 1])
        humain.pop(cartepris - 1) #la carte est donne
        if len(humain) != 0: #on verifie si on a encore des cartes, sinon le jeu est termine
            print("Voici vos carte maintenant: ", end='')
            affiche_cartes(humain)
        else:
            joueurgange = True
            break
        donneur = elimine_paires(donneur)
        attend_le_joueur()
        brise_ligne()


    if joueurgange == True:
        print("Bravo, vous avez gange!")
    else:
        print("Bel essai, mais j'ai gange cette fois.")
# programme principale
joue()

