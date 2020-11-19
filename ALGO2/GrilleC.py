class Grille: 
    
    def __init__(self, nbl, nbc, tabil, tabic, nMl, nMc):#tabil,tabic tableau de liste
        self.N = nbl # nombre ligne
        self.M = nbc # nombre colone
        self.Gr = list()
        self.tabic = tabic # liste des sl des colones
        self.tabil = tabil # liste des sl des lignes
        self.nMl = nMl # taille max du nombre de sl dans les lignes
        self.nMc = nMc # taille max du nombre de sl dans les colones
        self.SetCi=[]
        self.SetLi=[]
        for i in range(self.N) :

            ligne = list()

            for j in range(self.M) :

                ligne.append(-1)
                
            self.Gr.append(ligne)

            

    '''def affiche_grille(self):
        for t in range(self.M):
            
            print(tabic1[t], end = '')
        for i in range(self.N) :
            print('\n')
            print(end='|')
            
            for j in range(self.M) :
                print(self.Gr[i][j],end= '|')
            print(tabil1[i], end = '')    

tabil1 = [[3],[],[1,1,1],[3]]
tabic1 = [[1,1],[1],[1,2],[1],[2]]
 

g.affiche_grille()'''