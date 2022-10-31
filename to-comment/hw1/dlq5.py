import math
def fun(x):
    y = (math.log10(x+3))/4
    return y
#En premier, on ajoute le 3 au 'x'. Ensuite on trouve l'logarithme pour..
#..connaitre l'exposant. Finalement, on le divise par quatre (parce que 4y/4=y).
x = float(input("Entrez une valeur pour x: "))
y = fun(x) #On cherche la valeur et on l'imprime.
print(y)
