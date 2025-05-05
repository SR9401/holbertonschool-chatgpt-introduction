#!/usr/bin/python3
import sys

def factorial(n):
    if n < 0:
        raise ValueError("Le factoriel n'est pas défini pour les entiers négatifs.")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

if __name__ == "__main__":
    try:
        if len(sys.argv) != 2:
            raise ValueError("Utilisation : ./factorial.py <entier>")
        n = int(sys.argv[1])
        f = factorial(n)
        print(f)
    except ValueError as e:
        print(f"Erreur : {e}")
    except Exception as e:
        print(f"Une erreur inattendue est survenue : {e}")
