def pointDeRencontre(v1, v2, distance):
    # TODO faites les calculs intermediaires, vous pouvez initialiser des variables locales.
    vitesse_finale = 0
    position_initiale1 = 0
    position_intiale2 = distance
    temps = (2*position_intiale2)/((v1-v2))

    # TODO calculer la position de rencontre, assignez la valeur à la variable "positionRencontre"

    positionRencontre = (((v2+vitesse_finale)*temps)/2)+distance

    return positionRencontre

if __name__ == '__main__':
    v1 = int(input("Entrez v1: "))
    v2 = int(input("Entrez v2: "))
    distance = int(input("Entrez la distance: "))
    print(pointDeRencontre(v1, v2, distance))
