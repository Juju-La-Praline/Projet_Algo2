from Parse import *
from Graphic import *
from version_jsupSLM import *


def jsupSL(j, l, sl):
    """
    pour j un indice, une sous sequence sl de taille l,
    la fonction retourne True si T(j,l) est vrai, Faux sinon.
    """
    if l == 0 :       #il n'y a pas de bloc
        return True
                     #il y a au moins 1 bloc
    elif j < sl[l-1] - 1:   #j est trop petit
        return False
    
    elif j == sl[l-1] - 1: #il y a assez de place pour un bloc seuleument

        if l == 1:       

            return True
        else :
            return False
    else:                   #appel récursif case j noire ou blanche
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
    """
    retourne True si la ligne i de la grille a peut être coloriée 
    avec la séquence d'entiers associées à cette ligne, False sinon.
    
    """
    #print(a.M)
    for indice in range(a.M) :  #parcours de toutes les cases de la ligne
        
        #print(indice)
        #print("indice=",indice,"i=",i)
        if a.Gr[i][indice] == -1:  #si une case est indéterminée
            a.Gr[i][indice]= 2     
            D= dict()              
            #print(i,len(a.tabil[i]), a.tabil[i], a.Gr[i])
            #test si un coloriage possible quand la case est noire
            noirV = jsupSLMO(a.M-1, len(a.tabil[i]), a.tabil[i], a.Gr[i], D) 
            #print("noirV ",noirV)
            #print(a.Gr[i])
            a.Gr[i][indice]= 1   
            D1= dict()
            #test si un coloriage possible quand la case est blanche
            blancV = jsupSLMO(a.M-1, len(a.tabil[i]), a.tabil[i], a.Gr[i], D1)
            
            #print("blancV ",blancV)
            #print(a.Gr[i])
            if noirV :    #si coloriage possible de la ligne qd la case est noire
                if blancV:  #si coloriage possible de la ligne qd la case est blanche
                    a.Gr[i][indice] = -1  #on ne sait pas la vraie couleur donc c'est indéterminée
                    
                    
                else :       #coloriage impossible quand la case est blanche
                    a.Gr[i][indice]= 2   #la case est noire
                    a.SetLi+=[indice]    #ajout de la colonne à la liste des colonnes modifiées
                    
                    
            else :
                if not(blancV):  #si ni noir ni blanc
                    return False  #coloriage impossible

                a.Gr[i][indice]= 1   #sinon la case est blanche
                a.SetLi+=[indice]    #ajout de la colonne à la liste des colonnes modifiées
            
            
    
    #print("fin")                 
    return True

def colorC(a,j):
    """
    retourne True si la colonne j de la grille a peut être coloriée 
    avec la séquence d'entiers associées à cette colonne, False sinon.
    
    """
    #print("rentre")
    colonne=[i[j] for i in a.Gr]  #liste des indices de la colonne j
    #print(colonne)
    for indice in range(a.N) :    #parcours des cases de la colonne
            if a.Gr[indice][j] == -1:   #si une case est indéterminée
                a.Gr[indice][j]= 2
                colonne[indice]=2      #mise à jour de la colonne
                D=dict()
                #test si un coloriage possible quand la case est noire
                noirV = jsupSLMO(a.N-1, len(a.tabic[j]), a.tabic[j], colonne, D)
                #print("noirV ",noirV)
                #print(colonne)
                a.Gr[indice][j]= 1
                colonne[indice]=1      #mise à jour de la colonne
                D1= dict()
                #test si un coloriage possible quand la case est blanche
                blancV = jsupSLMO(a.N-1, len(a.tabic[j]), a.tabic[j], colonne, D1)
                #print("blancV",blancV)
                #print("colonne",colonne)

                if noirV :       #si coloriage possible de la ligne qd la case est noire
                    if blancV:   #si coloriage possible de la ligne qd la case est blanche
                        a.Gr[indice][j] = -1   #on ne sait pas la vraie couleur donc c'est indéterminée
                        colonne[indice]= -1    #mise à jour de la colonne
                        
                    else :                   #coloriage impossible quand la case est blanche
                        a.Gr[indice][j]= 2   #la case est noire
                        colonne[indice]=2    
                        a.SetCi+=[indice]    #ajout de la colonne à la liste des colonnes modifiées
                        
                        
                else :
                    if not(blancV):
                        return False

                    a.Gr[indice][j]= 1    #la case est blanche
                    a.SetCi+=[indice]    #ajout de la colonne à la liste des colonnes modifiées
                    
                #print("setCi",a.SetCi)
    #print(a.SetCi)
    return True # colonne recupe


def coloration2(A):
    """
    affiche la grille A coloriées si possible ainsi que les séquences d'entiers
    des lignes et colonnes correspondantes
    
    """
    a = A                  #a grille

    colonneAvoir = [i for i in range(len(a.tabic))]
    ligneAvoir = [i for i in range(len(a.tabil))]
    #print(colonneAvoir)
    #print(ligneAvoir)
    verif = False               #variable pour vérifier si coloration possible d'une ligne
    verif2 = False              #variable pour vérifier si coloration possible d'une colonne
    verif3 = True               #variable pour vérifier si toutes les cases sont coloriées
    verif4 = "ne sait pas"      # cas où toutes mes cases ne sont pas coloriées à la fin de l'algo
    nouv= []
    nouv2 =  []
    while ligneAvoir != [] or colonneAvoir != [] : #tant qu'il reste des cas à examiner
        
        #print("ligne",ligneAvoir)
        #print("colonne",colonneAvoir)
        for i in ligneAvoir :     #parcours des lignes 
            #print(i)
            verif = colorL(a,i)
            
            if not(verif):    #si coloriage impossible retourne False
                return False
            #print("setli",a.SetLi)
            nouv += [i for i in a.SetLi if i not in nouv] #ajout à nouv des colonne où une case a été coloriée 
            #affichage_fenetre(a)
            #print("nouv",nouv)
            colonneAvoir += [i for i in nouv if i not in colonneAvoir] #ajout dans les colonnes à voir
            #print("colonneavoir",colonneAvoir)
            #print(colonneAvoir)
            #print("ligneavoir3",ligneAvoir)
            
            a.SetLi = []   #remise à zéro de la liste des colonnes modifiées lors d'un appel à colorL(a,i)
            
            
        ligneAvoir=[]
        nouv = []

        for j in colonneAvoir :   #parcours des colonnes
            #print(j)
            verif2 = colorC(a,j)
            #print("sprez")
            if not(verif2):
                return False

            nouv2 += [i for i in a.SetCi if i not in nouv2] #ajout à nouv des lignes où une case a été coloriée  
            #print("nouv2",nouv2)
            #affichage_fenetre(a)
            ligneAvoir += [i for i in nouv2 if i not in ligneAvoir] #ajout aux lignes à voir
            #print("ligneavoir",ligneAvoir)
            
            
            a.SetCi = []   #remise à zéro de la liste des lignes modifiées lors d'un appel à colorC(a,j)
        colonneAvoir = []
        nouv2 = []
        
        
        
    affichage_fenetre(a)
    
    #verifie si toute la grille est coloriée
    verif3 = a.EstComplete(0)   # verif3 = True si toutes les cases sont coloriées
    print(a.Kp)
    if verif3 == True:
       
        print(verif3)
        return verif3
    else :
        print(verif4)            # toutes les cases ne sont pas coloriées
        return verif4
    



