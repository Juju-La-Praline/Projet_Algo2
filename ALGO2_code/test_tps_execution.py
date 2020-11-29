from Projet import *
from Parse import *
from Graphic import *
from Parse1 import *
from ProPar2 import *
import time

temp = 0
a = '5.txt'

for i in range(0,20):
    debut = time.time()
    g = creer_grille2(a)
    res = coloration2(g)
    fin = time.time()
    temp += fin - debut

print( "Temps d'exécution moyen : ", temp/20)
