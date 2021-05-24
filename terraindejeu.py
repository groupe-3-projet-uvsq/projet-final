
#groupe 3 L1 MIASHS TD1
#Margaux Ulliac
#Sulayman Charpentier
#madjoua Djeti
#Fouad Abdoullah
#Sihem MADMAR

#Import des librairies#
import tkinter as tk
import random 
import copy

#Constantes#
HEIGHT = int(input("Entrer un nombre"))
WIDTH = int(input("Entrer un nombre"))
T = int(input("Entrer un nombre"))
p = 0.5
cote = 10
nb_col = WIDTH // cote
nb_line = HEIGHT // cote
couleur =["green","blue"]
eau = 1
terre = 0
nb_terre = HEIGHT*WIDTH
nb_eau = 0

#Variables globales#
cpt = 0

# Matrices #
#Mémorise les cellules#
cell = [[0 for row in range(HEIGHT)] for col in range(WIDTH)] 
#Mémorise l'état initial des cellules#
etat = [[terre for row in range(HEIGHT)] for col in range(WIDTH)]
# Mémorise le nouvel état des cellules#
temp = [[terre for row in range(HEIGHT)] for col in range(WIDTH)]


# Fonctions du programme #

def dessiner():
    #Dessine les cellules#
    for y in range(HEIGHT):
        for x in range(WIDTH):
            if etat[x][y]==1:
                coul = "blue"
            else:
                coul = "green"
            canvas.itemconfig(cell[x][y], fill=coul)


def quad():
        #Quadrille le terrain et place des cellules de terre en fonction de p#
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
    dessiner()


def nb_voisin(a,b):
       #Compte les cases voisines#
    voisin = random.randrange(8)
    if voisin==1:
        couleur = etat[(a-1)%WIDTH][(b+1)%HEIGHT]
    elif voisin==2:
        couleur = etat[a][(b+1)%HEIGHT]
    elif voisin==3:
        couleur = etat[(a+1)%WIDTH][(b+1)%HEIGHT]
    elif voisin==4:
        couleur = etat[(a-1)%WIDTH][b]
    elif voisin==5:
        couleur = etat[(a+1)%WIDTH][b]
    elif voisin==6:
        couleur = etat[(a-1)%WIDTH][(b-1)%HEIGHT]
    elif voisin==7:
        couleur = etat[a][(b-1)%HEIGHT]
    else:
        couleur = etat[(a+1)%WIDTH][(b-1)%HEIGHT]
    return couleur


def nouvel_etat():
       #Dessine le nouvel etat des cellules en fonction des voisins#
    global nb_terre, nb_eau
    x = random.randrange(HEIGHT)
    y = random.randrange(WIDTH)
    nouvelle_cell = nb_voisin(x,y)
    if etat[x][y] != nouvelle_cell:
        if nouvelle_cell == terre:
            nb_terre += 1
            nb_eau -= 1
        else :
            nb_terre -= 1
            nb_eau += 1
            etat[x][y] = nouvelle_cell
        if etat[x][y] == terre:
            coul = "green"
        else:
            coul = "blue"
        canvas.itemconfig(cell[x][y], fill=coul)
    

def coord_to_lg(x, y):
       #Fonction qui retourne la colonne et la ligne du quadrillage
    à partir des coordonnées x et y#
    return x // cote, y // cote


def perso(event):
       #Place le personnage#
    i, j = coord_to_lg(event.x, event.y)
    if etat[i][j] == -1:
        x, y = i * cote, j * cote
        carre = canvas.create_rectangle(x, y, x + cote,
                                        y + cote, fill="black",
                                        outline="gray")
        etat[i][j] = carre
    else:
        canvas.delete(etat[i][j])
        etat[i][j] = -1


def tableau():
       #Retourne du prochain tableau#
    nouvel_etat()
    root.after(100, tableau)
    
def lectureFichierSauvegarde():
	   #Sauvegarde le tableau dans le fichier sauvegarde.txt#
	fichier = open("sauvegarde.txt", "w")
	for j in range(HEIGHT):
		for i in range(WIDTH):
			fichier.write(str(temp[i][j]) + "\n")
	fichier.close()
    
    #def recharger():
	 ## Fonction qui recharge le fichier sauvegarde.txt et qui renvoie le tableau##
	fichier = open("sauvegarde.txt","r")
	cpt = 0
	for ligne in fichier:
		i, j = cpt% nb_col, cpt // nb_col
		if temp[i][j] != -1:
			canvas.delete(temp[i][j])
		n = int(ligne)
		if n == -1:
			temp[i][j] = -1
		else:
			x, y = i * cote, j * cote
			carre = canvas.create_rectangle(x, y, x + cote, y + cote, fill= couleur[etat[x][y]], outline="grey")
			temp[i][j] = carre
		cpt += 1
	fichier.close()#
    
    
                     
# Programme principal #
root= tk.Tk()
root.title('Terrain de jeu')
canvas= tk.Canvas(root, height=HEIGHT*cote, width=WIDTH*cote, bg="white")
canvas.grid(row = 0, column = 0, columnspan=2, padx=3, pady=3)

# Appel des fonctions #
quad()
tableau()

#Création des widgets#
btn_lectureFichierSauvegarde = tk.Button(root, text="sauvegarder", command=lectureFichierSauvegarde)
#btn_recharger = tk.Button(root, text="recharger", command=recharger)#

#Emplacement des widgets#
btn_lectureFichierSauvegarde.grid(column=0, row=4)
#btn_recharger.grid(column = 1, row= 4)#

# Liaison des evènenements #
canvas.bind("<Button-1>", perso)
#canvas.bind("<Alt-Up>", perso)
#canvas.bind("<Alt-Down>", perso)
#canvas.bind("<Alt-Right>", perso)
#canvas.bind("<Alt-Left>", perso)

# Lancement de la boucle principal #
root.mainloop() 

