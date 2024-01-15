from noyau import *
import pytest

def test_changer_joueur():
    assert changer_joueur(0) == 1
    assert changer_joueur(1) == 0
    assert changer_joueur(28) == 1
    assert changer_joueur(27) == 0
    assert changer_joueur(-28) == 1
    assert changer_joueur(-27) == 0

