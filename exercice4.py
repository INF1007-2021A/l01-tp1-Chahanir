import math


def calculerPosition(positionInitiale, vitesseInitiale, duree, vitesseFinale):
    # TODO faites les calculs intermediaires, vous pouvez initialiser des variables locales.

    variationPosition = (((vitesseInitiale/3.6) + (vitesseFinale/3.6)) * (duree)/2) #Note : 1m/s = 3.6km/h#

    # TODO calculer la position finale, assigner la valeur à la variable "positionFinale"
    positionFinale = variationPosition + positionInitiale

    return positionFinale

if __name__ == '__main__':
    positionInitiale = int(input("Entrez la position initiale en mètre: "))
    vitesseInitiale = int(input("Entrez la vitesse initiale en km/h: "))
    duree = int(input("Entrez la duree en secondes: "))
    vitesseFinale = int(input("Entrez la vitesseFinale en km/h: "))
    print(calculerPosition(positionInitiale, vitesseInitiale, duree, vitesseFinale))

