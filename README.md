ROUANET Matthieu
BAUDEQUIN Clément
RAMOND Nicolas

Exercice 5 - Version 0.0.1


Bugs : 
1- Si toutes les cases sont remplies sans qu'il n'y ait de gagnant, le jeu ne s'arrête pas.
Suggestion : Implémenter un compteur qui va jusqu'à 42, et s'il l'atteint, indiquer qu'il y a égalité et arrêter la partie.

2- Lorsqu'un joueur gagne, on ne peut plus jouer, il faut relancer le code.
Suggestion : Implémenter un bouton pour refaire une partie sur l'interface lorsqu'une partie est finie.


Code cleaning :
1- La fonction jeton possède deux Return, c'est une mauvaise pratique (travail de cochon).
Suggestion : Stocker la valeur dans une variable, puis retourner la variable.
2- La fonction coup_gagnant possède CINQ returns .........
Suggestion : Stocker la valeur dans une variable, puis retourner la variable.