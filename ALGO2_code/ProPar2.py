from Projet2 import *


def enumeration(A): 
    ok = coloration2(A)
    a=A
    if ok == False:
       return False
    else:
        print (a.Kp)
        enum_rec(a,a.Kp,1) or enum_rec(a,a.Kp,2)
        

def enum_rec(A,indice,c):
    if indice == A.N * A.M:
        return True
    i = indice // A.M 
    j = indice % A.M
    print("i ",i,"j ",j)
    
    ok=coloration_propagation(A,i,j,c)
    a=A
    if ok == False:
        return False
    if ok == True:
        return True
    
    a.EstComplete(1)
    return enum_rec(a,a.Kn,1) or enum_rec(a,A.Kn,2)

def coloration_propagation(A,i,j,c):
    a = A #a
    a.Gr[i][j]= c
    coloneAvoir = [j]
    ligneAvoir = [i]
    print(coloneAvoir)
    print(ligneAvoir)
    verif = False
    verif2 = False
    verif3 = True
    verif4 = "ne sait pas"
    nouv= []
    nouv2 =  []
    while ligneAvoir != [] or coloneAvoir != [] :
        
        #print("ligne",ligneAvoir)
        #print("colone",coloneAvoir)
        for i in ligneAvoir :
            #print(i)
            verif = colorL(a,i)
            
            if not(verif):
                return False
            #print("setli",a.SetLi)
            nouv += [i for i in a.SetLi if i not in nouv] #colone j ou une case a eté  coloriée 
            #affichage_fenetre(a)
            #print("nouv",nouv)
            coloneAvoir += [i for i in nouv if i not in coloneAvoir]
            #print("coloneavoir",coloneAvoir)
            #print(coloneAvoir)
            #print("ligneavoir3",ligneAvoir)
            
            a.SetLi = []
        ligneAvoir=[]
        nouv = []

        for j in coloneAvoir :
            #print(j)
            verif2 = colorC(a,j)
            #print("sprez")
            if not(verif2):
                return False

            nouv2 += [i for i in a.SetCi if i not in nouv2] #colone j ou une case a eté  coloriée 
            #print("nouv2",nouv2)
            #affichage_fenetre(a)
            ligneAvoir += [i for i in nouv2 if i not in ligneAvoir]
            #print("ligneavoir",ligneAvoir)
            
            
            a.SetCi = []
        coloneAvoir = []
        nouv2 = []
        
        #verifier si cases coloriées verif 3
        
    #affichage_fenetre(a)
    verif3 = a.EstComplete(0)
    
    if verif3 == True:
       
        
        return verif3
    else :
        
        return verif4


