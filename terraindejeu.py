
#groupe 3 L1 MIASHS TD1
#Margaux Ulliac
#Sulayman Charpentier
#madjoua Djeti
#Fouad Abdoullah
#Sihem MADMAR

import tkinter as tk
from random import sample
import random as rd
def generateur_case(p, n):
	units=[(line, col) for col in range(n) for line in range(n)]
	trees=int(n**2*p)
	soil=sample(units, trees)
	states=[[0]*n for _ in range(n)]
	for (i, j) in soil:
	    states[i][j]=1
	return states

def coul_quad():
	for i in range(50):
		for j in range(50):
			r = rd.choice([0, p])
			if r == p:
				case=tk.Canvas(root, height = HEIGHT, width = WIDTH, bg="blue").grid(row = i, column = j)
			else :
				case=tk.Canvas(root, height = HEIGHT, width = WIDTH, bg="brown").grid(row = i, column = j)

HEIGHT=10
WIDTH=10
cases = []
p=0.5
n=4
unit=10
import random
###Constantes###
HEIGHT=50
WIDTH=50
nb_voisins= random.randint(0, 8)
cote= 10
p= 0.5
T= 5
couleur=["green","blue"]
eau= 1
terre= 0
# Matrices #
#Mémorise les cellules#
cell = [[0 for row in range(HEIGHT)] for col in range(WIDTH)] 
#Mémorise l'état initial des cellules#
etat = [[terre for row in range(HEIGHT)] for col in range(WIDTH)]
# Mémorise le nouvel état des cellules#
temp = [[terre for row in range(HEIGHT)] for col in range(WIDTH)]
# Fonctions du programme #

def quad():
     """ Quadrille le terrain et place des cellules de terre en fonction de p"""
     # placer au hasard environ 50% de cellules de terre###
     for i in range(HEIGHT):
         for j in range(WIDTH):
             r=random.randrange(0, 10, 1)
             if r < (p*10) :
                 etat[i][j] = terre
             else : etat[i][j]=eau

     for y in range(HEIGHT):
         for x in range(WIDTH):
             temp[x][y] = etat[x][y]
             cell[x][y] = canvas.create_rectangle((x*cote, y*cote, 
                         (x+1)*cote, (y+1)*cote), outline="gray", fill=couleur[etat[x][y]])

def dessiner():
     """ Dessine les cellules """
     for y in range(HEIGHT):
         for x in range(WIDTH):
             if etat[x][y]==1:
                 coul = "blue"
             else:
                 coul = "green"
             canvas.itemconfig(cell[x][y], fill=coul)

def case_eau(a,b):
     """ Compte les cases d'eau """
     if etat[(a-1)%WIDTH][(b+1)%HEIGHT] == 1:
         nb_voisins += 1
     if etat[a][(b+1)%HEIGHT] == 1:
         nb_voisins += 1
     if etat[(a+1)%WIDTH][(b+1)%HEIGHT] == 1:
         nb_voisins += 1
     if etat[(a-1)%WIDTH][b] == 1:
         nb_voisins += 1
     if etat[(a+1)%WIDTH][b] == 1:
         nb_voisins += 1
     if etat[(a-1)%WIDTH][(b-1)%HEIGHT] == 1:
         nb_voisins += 1
     if etat[a][(b-1)%HEIGHT] == 1:
         nb_voisins += 1
     if etat[(a+1)%WIDTH][(b-1)%HEIGHT] == 1:
         nb_voisins += 1

     return nb_voisins

def perso():
     x= random.randint(0, WIDTH)
     y= random.randint(0, HEIGHT)
     canvas.itemconfig(cell[x][y], fill="black")

def calculer():
     """ Création des cases d'eau et de terre en fonction du voisinage"""
     global nb_voisins
     n= 0
     while n != 4:
         for y in range(HEIGHT):
             for x in range(WIDTH):
                           
# Naissance d'une case de terre #
                 if etat[x][y] == eau and nb_voisins < T :
                     temp[x][y] = terre

                 elif etat[x][y] == terre and nb_voisins < T :
                     temp[x][y] = terre

# Naissance d'une case d'eau #
                 if etat[x][y] == terre and T <= nb_voisins :
                     temp[x][y] = eau

                 if etat[x][y] == eau and T <= nb_voisins :
                     temp[x][y] = eau

                 for y in range(HEIGHT):
                     for x in range(WIDTH):
                         etat[x][y] = temp[x][y]
         n = n+1

def tableau():
     """ Calcul et dessin du prochain tableau """
     calculer()
     dessiner()
     root.after(500, tableau)


root= tk.Tk()
root.title('Terrain de jeu')
canvas= tk.Canvas(root, height=HEIGHT, width=WIDTH, bg='white')
canvas= tk.Canvas(root, height=HEIGHT, width=WIDTH, bg='blue')
canvas.grid(row = 0, column = 0, columnspan=2, padx=3, pady=3)
for i in range(50):
            for j in range(50):
                  tk.Canvas(root, height = HEIGHT, width = WIDTH, highlightbackground = 'black').grid(row = i, column = j)
states = generateur_case(p, n)
coul_quad()
quad()
tableau()
perso()
canvas.bind("KP_UP", perso)
canvas.bind("KP_Down", perso)
canvas.bind("KP_Left", perso)
canvas.bind("KP_Right", perso)
root.mainloop()
