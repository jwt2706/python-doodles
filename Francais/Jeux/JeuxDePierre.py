#Le joueur qui ramasse la derniere pierre remporte la partie.
#Tu ne peut pas ramasser tout les pierre d'un coup.

pile = 20
MAX = 5 #place les valeurs de default
joueur = 0

while pile > 0: #le jeu continue tant qu'il y a des pierres qui reste dans la pile
    if pile < 5: #si la pile est de moins que 5, la valeur maximal decent
        MAX = pile
    print("Il reste", pile, "pierre dans la pile. Tour du joueur", joueur + 1, ":") #det a qui c'est le tour de jouer
    reponse = int(input("Combien de pierres voulez-vous bouger?")) #demande combien de pierre le joueur veut prendre
    if reponse <= MAX: #si la reponse est valide...
        pile = pile - reponse #...la pile diminue en rapport avec la reponse
        joueur ^= 1 #ensuite on donne le tour a l'autre joueur
    else:#si la reponse n'est pas valide, on demande de donner une autre valeur
        print("SVP entrez une valeur valide, sois entre 1 et", MAX, ".")
print("Bravo! Joueur", joueur + 1, "a gangne la partie. Le jeu est termine.")
#finalement, quand il reste aucune pierre, on deduit le gangnant^
