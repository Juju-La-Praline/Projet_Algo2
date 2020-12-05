from Propagation1_3 import *
from copy import *
from Graphic import *

def enumeration(A): 
    """  retourne la grille A coloriée (si possible) 
    """

    ok,a1 = coloration2(A)       #coloration partielle de A
    a = deepcopy(a1)

    if ok == False:            #si coloration impossible
       return False     
    
    else:
        a.EstComplete()         # appel qui détermine a.Kn = la prochaine case indéterminée
        ok1,b = enum_rec(a, a.Kn,1) #on considère que la case est blanche 

        if ok1 == False:        #si coloration impossible
            ok2,c = enum_rec(a, a.Kn,2)   #on considère que la case est noire
            return ok1 or ok2, c            #retourne un booléen et la grille modifiée
            
        return ok1 or ok2, b
        #return enum_rec(a,a.Kn,1) or enum_rec(a,a.Kn,2)
        
        
        

def enum_rec(A, indice, c):
    """ 
        fonction récursive qui colorie la case indice avec la couleur c
        et tente de colorier la grille A.
    """

    if indice == A.N * A.M:  #toutes les cases sont coloriées
        return True,A
    
    i = indice // A.M     #ligne de la case indice
    j = indice % A.M      #colonne de la case indice

    ok,a=coloration_propagation(A, i, j, c)  #colorie la case (i,j) avec la couleur c 
                                             #et tente de colorier la grille
    if ok == False:
        return False, A

    if ok == True:
        return True, a
    
    a.EstComplete()             #calcul de la prochaine case indéterminée
    
    ok1,b = enum_rec(a, a.Kn, 1)    #choix de la colorier en blanc
    if ok1 == False:
        ok2,c = enum_rec(a, a.Kn, 2)   #choix de la colorier en noir

        return ok1 or ok2, c

    return ok1 or ok2, b
    #return enum_rec(a,a.Kn,1) or enum_rec(a,a.Kn,2)



def coloration_propagation(A, i, j, c):
    a  = deepcopy(A)  
    a.Gr[i][j] = c
    
    coloneAvoir = [j]
    ligneAvoir = [i]
    
    verif = False                    #variable pour vérifier si coloration possible d'une ligne
    verif2 = False                   #variable pour vérifier si coloration possible d'une colonne
    verif3 = True                    #variable pour vérifier si toutes les cases sont coloriées
    verif4 = "ne sait pas"           # cas où toutes les cases ne sont pas coloriées à la fin de l'algo
    nouv= []
    nouv2 =  []
    while ligneAvoir != [] or coloneAvoir != [] :   #tant qu'il reste des cas à examiner
        
        
        for i in ligneAvoir :            #parcours des lignes
            
            verif = colorL(a, i)
            
            if not(verif):                #si coloriage impossible retourne False
                return False, A 
            
            nouv += [i for i in a.SetLi if i not in nouv]  #ajout à nouv des colonne où une case a été coloriée 
            
            coloneAvoir += [i for i in nouv if i not in coloneAvoir]    #ajout dans les colonnes à voir
            
            
            a.SetLi = []            #remise à zéro de SetLi = la liste des colonnes modifiées lors d'un appel à colorL(a,i)
            
        ligneAvoir = []
        nouv = []

        for j in coloneAvoir :      #parcours des colonnes
           
            verif2 = colorC(a, j)
            
            if not(verif2):
                return False, A 

            nouv2 += [i for i in a.SetCi if i not in nouv2] #ajout à nouv des lignes où une case a été coloriée 
            
            ligneAvoir += [i for i in nouv2 if i not in ligneAvoir]   #ajout aux lignes à voir
            
            
            
            a.SetCi = []    #remise à zéro de SetCi = la liste des lignes modifiées lors d'un appel à colorC(a,j)
        coloneAvoir = []
        nouv2 = []
        
       
    #verifie si toute la grille est coloriée
    verif3 = a.EstComplete()
    
    if verif3 == True:   # verif3 = True si toutes les cases sont coloriées
       
        return verif3,a 
    else :                  # toutes les cases ne sont pas coloriées
        
        return verif4,a    


