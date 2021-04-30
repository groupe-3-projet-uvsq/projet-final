
#groupe 3 L1 MIASHS TD1
#Margaux Ulliac
#Sulayman Charpentier
#madjoua Djeti
#Fouad Abdoullah
#Sihem MADMAR

import tkinter as tk
from random import sample
Colors=["green2 ", "cyan"]
def generateur_case(p, n):
	units=[(line, col) for col in range(n) for line in range(n)]
	ntrees=int(n**2*p)
	trees=sample(units, ntrees)
	states=[[0]*n for _ in range(n)]
	for (i, j) in trees:
	    states[i][j]=1
	return states
def fill(states): 
    n=len(states)
    for line in range(n):
        for col in range(n):
            fill_cell(states, line, col)
def fill_cell(states, line, col):
        A=(unit*col, unit*line)
        B=(unit*(col+1), unit*(line+1))
        state=states[line][col]
        color=Colors[state]
        canvas.create_rectangle(A, B, fill=color, outline='black')
	
###Import des librairies###
import tkinter as tk
import random as rd

###Constantes###
HEIGHT=10
WIDTH=10
p=0.5
n=4	

### Fonctions ###
def coul_quad():
    "Creation des cellules d'eau ou de terre"  
    for i in range(50):
        for j in range(50):
            r = rd.choice([0, p])
            if r == p:
                case=tk.Canvas(root, height = HEIGHT, width = WIDTH, bg="blue").grid(row = i, column = j)
                
            else :
                case=tk.Canvas(root, height = HEIGHT, width = WIDTH, bg="brown").grid(row = i, column = j)

		
### Programme principal ###
root= tk.Tk()
root.title('Terrain de jeu')
canvas= tk.Canvas(root, height=HEIGHT, width=WIDTH, bg="blue")
canvas.grid(row = 0, column = 0, columnspan=2, padx=3, pady=3)


### Appel des fonctions ###
coul_quad()
creer_tableau()


### Lancement de la boucle ###
root.mainloop()
