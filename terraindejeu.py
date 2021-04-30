
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
	ntrees=int(n**2*p)
	trees=sample(units, ntrees)
	states=[[0]*n for _ in range(n)]
	for (i, j) in trees:
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
root= tk.Tk()
root.title('Terrain de jeu')
canvas= tk.Canvas(root, height=HEIGHT, width=WIDTH, bg='white')
canvas= tk.Canvas(root, height=HEIGHT, width=WIDTH, bg='blue')
canvas.grid(row = 0, column = 0, columnspan=2, padx=3, pady=3)
for i in range(50):
            for j in range(50):
                  tk.Canvas(root, height = HEIGHT, width = WIDTH, highlightbackground = 'black').grid(row = i, column = j)
states = generateur_case(p, n)
i=n//2
j=0
states[i][j]=2
coul_quad()
root.mainloop()
