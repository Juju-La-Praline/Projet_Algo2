from Projet2 import *
from copy import *

def enumeration(A): 
    ok = coloration2(A)
    a = deepcopy(A)
    if ok == False:
       return False
    
    else:
        a.EstComplete(1)
        #print("oui")
        test=a.Kn
        return enum_rec(a,a.Kn,1) or enum_rec(a,test,2)
        
        
        

def enum_rec(A,indice,c):

    #if c == 2:
        #print("noire")
    if indice == A.N * A.M:
        return True
    #print("indice",indice,"N,M",A.N,A.M)
    i = indice // A.M 
    j = indice % A.M

    #print("i ",i,"j ",j,"azeazea")
    #print("fluteeeee",A.Kp)
    ok,a=coloration_propagation(A,i,j,c)
    
    if ok == False:
        #print("false")
        return False
    if ok == True:
        #print("true")
        #affichage_fenetre(a)
        return True
    
    a.EstComplete(1)
    #print("or sait pas",a.Kn)
    test=a.Kn
    return enum_rec(a,a.Kn,1) or enum_rec(a,test,2)

def coloration_propagation(A,i,j,c):
    a  = deepcopy(A)  #a
    a.Gr[i][j]= c
    #"print("a.Gr[i][j]",a.Gr[i][j])
    #affichage_fenetre(a)
    coloneAvoir = [j]
    ligneAvoir = [i]
    #print(coloneAvoir)
    #print(ligneAvoir)
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
                #print("cl false")
                return False,a 
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
                #print("cc false")
                return False,a 

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
    
    
    #print(a.Kn)
    verif3 = a.EstComplete(1)
    
    if verif3 == True:
       
        #print(verif3)
        return verif3,a 
    else :
        #print("ve4")
        return verif4,a


