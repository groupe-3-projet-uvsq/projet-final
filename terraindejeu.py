
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

HEIGHT=10
WIDTH=10
cases = []
p=0.5
n=4
unit=10
root= tk.Tk()
root.title('Terrain de jeu')
canvas= tk.Canvas(root, height=HEIGHT, width=WIDTH, bg='white')
canvas.grid(row = 0, column = 0, columnspan=2, padx=3, pady=3)
for i in range(50):
            for j in range(50):
                  tk.Canvas(root, height = HEIGHT, width = WIDTH, highlightbackground = 'black').grid(row = i, column = j)
states = generateur_case(p, n)
i=n//2
j=0
states[i][j]=2
fill(states)
root.mainloop()
