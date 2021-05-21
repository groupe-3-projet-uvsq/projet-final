
#groupe 3 L1 MIASHS TD1
#Margaux Ulliac
#Sulayman Charpentier
#madjoua Djeti
#Fouad Abdoullah
#Sihem MADMAR


import tkinter as tk
import random 

###Constantes###
HEIGHT=50
WIDTH=50

cote= 10
p= 0.5
T= 5
couleur=["green","blue"]
eau= 1
terre= 0
nb_col= WIDTH// cote
nb_lig= HEIGHT// cote
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
    cpt= 0
    if etat[(a-1)%WIDTH][(b+1)%HEIGHT] == 1:
       cpt += 1
    if etat[a][(b+1)%HEIGHT] == 1:
        cpt += 1
    if etat[(a+1)%WIDTH][(b+1)%HEIGHT] == 1:
        cpt += 1
    if etat[(a-1)%WIDTH][b] == 1:
        cpt += 1
    if etat[(a+1)%WIDTH][b] == 1:
        cpt += 1
    if etat[(a-1)%WIDTH][(b-1)%HEIGHT] == 1:
        cpt += 1
    if etat[a][(b-1)%HEIGHT] == 1:
        cpt += 1
    if etat[(a+1)%WIDTH][(b-1)%HEIGHT] == 1:
        cpt += 1
    return cpt
    


def calculer():
    """ Création des cases d'eau et de terre en fonction du voisinage"""
    a = random.randint(0, HEIGHT)
    b = random.randint(0, WIDTH)
    nb_voisins = case_eau(a, b)
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


def perso():
    x= random.randint(0, WIDTH)
    y= random.randint(0, HEIGHT)
    cell[x][y] = canvas.create_rectangle((x*cote, y*cote, 
                        (x+1)*cote, (y+1)*cote), outline="gray", fill="black")



def tableau():
    """ Calcul et dessin du prochain tableau """
    calculer()
    dessiner()
    perso()
    root.after(100, tableau)
      
                
# Programme principal #
root= tk.Tk()
root.title('Terrain de jeu')
canvas= tk.Canvas(root, height=HEIGHT*cote, width=WIDTH*cote, bg="white")
canvas.grid(row = 0, column = 0, columnspan=2, padx=3, pady=3)

# Appel des fonctions #
quad()
tableau()


# Liaison des evènenements #
# canvas.bind("<keysym-80>", perso)
# canvas.bind("<keysym-88>", perso)
# canvas.bind("<keysym-83>", perso)
#  canvas.bind("<keysym-85>", perso)

# Lancement de la boucle principal #
root.mainloop() 
