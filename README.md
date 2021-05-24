# projet-final
projet génération terrain de jeu

Le projet de génération de terrain de jeu video comporte deux grandes parties distinctes: 
  générer aléatoirement et continuellement un terrain de jeu changeant entre deux types de cases de jeu
  incorporer un personnage qui pourra jouer en fonction des contraintes des cases de jeu

Instruction pour l'utilisateur:

L'utilisateur doit entrer les valeurs qu'il aura choisies dans le terminal.
Trois valeurs lui seront demandées.
Les deux premières valeurs doivent être positives et inférieures à 200.
La dernière valeur doit être positive et inférieure à 10.
Pour placer son personnage, l'utilisateur doit faire un double-clic droit. 
Pour retirer son personnage, l'utilisateur doit faire un clic droit sur la cellule sur laquelle il a cliqué.

Explication sur certaines fonctions que nous n'avons pas réussies à faire fonctionner:

La fonction perso(event) peut normalement permettre à l'utilisateur de déplacer son personnage en maintenant la touche Alt+ l'une des flèches du clavier, mais cette fonction est laissée en commentaire.
La fonction recharger() ne fonctionne pas, celle-ci permet de recharger le fichier sauvegarde.txt et renvoie le tableau.
