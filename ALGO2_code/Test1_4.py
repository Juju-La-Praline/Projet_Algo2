from Generalisation1_2 import *
from Graphic import * 
from Propagation1_3 import *
from Parse import *
from MethodeComplete2_1 import *
import time

test = 2

fichier=['0.txt','1.txt','2.txt','3.txt','4.txt','5.txt','6.txt','7.txt','8.txt','9.txt','10.txt','11.txt','12.txt','13.txt','14.txt','15.txt','16.txt']

if test == 0:    
    g1 = creer_grille2(fichier[10])

    verif1,g2=coloration2 (g1)
    affichage_fenetre(g2)

if test == 1:    
    g1 = creer_grille2(fichier[10])

    verif2,g3 = enumeration(g1)
    affichage_fenetre(g3)

if test == 2 :
    temp = 0
    
    n = 5
    for i in range(0,n):
        debut = time.time()
        g = creer_grille2(fichier[0])
        verif2,g4 = coloration2(g)
        #verif2,g4 = enumeration(g)
        fin = time.time()
        temp += fin - debut

    print( "Temps d'exécution moyen : ", temp/n)

if test == 3: #test de resolution complete pour toute les grilles 
    tempt = 0
    debut = time.time()
    for i in fichier:
        
        tempslo=time.time()
        g = creer_grille2(i)
        #res = coloration2(g)
        verif2,g4 = enumeration(g)
        tempslo2=time.time()
        tempslo3=tempslo2-tempslo
        print(i,"fait",tempslo3)
    fin = time.time()
    tempt += fin - debut
    print(tempt)

if test == 4:
    tempt = 0
    debut = time.time()
    for i in fichier:
        
        tempslo=time.time()
        g = creer_grille2(i)
        verif2,g4  = coloration2(g)
        
        tempslo2=time.time()
        tempslo3=tempslo2-tempslo
        print(i,"fait",tempslo3)
    fin = time.time()
    tempt += fin - debut
    print(tempt)
    
