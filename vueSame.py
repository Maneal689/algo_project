import tkinter
import random
from modeleSame import ModeleSame

class VueSame:
    def __init__(self, modele):
        """
        Initialise une instance de la classe VueSame
        VueSame, ModeleSame -> VueSame
        """
        self.__same = modele
        self.__fen = tkinter.Tk()
        self.__imgs = self.init_imgs()
        self.__btn_list = []
        i = 0
        while (i < self.__same.nblig()):
            j = 0
            while (j < self.__same.nbcol()):
                self.__btn_list.append(tkinter.Button(self.__fen, command=self.creer_ctrl_suppr_bille(i, j)))
                j += 1
            i += 1
        self.update_view()

        btn_recommencer = tkinter.Button(self.__fen, text="Recommencer", command=self.reinit)
        btn_recommencer.grid(row=self.__same.nblig() // 2, column=self.__same.nbcol())
        self.__fen.mainloop()

    def update_view(self):
        """
        
        """
        i = 0
        while (i < self.__same.nblig()):
            j = 0
            while (j < self.__same.nbcol()):
                self.__btn_list[i * self.__same.nbcol() + j]["image"] = self.__imgs[self.__same.couleur(i, j)]
                self.__btn_list[i * self.__same.nbcol() + j].grid(row=i, column=j)
                j += 1
            i += 1

    def creer_ctrl_suppr_bille(self, i ,j):
        def ctrl_suppr_bille():
            self.__same.supprime_bille(i, j)
            self.update_view()
        return (ctrl_suppr_bille)

    def init_imgs(self):
        """
        Initialise la liste des couleurs
        VueSame -> list(tkinter.PhotoImage)
        """
        res = []
        i = 0
        while (i < self.__same.nbcouleurs()):
            current_file = "img/petit_sphere" + str(i + 1) + ".gif"
            res.append(tkinter.PhotoImage(file=current_file))
            i += 1
        res.append(tkinter.PhotoImage(file="img/petit_spherevide.gif"))
        return (res)

    def reinit(self):
        self.__same.nouvelle_partie()
        self.update_view()

if (__name__ == "__main__"):
    same = ModeleSame()
    jeu = VueSame(same)
