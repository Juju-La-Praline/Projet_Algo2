from GrilleC import *

a='0.txt'

def creer_grille(z):# crée la grille a partir d'un fichier 
    
    tabic = []
    tabil = []
    N = 0
    M = 0
    cptLi = 0
    cptCo = 0
    tail_max_L = 0
    tail_max_C = 0
    t_m_i = 0
    t_m_i2 = 0
    hashtag = False
    fichier = open(z, 'r')

    for ligne in fichier:

        cptLi = cptLi + 1
        cptCo = cptCo + 1
        slP=[]

        if t_m_i > t_m_i2 :
            t_m_i2 = t_m_i

        t_m_i = 0

        for carac in ligne:
            
            if carac == '#':
                hashtag = True
                N = cptLi - 1
                tail_max_L = t_m_i2
                t_m_i2 = 0
                cptCo = cptCo - cptLi

            elif carac == ' ':
                None

            elif carac == '\n':
                None

            else:
                slP.append(int(carac))
                t_m_i = t_m_i + 1


        if hashtag :
            tabic = tabic + [slP]

        else:
            tabil = tabil + [slP]

    M = cptCo
    tail_max_C = t_m_i2       
    fichier.close()
    
    del tabic[0]
    '''print(tail_max_L)
    print(tail_max_C)
    print(tabil)
    print(tabic)
    print(N, M)'''
    g = Grille(N, M, tabil, tabic, tail_max_L, tail_max_C)
    
    return g

    

