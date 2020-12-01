from Generalisation1_2 import *
from Graphic import * 
from Propagation1_3 import *
from Parse import *
from MethodeComplete2_1 import *
import time

a1='0.txt'
a2='1.txt'
a3='16.txt'
test = 1
if test == 1:    
    g1 = creer_grille2(a3)

    #res=coloration2 (g1)
    #affichage_fenetre(g1)

    g2 = enumeration(g1)
    #affichage_fenetre(g1)

if test == 2 :
    temp = 0
    a = '16.txt'

    for i in range(0,5):
        debut = time.time()
        g = creer_grille2(a)
        #res = coloration2(g)
        res = enumeration(g)
        fin = time.time()
        temp += fin - debut

    print( "Temps d'exécution moyen : ", temp/5)