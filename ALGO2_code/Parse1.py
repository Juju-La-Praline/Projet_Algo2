from GrilleC import *

a='0.txt'

def creer_grille2(z):# crée la grille a partir d'un fichier 
    
    tabic = []
    tabil = []
    N = 0
    M = 0
    tail_max_L = 0
    tail_max_C = 0
    
    hashtag = False
    fichier = open(z, 'r')
    i=0
    for ligne in fichier:

        i=i+1
        if ligne[0]== '#':
            hashtag = True
            N=i-1
            i=0
        
        elif hashtag:
            ligne_split=ligne.split()
            Vtemp = [int(i) for i in ligne_split]
            
            if Vtemp != []:
                tail_max_C=max(len(Vtemp),tail_max_C)
            tabic+= [Vtemp]
            
        else:
            ligne_split2 = ligne.split()
            Vtemp2=[int(i) for i in ligne_split2]

            if Vtemp2 != []:
                tail_max_L=max(len(Vtemp2),tail_max_L)
            tabil+= [Vtemp2]
            
    M=i       
    fichier.close()
    g = Grille(N, M, tabil, tabic, tail_max_L+1, tail_max_C+3)

    return g

