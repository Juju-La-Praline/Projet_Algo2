from tkinter import *
from GrilleC import *

def affichage_fenetre(grille):
    """ affiche une grille dans une fenêtre graphique
    """

    
    largeur = (grille.nMl + grille.M) * 10
    hauteur = (grille.nMc + grille.N) * 10
    taille_case = 10
    fenetre = Tk()
    nMc = grille.nMc
    nMl = grille.nMl
    can = Canvas(fenetre, width=largeur, height=hauteur,bg="white")
    for j in range (grille.N + 1):
        x1j = 0
        y1j = nMc * taille_case + taille_case * (j+1)

        x2j = nMl * taille_case + taille_case * (grille.M+1) 
        y2j = nMc * taille_case + taille_case * (j+1)
        can.create_line(x1j, y1j, x2j, y2j, fill="black")#creation des lignes horizontals
    
    for i in range(grille.M + 1):
        x1i = nMl * taille_case + taille_case * (i+1)
        y1i = 0

        x2i = nMl * taille_case + taille_case * (i+1)
        y2i = taille_case * (grille.N+1) + nMc * taille_case 
        can.create_line(x1i, y1i, x2i, y2i, fill="black")#creation des lignes verticals
    
    for n in range (grille.N):
        for m in range (grille.M):
            t = grille.Gr[n][m]
            if t == -1 : # inconnu
                x1k = nMl * taille_case + taille_case * (m+1)
                y1k = nMc * taille_case + taille_case * (n+1)

                x2k = nMl * taille_case + taille_case * (m+1) + taille_case
                y2k = nMc * taille_case + taille_case * (n+1) + taille_case
                can.create_rectangle(x1k, y1k, x2k, y2k, fill="pink")
                
            if t == 1 : # blanc
                x1l = nMl * taille_case + taille_case * (m+1)
                y1l = nMc * taille_case + taille_case * (n+1)

                x2l = nMl * taille_case + taille_case * (m+1) + taille_case
                y2l = nMc * taille_case + taille_case * (n+1) + taille_case
                can.create_rectangle(x1l, y1l, x2l, y2l, fill="white")
            if t == 2 : #noir
                x1m = nMl * taille_case + taille_case * (m+1)
                y1m = nMc * taille_case + taille_case * (n+1)

                x2m = nMl * taille_case + taille_case * (m+1) + taille_case
                y2m = nMc * taille_case + taille_case * (n+1) + taille_case
                can.create_rectangle(x1m, y1m, x2m, y2m, fill="black")

    for o in range(len(grille.tabil)) :
        blocl=grille.tabil[o]
        strl=' '.join(str(elem) for elem in blocl)

        x1q = nMl * taille_case/2
        y1q = taille_case * (o+1) + nMc * taille_case + taille_case/2

        can.create_text(x1q, y1q, text=strl)
        
   
    
    for p in range(len(grille.tabic)) :
        blocC=grille.tabic[p]
        strC=''.join(str(elem) for elem in blocC)

        x1r = taille_case * (p+1) + nMl * taille_case + taille_case/2
        y1r = nMc * taille_case/2

        can.create_text(x1r, y1r, text= strC, width=1 )

    can.pack(fill=BOTH, expand=1)
    
    fenetre.mainloop()

    #for i in range()

