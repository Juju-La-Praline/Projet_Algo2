from Projet import *
from Parse import *
from Graphic import *

#rendre en dynamique (retenir les res des difference valeur de j et l)
def jsupSLMP(j, l, sl, ligne):# l taille de la sous sequence  , S la sous sequence
    print("\n")
    
    print("jsupSLMP(j=",j,", l=",l,", sl, ligne)")
    if l == 0 :
        for ti in ligne[0:j+1] :
            if ti == 2:
                print("false")
                return False
        print("true")
        return True
    elif j < sl[l-1] - 1:
        print("false")
        return False
    elif j == sl[l-1] - 1:
        if l == 1 and ligne[j]!= 1:
            print("true")
            return True
        else :
            print("false")
            return False
    

    if ligne[j] == -1:
        print("ligne[j-1]==-1")
        for i in ligne[j - sl[l-1]+1:j ] : # cas une case blanche dans sl dans la suite 
            #print(i)
            if i == 1 :
                print("pas noire")
                return jsupSLMP(j - 1, l, sl, ligne)
        if j-sl[l-1] +1 < 0: #cas pas la place de mettre les cases noires
            print("j-sl[l-1] < 0:")
            print("false")
            return jsupSLMP(j - 1, l, sl, ligne)
            
        if ligne[j - sl[l-1]] == 2:
            print("pas noire")
            return jsupSLMP(j - 1, l, sl, ligne)
            
        if j-sl[l-1]+1<0:
            print("false")
            return jsupSLMP(j - 1, l, sl, ligne)

        
        if j-sl[l-1] +1 == 0: #cas pile la place de mettre les cases noires
            print("j-sl[l-1] == 0:")
            print("true")
            return True
        

        print("ne sais pas")        
        return jsupSLMP(j - sl[l-1]-1, l-1, sl, ligne) or jsupSLMP(j - 1, l, sl, ligne)   


    if ligne[j] == 1:#blanc
        
        print("ligne[j-1]==1")
        return jsupSLMP(j - 1, l, sl, ligne) # case blanche


    if ligne[j] == 2:#noire

        print("ligne[j-1]==2:")
        for i in ligne[j - sl[l-1]+1:j ] : # cas une case blanche dans sl dans la suite 
            if i == 1:
                print("false")
                return False
            
        if j-sl[l-1] +1 < 0: #cas pas la place de mettre les cases noires
            print("j-sl[l-1] < 0:")
            print("false")
            return False

        if j-sl[l-1] +1 == 0: #cas pile la place de mettre les cases noires
            print("j-sl[l-1] == 0:")
            print("true")
            return True
        else :
            
            if ligne[j - sl[l-1]] == 2: 
                print("ligne[j-sl[l-1]-1] == 2:")
                print("false")
                return False # cas une case noire de trop par rapport a la taille 
            else :

                return jsupSLMP(j - sl[l-1] -1, l - 1, sl, ligne) # cas case noire trouvée 

"""for i in range (5):
    print (i)


l=[1,2,5]
print(l)
del l[0]
print(l)

ligneAvoir = set(i for i in range(10))
print (ligneAvoir)

for i in ligneAvoir :
    print (i)

a=list()
for i in range(10) :

            ligne = list()

            for j in range(5) :

                ligne.append(-1)
                
            a.append(ligne)

print(a)
print(a[1])
colone= []


j=3
for i in a:
    colone= colone + [i[j]]
print(colone)

col=[i[j] for i in a ]
print(col)"""
j = 4
l = 1
sl = [3]
ligne = [2, -1, -1,-1,-1]
print(1)
print(True==jsupSLMP(j, l, sl, ligne) )

j1 = 4
l1 = 3
sl1 = [1,1,1]
ligne1 = [-1, -1, 1,1,2]
print(2)
print(False==jsupSLMP(j1, l1, sl1, ligne1))

j2 = 4
l2 = 3
sl2 = [1,1,1]
ligne2 = [1, -1, -1,-1,-1]
print(3)
print(False==jsupSLMP(j2, l2, sl2, ligne2))

j3 = 4
l3 = 1
sl3 = [3]
ligne3 = [-1, -1, -1,2,-1]
print(4)
print(True==jsupSLMP(j3, l3, sl3, ligne3))