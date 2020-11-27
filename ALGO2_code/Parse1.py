from GrilleC import *

a='0.txt'

def creer_grille2(z):# crée la grille a partir d'un fichier 
    """ 
    crée une grille à partir des valeurs du fichier z
    
    """
    tabic = []       # liste des sl des colonnes
    tabil = []       # liste des sl des lignes
    N = 0
    M = 0
    tail_max_L = 0
    tail_max_C = 0
    
    hashtag = False
    fichier = open(z, 'r')
    i=0
    for ligne in fichier:

        i=i+1
        if ligne[0]== '#':        #si la ligne commence par un #
            hashtag = True
            N=i-1                 #nombre de lignes 
            i=0
        
        elif hashtag:                          #cas des colonnes
            ligne_split=ligne.split()
            Vtemp = [int(i) for i in ligne_split]  #sequence d'entier d'une colonne
            
            if Vtemp != []:
                tail_max_C=max(len(Vtemp),tail_max_C)
            tabic+= [Vtemp]                   #ajout à la liste des sl des colonnes
            
        else:                                      # cas des lignes
            ligne_split2 = ligne.split()
            Vtemp2=[int(i) for i in ligne_split2]  #sequence d'entier d'une ligne

            if Vtemp2 != []: 
                tail_max_L=max(len(Vtemp2),tail_max_L)
            tabil+= [Vtemp2]                #ajout à la liste des sl des lignes
            
    M=i                                     #nombre de colonnes      
    fichier.close()
    g = Grille(N, M, tabil, tabic, tail_max_L+1, tail_max_C+3)

    return g

