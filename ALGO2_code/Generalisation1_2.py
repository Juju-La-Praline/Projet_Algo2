

def VerifGrilleMO(j, l, sl, ligne, D):
    #print("\n")
    
    #print("jsupSLMP(j=",j,", l=",l,", sl, ligne)")
    """
    pour j un indice, une sous sequence sl de taille l, une ligne 
    la fonction retourne True si une coloration de la ligne est possible, False sinon.
    D est le dictionnaire des valeurs T(j,l), par exemple D[j,l] = True ou False.
    Une case à valeur 1 est blanche, 2 est noire et -1 est indéterminée.
    """
    
    #dictionnaire des valeurs [j,l] : False ou True 
    
    
    
    if l == 0 :                     #cas où il n'y a pas de blocs 

        for ti in ligne[0 : j + 1] :
            if ti == 2 :             #si une case est coloriée en noire, T(j,l) est faux 
                return False
        return True

    elif j < sl[l - 1] - 1 :         #indice de j est trop petit, T(j,l) est faux
        return False

    elif j == sl[l - 1] - 1 :       #j est assez grand que s'il reste un seul bloc
        if l == 1 :

            for tti in ligne[0 : j + 1] :
                
                if tti == 1 :        #si une des cases précédentes à j est blanche, T(j,l) est faux
                    return False
           
            return True
            
        else :
            return False


    if ligne[j] == -1 :               #si la case est indéterminée
        
        if ligne[j - sl[l - 1]] == 2 :     #si cette case est noire 
                
                #alors la case ligne[j] est blanche sinon il y a une case noire de trop
                if (j - 1, l) not in D : 
            
                    D[j - 1, l] = VerifGrilleMO(j - 1, l, sl, ligne, D)
                    
                return D[j - 1, l] 
                
                 # cas une case noire de trop par rapport a la taille
        
        
        for i in ligne[j - sl[l - 1] + 1:j] : #parcours des j - sl[l-1] cases précédent j  # cas une case blanche dans sl dans la suite 
            
            if i == 1 :            #si une des cases est blanche alors ligne[j] est blanche
                
                
                if (j - 1, l) not in D :
                    
                    D[j - 1, l] = VerifGrilleMO(j - 1, l, sl, ligne, D)
                    
                return D[j - 1, l]
                
        
        k = j - sl[l - 1] - 1
        
        if (k, l - 1) not in D : 
             
            D[k, l - 1] = VerifGrilleMO(j - sl[l - 1] - 1, l - 1, sl, ligne, D)

            if D[k, l - 1] == True :
                return True
         
        if (j - 1, l) not in D:  #considere que ligne[j] est blanche
            D[j - 1, l] = VerifGrilleMO(j - 1, l, sl, ligne, D)
            
        return D[k, l - 1] or D[j - 1, l]
            
        
        

    if ligne[j] == 1 :      #si la case est blanche

       
        if (j - 1, l) not in D :  
            D[j - 1, l] = VerifGrilleMO(j - 1, l, sl, ligne, D)

        return D[j - 1, l]
        


    if ligne[j] == 2 :           #si la case est noire

       
        for i in ligne[j - sl[l - 1] + 1 : j ] : # parcours des j - sl[l-1] cases avant j
            if i == 1 :                    #si une des cases est blanche
                
                return False               #le coloriage est impossible
            
        
            
        if ligne[j - sl[l - 1]] == 2 :  #si cette case est noire
            
            return False # coloriage impossible car une case noire de trop 
        else :
            k = j - sl[l - 1] - 1
            if (k, l - 1) not in D :
                    
                    D[k, l - 1] = VerifGrilleMO(j - sl[l - 1] - 1, l - 1, sl, ligne, D)
                    
            return D[k, l - 1]
           