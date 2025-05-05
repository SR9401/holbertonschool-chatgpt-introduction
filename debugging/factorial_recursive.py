#!/usr/bin/python3
import sys

def factorial(n):
    """
    Calcule récursivement la factorielle d'un entier non négatif.

    Paramètres :
        n (int) : Un entier non négatif dont on veut calculer la factorielle.

    Retourne :
        int : La factorielle de n (n!), c’est-à-dire le produit de tous les entiers de 1 à n.
              Si n vaut 0, retourne 1 (par définition).
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Lecture de l'argument passé en ligne de commande
f = factorial(int(sys.argv[1]))
# Affichage du résultat
print(f)
