
from Parse import *
from Graphic import *


def jsupSL(j, l, sl):# l taille de la sous sequence  , S la sous sequence
    if l == 0 :
        return True

    elif j < sl[l-1] - 1:

        return False
    elif j == sl[l-1] - 1:

        if l == 1:

            return True
        else :
            return False
    else:
        return jsupSL(j - sl[l-1] - 1, l - 1, sl ) or jsupSL(j - 1, l, sl)  


#rendre en dynamique (retenir les res des difference valeur de j et l)
def jsupSLM(j, l, sl, ligne):# l taille de la sous sequence  , S la sous sequence
    #print("\n")
    
    #print("jsupSLMP(j=",j,", l=",l,", sl, ligne)")
    if l == 0 :
        for ti in ligne[0:j+1] :
            if ti == 2:
                #print("false")
                return False
        #print("true")
        return True

    elif j < sl[l-1] - 1:
        #print("false")
        return False

    elif j == sl[l-1] - 1:#
        if l == 1:
            for tti in ligne[0:j+1]:
                if tti == 1:
                    return False
            #print("true")
            return True
            
        else :
            #print("false")
            return False

    if ligne[j] == -1:
        #print("ligne[j-1]==-1")
        for i in ligne[j - sl[l-1]+1:j ] : # cas une case blanche dans sl dans la suite 
            #print(i)
            if i == 1 :
                #print("pas noire")
                return jsupSLM(j - 1, l, sl, ligne)
        """if j-sl[l-1] +1 < 0: #cas pas la place de mettre les cases noires
            #print("j-sl[l-1] < 0:")
            #print("false")
            return jsupSLM(j - 1, l, sl, ligne)"""
            
            
        if ligne[j - sl[l-1]] == 2: 
                #print("ligne[j-sl[l-1]-1] == 2:")
                #print("false")
                return jsupSLM(j - 1, l, sl, ligne) # cas une case noire de trop par rapport a la taille

        """if j-sl[l-1] +1 == 0: #cas pile la place de mettre les cases noires
            #print("j-sl[l-1] == 0:")
            #print("true")
            return True"""
        

        #print("ne sais pas")        
        return jsupSLM(j - sl[l-1]-1, l-1, sl, ligne) or jsupSLM(j - 1, l, sl, ligne)   


    if ligne[j] == 1:#blanc

        #print("ligne[j-1]==1")
        return jsupSLM(j - 1, l, sl, ligne) # case blanche


    if ligne[j] == 2:#noire

        #print("ligne[j-1]==2:")
        for i in ligne[j - sl[l-1]+1:j ] : # cas une case blanche dans sl dans la suite 
            if i == 1:
                #print("false")
                return False
            
        """if j-sl[l-1] +1 < 0: #cas pas la place de mettre les cases noires
            #print("j-sl[l-1] < 0:")
            #print("false")
            return False"""

        """if j-sl[l-1] +1 == 0: #cas pile la place de mettre les cases noires
            #print("j-sl[l-1] == 0:")
            #print("true")
            return True
        else :"""
            
        if ligne[j - sl[l-1]] == 2: 
                #print("ligne[j-sl[l-1]-1] == 2:")
                #print("false")
            return False # cas une case noire de trop par rapport a la taille 
        else :

            return jsupSLM(j - sl[l-1] -1, l - 1, sl, ligne) # cas case noire trouvée 




def colorL(a,i):
    #print(a.M)
    for indice in range(a.M) :
        
        #print(indice)
        #print("indice=",indice,"i=",i)
        if a.Gr[i][indice] == -1:
            a.Gr[i][indice]= 2
            #print(i,len(a.tabil[i]), a.tabil[i], a.Gr[i])
            noirV = jsupSLM(a.M-1, len(a.tabil[i]), a.tabil[i], a.Gr[i])#test avec case noir 
            #print("noirV ",noirV)
            #print(a.Gr[i])
            a.Gr[i][indice]= 1
            
            blancV = jsupSLM(a.M-1, len(a.tabil[i]), a.tabil[i], a.Gr[i])#test avec case bblanche
            
            #print("blancV ",blancV)
            #print(a.Gr[i])
            if noirV :
                if blancV:
                    a.Gr[i][indice] = -1
                    
                    
                else :
                    a.Gr[i][indice]= 2
                    a.SetLi+=[indice]
                    
                    
            else :
                if not(blancV):
                    return False

                a.Gr[i][indice]= 1
                a.SetLi+=[indice]
            
            
    
    #print("fin")                 
    return True

def colorC(a,j):
    #print("rentre")
    colone=[i[j] for i in a.Gr]
    #print(colone)
    for indice in range(a.N) :
            if a.Gr[indice][j] == -1:
                a.Gr[indice][j]= 2
                colone[indice]=2
                noirV = jsupSLM(a.N-1, len(a.tabic[j]), a.tabic[j], colone)#test avec case noir 
                #print("noirV ",noirV)
                #print(colone)
                a.Gr[indice][j]= 1
                colone[indice]=1
                blancV = jsupSLM(a.N-1, len(a.tabic[j]), a.tabic[j], colone)#test avec case bblanche
                #print("blancV",blancV)
                #print("colone",colone)

                if noirV :
                    if blancV:
                        a.Gr[indice][j] = -1
                        colone[indice]= -1
                        
                    else :
                        a.Gr[indice][j]= 2
                        colone[indice]=2
                        a.SetCi+=[indice]
                        
                        
                else :
                    if not(blancV):
                        return False

                    a.Gr[indice][j]= 1
                    a.SetCi+=[indice]
                    
                #print("setCi",a.SetCi)
    #print(a.SetCi)
    return True # colone recupe


def coloration(A):#a grille
    a = A #a

    coloneAvoir = [i for i in range(len(a.tabic))]
    ligneAvoir = [i for i in range(len(a.tabil))]
    print(coloneAvoir)
    print(ligneAvoir)
    verif = False
    verif2 = False
    verif3 = "ne sait pas"
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
        
    affichage_fenetre(a)
    print(verif3)
    return verif3

