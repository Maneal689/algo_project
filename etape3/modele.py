from random import *

class Case:
    '''Defini une case'''

    def __init__(self,couleur):
        '''Initialise la case'''
        self.__couleur=couleur

    def couleur(self):
        '''Retourne la couleur de la case  /  return : int'''
        return self.__couleur

    def change_couleur(self,couleur):
        '''Change la couleur de la case  /  Case(modif)'''
        self.__couleur = couleur
        self.__compo = -1

    def supprime(self):
        '''Supprime la case (passe la couleur a -1)  /  Case(modif)'''
        self.__couleur = -1
        self.__compo = 0

    def est_vide(self):
        '''Retourne True si la case est vide(self.__couleur=-1)  /  return : boolean'''
        return self.__couleur == -1

class ModeleSame:
    '''Defini le plateau de jeu'''

    def __init__(self,nbl=10,nbc=15,nbcouleur=3):
        '''Initialise le plateau de jeu'''
        self.__nbligne=nbl
        self.__nbcolonne=nbc
        self.__nbcouleur=nbcouleur
        self.__score=0
    #Creation de la matrice du plateau de jeu
        self.__mat=[]
        for i in range(self.__nbligne):
            self.__mat.append([])
            for j in range(self.__nbcolonne):
                self.__mat[i].append(Case(randint(0,self.__nbcouleur-1)))

    def nblig(self):
        '''Retourne le nombre de ligne du plateau  /  return : int'''
        return self.__nbligne

    def nbcol(self):
        '''Retourne le nombre de colonne du plateau  /  return : int'''
        return self.__nbcolonne

    def nbcouleur(self):
        '''Retourne le nombre de couleurs du plateau  /  return : int'''
        return self.__nbcouleur

    def score(self):
        '''Retourne le score du joueur  /  return : int'''
        return self.__score

    def coords_valides(self,i,j):
        '''Retourne True si les coordonnées données sont valides  /  return : boolean'''
        return -1<i<self.__nbligne and -1<j<self.__nbcolonne

    def couleur(self,i,j):
        '''Retourne la couleur de la case a la ligne i et colonne j  /  return : int'''
        return self.__mat[i][j].couleur()

    def supprime_bille(self,i,j):
        '''Supprime une bille en mettant la valeur de sa couleur a -1  /  ModeleSame(modif)'''
        if (self.__mat[i][j].couleur() != -1):
            l_asuppr = []
            l_asuppr.append((i, j))
            self.ajoute_meme_couleur(l_asuppr, i, j, self.__mat[i][j].couleur())
            if (len(l_asuppr) >= 2):
                self.__score += (len(l_asuppr) - 2) ** 2
                for elm in l_asuppr:
                    self.__mat[elm[0]][elm[1]].supprime()
                self.supprime_colonne_vide()
                self.tombe_bille()
                return (True)
        return (False)

    def nouvelle_partie(self):
        for i in range (self.__nbligne):
            for j in range(self.__nbcolonne):
                self.__mat[i][j].change_couleur(randint(0,self.__nbcouleur-1))
        self.__score = 0

    def coords_autour(self, i, j):
        res = []
        if (self.coords_valides(i - 1, j)):
            res.append((i - 1, j))
        if (self.coords_valides(i + 1, j)):
            res.append((i + 1, j))
        if (self.coords_valides(i, j - 1)):
            res.append((i, j - 1))
        if (self.coords_valides(i, j + 1)):
            res.append((i, j + 1))
        return (res)

    def ajoute_meme_couleur(self, lsuppr, i, j, couleur):
        """
        Fonction qui ajoute a lsuppr (list((int, int))) les coordonnées des billes de même couleur que couleur
        ModeleSame, list(int, int), int, int, int -> None
        """
        coord_at = self.coords_autour(i, j)
        for coord in coord_at:
            if (self.__mat[coord[0]][coord[1]].couleur() == couleur and coord not in lsuppr):
                lsuppr.append((coord[0], coord[1]))
                self.ajoute_meme_couleur(lsuppr, coord[0], coord[1], couleur)

    def colonne_vide(self, col):
        """

        """
        i = 0
        while (i < self.nblig()):
            if (not self.__mat[i][col].est_vide()):
                return (False)
            i += 1
        return (True)

    def tombe_bille(self):
        """
        Met a jour les Cases en fonction des vides présents (fait tomber les billes)
        ModeleSame -> None
        """
        i = 0
        while (i < self.__nbligne):
            j = 0
            while (j < self.__nbcolonne):
                if (self.couleur(i, j) == -1):
                    k = i
                    while (k >= 1):
                        self.__mat[k][j].change_couleur(self.__mat[k - 1][j].couleur())
                        k -= 1
                    self.__mat[0][j].supprime()
                j += 1
            i += 1

    def supprime_colonne_vide(self):
        """
        
        """
        cpt = 0
        while (cpt < self.nbcol()):
            col = 0
            while (col < self.nbcol()):
                if (self.colonne_vide(col) and col != self.nbcol() - 1):
                    i = 0
                    while (i < self.nblig()):
                        self.__mat[i][col].change_couleur(self.__mat[i][col + 1].couleur())
                        self.__mat[i][col + 1].supprime()
                        i += 1
                col += 1
            cpt += 1
