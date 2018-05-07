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
        self.__images_n=[]
        for i in range(self.__same.nbcouleur()):
            self.__images.append(PhotoImage(file="img/medium_sphere"+str(i+1)+".gif"))
            self.__images_n.append(PhotoImage(file="img/medium_sphere"+str(i+1)+"black.gif"))
        self.__images.append(PhotoImage(file="img/medium_spherevide.gif"))
        self.__images_n.append(PhotoImage(file="img/medium_spherevide.gif"))
    #------------

    #Liste boutons
        self.__listebutton=[]
        for i in range(self.__same.nblig()):
            self.__listebutton.append([])
            for j in range(self.__same.nbcol()):
                self.__listebutton[i].append(Button(self.__fen,image=self.__images[self.__same.couleur(i,j)],command=self.creer_controleur_btn(i,j)))
                self.__listebutton[i][j].grid(row=i,column=j)
                self.__listebutton[i][j].bind("<Motion>",self.creer_controleur_btn_motion(i,j))
                self.__listebutton[i][j].bind("<Leave>",self.creer_controleur_btn_leave())
    #--------------

    #Bouton nouvelle partie et quitter
        nouvellepartie=Button(self.__fen,text="Nouvelle partie",command=self.newgame)
        nouvellepartie.grid(row=int(self.__same.nblig()/2),column=self.__same.nbcol())
        quitter=Button(self.__fen,text="Quitter",command=self.__fen.destroy)
        quitter.grid(row=int(self.__same.nblig()/2)+1,column=self.__same.nbcol())
    #----------------------
        self.__lbptscompo= Label(self.__fen,text="Pts compo : ")
        self.__lbptscompo.grid(row=int(self.__same.nblig()/2)-2,column=self.__same.nbcol())
        self.__lbscore = Label(self.__fen, text="Score : "+str(self.__same.score()))
        self.__lbscore.grid(row=int(self.__same.nblig()/2) - 1,column=self.__same.nbcol())
    #----------------------
        self.__same.calcule_composantes()
        mainloop()
    
    def update(self):
        '''Met a jour les images des boutons selon la valeur dans self.__same'''
        for i in range(self.__same.nblig()):
            for j in range(self.__same.nbcol()):
                self.__listebutton[i][j].config(image=self.__images[self.__same.couleur(i,j)])
        self.recalc_composantes()
        self.__lbscore["text"] = "Score : "+str(self.__same.score())

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

    def creer_controleur_btn_motion(self,x,y):
        '''retrourne une fonction  /  return : function'''
        def controleur_btn_motion(event):
            '''passe toutes les images de boutons de la composante en noir'''
            composante=self.__same.composante(x,y)
            self.__lbptscompo["text"]="Pts compo : "+str(self.calcul_pts_composante(x,y))
            for i in range(self.__same.nblig()):
                for j in range(self.__same.nbcol()):
                    if self.__same.composante(i,j)==composante:
                        self.__listebutton[i][j].config(image=self.__images_n[self.__same.couleur(i,j)])
        return controleur_btn_motion

    def creer_controleur_btn_leave(self):
        '''Quand on quitte une composante la remet de couleur blanche'''
        def controleur_btn_leave(event):
            '''evenement quand on quitte le bouton'''
            self.update()
        return controleur_btn_leave

    def recalc_composantes(self):
        self.__same.reset_composante()
        self.__same.calcule_composantes()

    def calcul_pts_composante(self,i,j):
        '''Calcul le nombre de points de la compo'''
        return ((self.__same.nb_elmts_compo(self.__same.composante(i,j)))-2)**2


if __name__ == "__main__":
# création du modèle
    same = ModeleSame()
# création de la vue qui créé les contrôleurs
# et lance la boucle d’écoute des évts
    vue = VueSame(same)
