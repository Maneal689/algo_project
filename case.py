class Case:
    def __init__(self, couleur = -1):
        """
        Initialise une instance de la classe Case
        """
        self.__couleur = couleur

    def couleur(self):
        """
        Renvoie la couleur de la case
        Case -> int
        """
        return (self.__couleur)

    def change_couleur(self, n_couleur):
        """
        Change la couleur actuelle de la case
        Case, int -> None
        """
        if (n_couleur >= -1 and n_couleur <= 8):
            self.__couleur = n_couleur

    def supprime(self):
        """
        Vide la case
        Case -> None
        """
        self.__couleur = -1

    def est_vide(self):
        """
        Indique si la case est vide ou non
        Case -> Boolean
        """
        return (self.__couleur == -1)
