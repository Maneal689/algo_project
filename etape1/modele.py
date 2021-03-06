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

    def supprime(self):
        '''Supprime la case (passe la couleur a -1)  /  Case(modif)'''
        self.__couleur = -1

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
        self.__mat[i][j].supprime()

    def nouvelle_partie(self):
        for i in range (self.__nbligne):
            for j in range(self.__nbcolonne):
                self.__mat[i][j].change_couleur(randint(0,self.__nbcouleur-1))
