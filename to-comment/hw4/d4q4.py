
def read_raw(file):
    raw = open(file).read().splitlines() #open and reads file then returns it in a list named 'raw'
    for i in range(len(raw)):
        raw[i]=raw[i].strip()
    return raw


def clean_up(l):
    '''list of str->list of str
    La fonction prend en entrée une liste de caractères.
    Elle renvoie une nouvelle liste contenant les mêmes caractères que l
    sauf que un de chaque caractère apparaissant un nombre impair de fois
    dans l est supprimé et tous les caractères * sont supprimés 

    >>> clean_up(['A', '*', '$', 'C', '*', '*', 'P', 'E', 'D', 'D', '#', 'D', 'E', 'B', '$', '#'])
    ['#', '#', '$', '$', 'D', 'D', 'E', 'E']

    >>> clean_up(['A', 'B', '*', 'C', '*', 'D', '*', '*', '*', 'E'])
    []
    '''
    clean_board=[]
    l.sort()
    cleanDict = {}
    for i in l:
        if i in cleanDict:
            cleanDict[i] = cleanDict[i] + 1
        else:
            cleanDict[i] = 1

    for key in cleanDict:
        if key == "*":
            continue
        num = cleanDict[key]
        if num%2 != 0:
            num = num - 1
        if num != 0:
            for x in range(num):
                clean_board.append(key)
    
    return clean_board
    


def  is_rigorous(l):
    '''list of str->bool
    Renvoie True si chaque caractère de la liste apparaît exactement 2 fois ou si la liste est vide.
    Sinon, elle renvoie False. 
    
    Précondition: vous pouvez supposer que chaque élément de la liste apparaît un nombre pair de fois
    (c'est-à-dire que la liste est nettoyée par la fonction clean_up)
    >>>  is_rigorous(['E', '#', 'D', '$', 'D', '$', 'E', '#'])
    True
    >>>  is_rigorous(['A', 'B', 'A', 'A', 'A', 'B'])
    False
    '''
    # COMPLETEZ CETTE FONCTION EN CONFORMITE AVEC LA DESCRIPTION CI-DESSUS
    # AJOUTEZ VOTRE CODE ICI

    
#programme principal
file=input("Entrer le nom du fichier (Choix: 'file1.txt' 'file2.txt 'file3.txt' 'file4.txt'): ")
file=file.strip()
b=read_raw(file)
print("\nAvant clean-up:\n", b)
b=clean_up(b)
print("\nAprès clean-up:\n", b)
if is_rigorous(b):
    print("\nCette liste est maintenant rigoureuse; elle n’a aucun * et elle a "+str(len(b))+" caractères.")
else:
    print("\nCette liste n’a aucun * mais n'est pas rigoureuse et a "+str(len(b))+" caractères.")
     
