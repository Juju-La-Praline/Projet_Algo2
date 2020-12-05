


def VerifGrille(j, l, sl):
    """
    pour j un indice, une sous sequence sl de taille l,
    la fonction retourne True si T(j,l) est vrai, Faux sinon.
    """
    if l == 0 :       #il n'y a pas de bloc
        return True
                     #il y a au moins 1 bloc
    elif j < sl[l - 1] - 1 :   #j est trop petit
        return False
    
    elif j == sl[l - 1] - 1 : #il y a assez de place pour un bloc seuleument

        if l == 1 :       

            return True
        else :
            return False
    else :                   #appel récursif case j noire ou blanche
        return VerifGrille(j - sl[l - 1] - 1, l - 1, sl ) or VerifGrille(j - 1, l, sl) 