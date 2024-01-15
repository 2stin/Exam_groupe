from noyau import *
import pytest


grille_perdante = [[-1,-1,-1,-1,-1,-1,-1],
                   [-1,-1,-1,-1,-1,-1,-1],
                   [-1,-1,-1,-1,-1,-1,-1],
                   [-1,-1,-1,-1,-1,-1,-1],
                   [-1,-1,-1,-1,-1,-1,-1],
                   [-1,-1, 0,-1,-1,-1,-1]]

grille_horizontale = [[-1,-1,-1,-1,-1,-1,-1],
                      [-1,-1,-1,-1,-1,-1,-1],
                      [-1,-1,-1,-1,-1,-1,-1],
                      [-1,-1,-1,-1,-1,-1,-1],
                      [-1,-1,-1,-1,-1,-1,-1],
                      [-1, 0, 0, 0, 0,-1,-1]]

grille_NE_SO = [[-1,-1,-1,-1,-1,-1,-1],
                [-1,-1,-1,-1,-1,-1,-1],
                [-1,-1,-1,-1, 0,-1,-1],
                [-1,-1,-1, 0, 1,-1,-1],
                [-1,-1, 0, 1, 1,-1,-1],
                [ 0, 0, 1, 1, 1, 0, 0]]

grille_NO_SE = [[-1,-1,-1,-1,-1,-1,-1],
                [-1,-1,-1,-1,-1,-1,-1],
                [-1,-1, 0,-1,-1,-1,-1],
                [-1,-1, 1, 0,-1,-1,-1],
                [-1, 0, 1, 1, 0,-1,-1],
                [-1, 0, 1, 1, 1, 0,-1]]

grille_verticale = [[-1,-1,-1,-1,-1,-1,-1],
                    [-1,-1,-1,-1,-1,-1,-1],
                    [-1,-1, 0,-1,-1,-1,-1],
                    [-1,-1, 0,-1,-1,-1,-1],
                    [-1,-1, 0,-1,-1,-1,-1],
                    [-1,-1, 0,-1,-1,-1,-1]]



def test_changer_joueur():
    assert changer_joueur(0) == 1
    assert changer_joueur(1) == 0
    assert changer_joueur(28) == 1
    assert changer_joueur(27) == 0
    assert changer_joueur(-28) == 1
    assert changer_joueur(-27) == 0

def test_coup_gagnant():
    assert coup_gagnant(0, 5, 2, grille_perdante) == False
    assert coup_gagnant(0, 5, 2, grille_horizontale) == True
    assert coup_gagnant(0, 5, 1, grille_NE_SO) == True
    assert coup_gagnant(0, 3, 3, grille_NO_SE) == True
    assert coup_gagnant(0, 2, 2, grille_verticale) == True

def test_jeton():
    assert jeton(0, -1, 3, 3, 3, True) == 0
    assert jeton(0, 3, -1, 3, 3, True) == 0
    assert jeton(0, 8, 3, 3, 3, True) == 0
    assert jeton(0, 3, 8, 3, 3, True) == 0
    #assert jeton(0, 2, 5, 3, 3, True) == 1+jeton(0, 5, 8, 3, 3, grille_horizontale)

