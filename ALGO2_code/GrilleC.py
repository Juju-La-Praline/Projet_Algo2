class Grille: 
    
    def __init__(self, nbl, nbc, tabil, tabic, nMl, nMc):#tabil,tabic tableau de liste
        """
        crée un objet grille 
        
        """
        
        self.N = nbl            # nombre ligne
        self.M = nbc            # nombre colone
        self.Gr = list()        # 
        self.tabic = tabic      # liste des sl des colonnes
        self.tabil = tabil      # liste des sl des lignes
        self.nMl = nMl          # taille max du nombre de sl dans les lignes
        self.nMc = nMc          # taille max du nombre de sl dans les colonnes
        self.SetCi=[]           # la liste des lignes modifiées lors d'un appel à colorC(a,j)
        self.SetLi=[]           # liste des colonnes modifiées lors d'un appel à colorL(a,i)
        self.Kn = 0            
        self.Kp = 0
        for i in range(self.N) :# initialisation de la grille à -1

            ligne = list()

            for j in range(self.M) :

                ligne.append(-1)
                
            self.Gr.append(ligne)
            
            
            
    def EstComplete(self):
        """ 
        retourne True si toutes les cases de la grille ont été coloriées,
        Faux sinon 
        """
        
        for i in range(self.N) :

            for j in range(self.M) :
                
                if self.Gr[i][j] == -1:
                     
                                  
                    self.Kn = i*self.M + j 
                    
                    return False
                    
        print("true")
        return True
                
            
            

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
