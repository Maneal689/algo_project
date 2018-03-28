from random import randint
import case

class ModeleSame:
    def __init__(self, nb_ligne = 15, nb_col = 20, nb_couleur = 4):
        """
        Initialise une instance de la classe ModeleSame
        Arguments:
            self : ModeleSame
            nb_ligne = 15 : int
            nb_col = 20 : int
            nb_couleur = 4 : int
        Retour:
            ModeleSame
        """
        self.__nblig = nb_ligne
        self.__nbcol = nb_col
        self.__nbcouleurs = nb_couleur
        self.__score = 0
        self.__mat = []
        i = 0
        while (i < self.__nblig):
            self.__mat.append([])
            j = 0
            while (j < self.__nbcol):
                self.__mat[i].append(case.Case(randint(0, self.__nbcouleurs - 1)))
                j += 1
            i += 1

    def score(self):
        """
        Retourne le score du joueur
        ModeleSame -> int
        """
        return (self.__score)

    def nblig(self):
        """
        Retourne le nombre de lignes du jeu
        ModeleSame -> int
        """
        return (self.__nblig)

    def nbcol(self):
        """
        Retourne le nombre de colonnes du jeu
        ModeleSame -> int
        """
        return (self.__nbcol)

    def nbcouleurs(self):
        """
        Retourne le nombre de couleurs du jeu
        ModeleSame -> int
        """
        return (self.__nbcouleurs)

    def coords_valides(self, i, j):
        """
        Indique s'il s'agit de coordonnées valides
        ModeleSame, int, int -> Boolean
        """
        return (i < self.__nblig and j < self.__nbcol and i >= 0 and j >= 0)

    def couleur(self, i, j):
        """
        Indique la couleur de case aux coordonnées données
        ModeleSame, int, int -> int
        """
        if (self.coords_valides(i, j)):
            return (self.__mat[i][j].couleur())
        return (-1)

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

    def supprime_bille(self, i, j):
        """
        Vide la case aux coordonnées données
        ModeleSame, int, int -> None
        """
        if (self.coords_valides(i, j)):
            asuppr = []
            asuppr.append((i, j))
            couleur = self.__mat[i][j].couleur()
            self.ajoute_meme_couleur(asuppr, i, j, couleur)
            for coord in asuppr:
                self.__mat[coord[0]][coord[1]].supprime()
        self.update()

    def update(self):
        """
        Met a jour les Cases en fonction des vides présents (fait tomber les billes)
        ModeleSame -> None
        """
        i = 0
        while (i < self.__nblig):
            j = 0
            while (j < self.__nbcol):
                if (self.couleur(i, j) == -1):
                    k = i
                    while (k >= 1):
                        self.__mat[k][j].change_couleur(self.__mat[k - 1][j].couleur())
                        k -= 1
                    self.__mat[0][j].supprime()
                j += 1
            i += 1

    def nouvelle_partie(self):
        """
        Réinitialise le jeu
        ModeleSame -> None
        """
        i = 0
        while (i < self.__nblig):
            j = 0
            while (j < self.__nbcol):
                self.__mat[i][j].change_couleur(randint(0, self.__nbcouleurs -1))
                j += 1
            i += 1
