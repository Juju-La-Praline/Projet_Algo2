

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
    #D = dict()
    
    #print(j)
    
    #print ("j = ",j,"l = ",l)
    #print (D)
    
    
    if l == 0 :                     #cas où il n'y a pas de blocs 
        for ti in ligne[0:j+1] :
            if ti == 2:             #si une case est coloriée en noire, T(j,l) est faux 
                return False
        return True

    elif j < sl[l-1] - 1:         #indice de j est trop petit, T(j,l) est faux
        return False

    elif j == sl[l-1] - 1:       #j est assez grand que s'il reste un seul bloc
        if l == 1:
            for tti in ligne[0:j+1]:
                if tti == 1:          #si une des cases précédentes à j est blanche, T(j,l) est faux
                    return False
           
            return True
            
        else :
            
            return False

    if ligne[j] == -1:               #si la case est indéterminée
        #print("ligne[j-1]==-1")
        
        if ligne[j - sl[l-1]] == 2:     #si cette case est noire 
                #print("ligne[j-sl[l-1]-1] == 2:")
                #print("false")
                #alors la case ligne[j] est blanche sinon il y a une case noire de trop
                if (j - 1 , l) not in D : 
            
                    D[j - 1 , l] = VerifGrilleMO(j - 1, l, sl, ligne, D)
                    
                return D[j - 1 , l] 
                
                #return jsupSLM(j - 1, l, sl, ligne) # cas une case noire de trop par rapport a la taille
        
        
        for i in ligne[j - sl[l-1]+1:j ] : #parcours des j - sl[l-1] cases précédent j  # cas une case blanche dans sl dans la suite 
            #print(i)
            if i == 1 :            #si une des cases est blanche alors ligne[j] est blanche
                #print("pas noire")
                
                if (j - 1 , l) not in D :
                    
                    D[j - 1 , l] = VerifGrilleMO(j - 1, l, sl, ligne, D)
                    
                return D[j - 1 , l]
                
        """if j-sl[l-1] +1 < 0: #cas pas la place de mettre les cases noires
            #print("j-sl[l-1] < 0:")
            #print("false")
            return jsupSLM(j - 1, l, sl, ligne)"""
            
            
        

        """if j-sl[l-1] +1 == 0: #cas pile la place de mettre les cases noires
            #print("j-sl[l-1] == 0:")
            #print("true")
            return True"""
        

        #print("ne sais pas")        
        #return jsupSLM(j - sl[l-1]-1, l-1, sl, ligne) or jsupSLM(j - 1, l, sl, ligne) 
        #3 cas on test pour ligne[j] noire et ligne[j] blanche
        k = j - sl[l-1] - 1
        
        if ( k , l - 1) not in D :# if in D ? faire le or quand meme 
            #print("appel", k, l-1)  #considere que ligne[j] est noire
            D[k , l - 1] = VerifGrilleMO(j - sl[l-1]-1, l-1, sl, ligne, D)# le or ?

            if D[k, l - 1] == True :
                return True
         
        if (j-1, l) not in D:  #considere que ligne[j] est blanche
            D[j - 1 , l] = VerifGrilleMO(j - 1, l, sl, ligne, D)
            
        return D[k , l - 1] or D[j - 1 , l]
            
        
        

    if ligne[j] == 1:      #si la case est blanche

        #○print("ligne[j-1]==1")
        #return jsupSLM(j - 1, l, sl, ligne) # case blanche
        if (j - 1 , l) not in D :  
            D[j - 1 , l] = VerifGrilleMO(j - 1, l, sl, ligne, D)

        return D[j - 1 , l]
        


    if ligne[j] == 2:           #si la case est noire

        #print("ligne[j-1]==2:")
        for i in ligne[j - sl[l-1]+1:j ] : # parcours des j - sl[l-1] cases avant j
            if i == 1:                    #si une des cases est blanche
                #print(i ,"false")
                return False               #le coloriage est impossible
            
        """if j-sl[l-1] +1 < 0: #cas pas la place de mettre les cases noires
            #print("j-sl[l-1] < 0:")
            #print("false")
            return False"""

        """if j-sl[l-1] +1 == 0: #cas pile la place de mettre les cases noires
            #print("j-sl[l-1] == 0:")
            #print("true")
            return True
        else :"""
            
        if ligne[j - sl[l-1]] == 2:  #si cette case est noire
            #print("ligne[j-sl[l-1]-1] == 2:")
                #print("false")
            return False # coloriage impossible car une case noire de trop 
        else :
            k = j - sl[l-1] - 1
            if (k, l - 1) not in D :
                    
                    D[k, l - 1] = VerifGrilleMO(j - sl[l-1] -1, l - 1, sl, ligne, D)
                    
            return D[k, l - 1]
            #return jsupSLM(j - sl[l-1] -1, l - 1, sl, ligne) # cas case noire trouvée 