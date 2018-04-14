from tkinter import *
from modele import *

class VueSame:
    '''Defini la vue du jeu'''

    def __init__(self,same):
        '''Initialise la vue du same'''
        self.__same=same
        self.__fen=Tk()
        self.__fen.title("SAMEEEEEEEEEEEEE")
    #Liste images
        self.__images=[]
        for i in range(self.__same.nbcouleur()):
            self.__images.append(PhotoImage(file="img/medium_sphere"+str(i+1)+".gif"))
        self.__images.append(PhotoImage(file="img/medium_spherevide.gif"))
    #------------

    #Liste boutons
        self.__listebutton=[]
        for i in range(self.__same.nblig()):
            self.__listebutton.append([])
            for j in range(self.__same.nbcol()):
                self.__listebutton[i].append(Button(self.__fen,image=self.__images[self.__same.couleur(i,j)],command=self.creer_controleur_btn(i,j)))
                self.__listebutton[i][j].grid(row=i,column=j)
    #--------------

    #Bouton nouvelle partie et quitter
        nouvellepartie=Button(self.__fen,text="Nouvelle partie",command=self.newgame)
        nouvellepartie.grid(row=int(self.__same.nblig()/2),column=self.__same.nbcol())
        quitter=Button(self.__fen,text="Quitter",command=self.__fen.destroy)
        quitter.grid(row=int(self.__same.nblig()/2)+1,column=self.__same.nbcol())
    #----------------------
        mainloop()
    
    def update(self):
        '''Met a jour les images des boutons selon la valeur dans self.__same'''
        for i in range(self.__same.nblig()):
            for j in range(self.__same.nbcol()):
                self.__listebutton[i][j].config(image=self.__images[self.__same.couleur(i,j)])

    def newgame(self):
        '''Démarre une nouvelle partie'''
        self.__same.nouvelle_partie()
        self.update()
    
    def creer_controleur_btn(self,i,j):
        '''retourne une fonction  /  return:function'''
        def controleur_btn():
            '''supprime la bille quand le joueur clique dessus  /  VueSame(modif)'''
            self.__same.supprime_bille(i,j)
            self.update()
        return controleur_btn

if __name__ == "__main__":
# création du modèle
    same = ModeleSame()
# création de la vue qui créé les contrôleurs
# et lance la boucle d’écoute des évts
    vue = VueSame(same)
