from random import shuffle #importer la fonction 'shuffle()' de la bibliotheque 'random'

def coder(message):
    message = list(message) #convertir le message en liste
    shuffle(message) #reorganiser la liste avec 'shuffle()' de la bibliotheque 'random'
    messageSecret = "".join(message) #remettres les caracteres reorganisee dans un nouvau string 'messageSecret'
    return messageSecret #retourner le resultat
    
message = str(input("Entrez un message: ")) #demande un message
print(coder(message)) #cherche et imprime le resultat
