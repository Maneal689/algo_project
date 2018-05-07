from random import *

class Case:
    '''Defini une case'''

    def __init__(self,couleur):
        '''Initialise la case'''
        self.__couleur=couleur
        self.__compo=-1

    def couleur(self):
        '''Retourne la couleur de la case  /  return : int'''
        return self.__couleur

    def change_couleur(self,couleur):
        '''Change la couleur de la case  /  Case(modif)'''
        self.__couleur=couleur
        self.__compo=-1

    def supprime(self):
        '''Supprime la case (passe la couleur a -1)  /  Case(modif)'''
        self.__couleur=-1
        self.__compo=0

    def est_vide(self):
        '''Retourne True si la case est vide(self.__couleur=-1)  /  return : boolean'''
        return self.__couleur == -1
    
    def composante(self):
        '''Donne le numéro de composante de la case  /  return : int'''
        return self.__compo
    
    def pose_composante(self,nb):
        '''Change le numéro de composante de la case  /  Case(modif)'''
        self.__compo=nb

    def supprime_composante(self):
        '''Supprime la composante (la reinit a -1)  /  Case(modif)'''
        self.__compo=-1

    def parcourue(self):
        '''Regarde si la case a déja eu un numéro de composante attribué  /  return : boolean'''
        return self.__compo!=-1

class ModeleSame:
    '''Defini le plateau de jeu'''

    def __init__(self,nbl=10,nbc=15,nbcouleur=3):
        '''Initialise le plateau de jeu'''
        self.__nbligne=nbl
        self.__nbcolonne=nbc
        self.__nbcouleur=nbcouleur
        self.__score=0
        self.__nb_elts_compo=[]
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
        if self.__mat[i][j].couleur()!=-1: 
            self.supprime_composante(self.__mat[i][j].composante())
            self.supprime_colonne_vide()

    def nouvelle_partie(self):
        self.__score = 0
        for i in range (self.__nbligne):
            for j in range(self.__nbcolonne):
                self.__mat[i][j].change_couleur(randint(0,self.__nbcouleur-1))

    def composante(self,i,j):
        '''Renvoie le numéro de composante de la case en (i,j)  /  return : int'''
        return self.__mat[i][j].composante()
    
    def calcule_composantes(self):
        '''Lance le calcul des composantes sur toutes les cases de la matrice'''
        self.__nb_elts_compo=[0]
        num_compo=1
        for i in range (self.nblig()):
            for j in range(self.nbcol()):
                if self.__mat[i][j].composante()==-1:
                    couleur=self.__mat[i][j].couleur()
                    a=self.calcule_composante_numero(i,j,num_compo,couleur)
                    self.__nb_elts_compo.append(a)
                    num_compo+=1
    
    def calcule_composante_numero(self,i,j,num_compo,couleur):
        '''Attribut un numero de composante et compte la taille du groupe  /  return : int'''
        if not self.coords_valides(i,j):
            return 0
        if self.__mat[i][j].parcourue() or self.__mat[i][j].couleur()!=couleur:
            return 0
        else:
            self.__mat[i][j].pose_composante(num_compo)
            return 1 + self.calcule_composante_numero(i,j+1,num_compo,couleur) + self.calcule_composante_numero(i,j-1,num_compo,couleur) + self.calcule_composante_numero(i+1,j,num_compo,couleur) + self.calcule_composante_numero(i-1,j,num_compo,couleur)
        

    def reset_composante(self):
        '''Reset les composantes du plateau'''
        for i in range(self.nblig()):
            for j in range(self.nbcol()):
                self.__mat[i][j].pose_composante(-1)

    def supprime_composante(self,num_compo):
        '''Supprime une composante'''
        if (self.__nb_elts_compo[num_compo]>=2):
            self.__score+=(self.__nb_elts_compo[num_compo]-2) ** 2
            i=0
            while i<self.nblig():
                j=0
                while j<self.nbcol():
                    if (self.__mat[i][j].composante() == num_compo):
                        self.supprime_composante_colonne(j,num_compo)
                    j+=1
                i+=1


    def case_vide(self,i,j):
        '''Retourne True si la case est vide  /  return : boolean'''
        return self.__mat[i][j].couleur() == -1

    def supprime_composante_colonne(self,j,num_compo):
        for i in range(self.nblig()):
            if self.__mat[i][j].composante() == num_compo:
                self.__mat[i][j].supprime()
                tmp=self.descend_vert(j)
                while tmp == True:
                    tmp=self.descend_vert(j)

    def descend_vert(self,j):
        """
        Fait tomber les billes de la colonner j à la verticale
        ModeleSame, int -> boolean
        """
        tmp=False
        for i in range(self.nblig()):
            if not self.case_vide(i,j):
                if 0<=(i+1)<self.nblig() and self.case_vide(i+1,j):
                    self.__mat[i][j], self.__mat[i+1][j] = self.__mat[i+1][j], self.__mat[i][j]
                    tmp=True
        return tmp

    def colonne_vide(self, col):
        """
        Vérifie si la colonne col, est vide ou non
        ModeleSame, int -> boolean
        """
        i = 0
        while (i < self.nblig()):
            if (not self.__mat[i][col].est_vide()):
                return (False)
            i += 1
        return (True)

    def supprime_colonne_vide(self):
        """
        Supprime les colonnes vides et décale les billes vers la gauche 
        ModeleSame -> None
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
    
    def nb_elmts_compo(self,x):
        '''Donne le nbre d elements dans la compo x'''
            return self.__nb_elts_compo[x]




