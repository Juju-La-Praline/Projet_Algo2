from Propagation1_3 import *
from copy import *
from Graphic import *

def enumeration(A): 
    ok,a1 = coloration2(A)
    a = deepcopy(a1)
    if ok == False:
       return False
    
    else:
        a.EstComplete()

        ok1,b = enum_rec(a,a.Kn,1)

        if ok1 == False:
            ok2,c = enum_rec(a,a.Kn,2)
            return ok1 or ok2,c
        return ok1 or ok2,b
        #return enum_rec(a,a.Kn,1) or enum_rec(a,a.Kn,2)
        
        
        

def enum_rec(A,indice,c):

    
    if indice == A.N * A.M:
        return True,A
    
    i = indice // A.M 
    j = indice % A.M

    
    ok,a=coloration_propagation(A,i,j,c)
    
    if ok == False:
        
        return False,a
    if ok == True:
        
        #affichage_fenetre(a)
        return True,a
    
    a.EstComplete()
    
    ok1,b = enum_rec(a,a.Kn,1)
    if ok1 == False:
        ok2,c = enum_rec(a,a.Kn,2)
        return ok1 or ok2,c
    return ok1 or ok2,b
    #return enum_rec(a,a.Kn,1) or enum_rec(a,a.Kn,2)



def coloration_propagation(A,i,j,c):
    a  = deepcopy(A)  
    a.Gr[i][j] = c
    
    coloneAvoir = [j]
    ligneAvoir = [i]
    
    verif = False
    verif2 = False
    verif3 = True
    verif4 = "ne sait pas"
    nouv= []
    nouv2 =  []
    while ligneAvoir != [] or coloneAvoir != [] :
        
        
        for i in ligneAvoir :
            
            verif = colorL(a,i)
            
            if not(verif):
                
                return False,a 
            
            nouv += [i for i in a.SetLi if i not in nouv] #colone j ou une case a eté  coloriée 
            
            coloneAvoir += [i for i in nouv if i not in coloneAvoir]
            
            
            a.SetLi = []
        ligneAvoir = []
        nouv = []

        for j in coloneAvoir :
           
            verif2 = colorC(a,j)
            
            if not(verif2):
                
                return False,a 

            nouv2 += [i for i in a.SetCi if i not in nouv2] #colone j ou une case a eté  coloriée 
            
            ligneAvoir += [i for i in nouv2 if i not in ligneAvoir]
            
            
            
            a.SetCi = []
        coloneAvoir = []
        nouv2 = []
        
        
        
    
    
    
    
    verif3 = a.EstComplete()
    
    if verif3 == True:
       
        
        return verif3,a 
    else :
        
        return verif4,a


