from Generalisation1_2 import *
from copy import *

def colorL(a,i):
    """
    retourne True si la ligne i de la grille a peut être coloriée 
    avec la séquence d'entiers associées à cette ligne, False sinon.
    
    """
    
    for indice in range(a.M) :  #parcours de toutes les cases de la ligne
        
        
        if a.Gr[i][indice] == -1:  #si une case est indéterminée
            a.Gr[i][indice] = 2     
            D = dict()              
            
            #test si un coloriage possible quand la case est noire
            noirV = VerifGrilleMO(a.M-1, len(a.tabil[i]), a.tabil[i], a.Gr[i], D) 
            
            a.Gr[i][indice] = 1   
            D1 = dict()
            #test si un coloriage possible quand la case est blanche
            blancV = VerifGrilleMO(a.M-1, len(a.tabil[i]), a.tabil[i], a.Gr[i], D1)
            
            
            if noirV :    #si coloriage possible de la ligne qd la case est noire
                if blancV:  #si coloriage possible de la ligne qd la case est blanche
                    a.Gr[i][indice] = -1  #on ne sait pas la vraie couleur donc c'est indéterminée
                    
                    
                else :       #coloriage impossible quand la case est blanche
                    a.Gr[i][indice] = 2   #la case est noire
                    a.SetLi += [indice]    #ajout de la colonne à la liste des colonnes modifiées
                    
                    
            else :
                if not(blancV):  #si ni noir ni blanc
                    return False  #coloriage impossible

                a.Gr[i][indice] = 1   #sinon la case est blanche
                a.SetLi += [indice]    #ajout de la colonne à la liste des colonnes modifiées
            
    D3 = dict()        
    # on verifie que l'instance qui nous a été donné n'est pas fausse                 
    return VerifGrilleMO(a.M-1, len(a.tabil[i]), a.tabil[i], a.Gr[i], D3)

def colorC(a,j):
    """
    retourne True si la colonne j de la grille a peut être coloriée 
    avec la séquence d'entiers associées à cette colonne, False sinon.
    
    """
    
    colonne=[i[j] for i in a.Gr]  #liste des indices de la colonne j
    
    for indice in range(a.N) :    #parcours des cases de la colonne
            if a.Gr[indice][j] == -1:   #si une case est indéterminée
                a.Gr[indice][j] = 2
                colonne[indice] =2      #mise à jour de la colonne
                D=dict()
                #test si un coloriage possible quand la case est noire
                noirV = VerifGrilleMO(a.N-1, len(a.tabic[j]), a.tabic[j], colonne, D)
                
                a.Gr[indice][j] = 1
                colonne[indice] = 1      #mise à jour de la colonne
                D1= dict()
                #test si un coloriage possible quand la case est blanche
                blancV = VerifGrilleMO(a.N-1, len(a.tabic[j]), a.tabic[j], colonne, D1)
                

                if noirV :       #si coloriage possible de la ligne qd la case est noire
                    if blancV:   #si coloriage possible de la ligne qd la case est blanche
                        a.Gr[indice][j] = -1   #on ne sait pas la vraie couleur donc c'est indéterminée
                        colonne[indice] = -1    #mise à jour de la colonne
                        
                    else :                   #coloriage impossible quand la case est blanche
                        a.Gr[indice][j] = 2   #la case est noire
                        colonne[indice] = 2    
                        a.SetCi += [indice]    #ajout de la colonne à la liste des colonnes modifiées
                        
                        
                else :
                    if not(blancV):
                        return False

                    a.Gr[indice][j] = 1
                    colonne[indice] = 1     #la case est blanche
                    a.SetCi += [indice]    #ajout de la colonne à la liste des colonnes modifiées
                    
                
    D3= dict()
    # on verifie que l'instance qui nous a été donné n'est pas fausse
    return VerifGrilleMO(a.N-1, len(a.tabic[j]), a.tabic[j], colonne, D3)


def coloration2(A):
    """
    affiche la grille A coloriées si possible ainsi que les séquences d'entiers
    des lignes et colonnes correspondantes
    
    """
    a  = deepcopy(A)                   #a grille

    colonneAvoir = [i for i in range(len(a.tabic))]
    ligneAvoir = [i for i in range(len(a.tabil))]
    
    verif = False               #variable pour vérifier si coloration possible d'une ligne
    verif2 = False              #variable pour vérifier si coloration possible d'une colonne
    verif3 = True               #variable pour vérifier si toutes les cases sont coloriées
    verif4 = "ne sait pas"      # cas où toutes mes cases ne sont pas coloriées à la fin de l'algo
    nouv= []
    nouv2 = []
    while ligneAvoir != [] or colonneAvoir != [] : #tant qu'il reste des cas à examiner
        
        
        for i in ligneAvoir :     #parcours des lignes 
            #print(i)
            verif = colorL(a,i)
            
            if not(verif):    #si coloriage impossible retourne False
                return False,a
            
            nouv += [i for i in a.SetLi if i not in nouv] #ajout à nouv des colonne où une case a été coloriée 
            
            colonneAvoir += [i for i in nouv if i not in colonneAvoir] #ajout dans les colonnes à voir
            
            
            a.SetLi = []   #remise à zéro de la liste des colonnes modifiées lors d'un appel à colorL(a,i)
            
            
        ligneAvoir=[]
        nouv = []

        for j in colonneAvoir :   #parcours des colonnes
            
            verif2 = colorC(a,j)
            
            if not(verif2):
                return False,a

            nouv2 += [i for i in a.SetCi if i not in nouv2] #ajout à nouv des lignes où une case a été coloriée  
            
            ligneAvoir += [i for i in nouv2 if i not in ligneAvoir] #ajout aux lignes à voir
            
            
            
            a.SetCi = []   #remise à zéro de la liste des lignes modifiées lors d'un appel à colorC(a,j)
        colonneAvoir = []
        nouv2 = []
        
        
        
    
    
    #verifie si toute la grille est coloriée
    verif3 = a.EstComplete()   # verif3 = True si toutes les cases sont coloriées
    
    if verif3 == True:
       
        
        return verif3,a
    else :
                    # toutes les cases ne sont pas coloriées
        return verif4,a