import math


def resoudreEquation(a, b, c):
    # TODO: Calculer le discriminant et assigner la valeur dans la variable "delta"
    delta = (b**2)- 4*(a*c)

    # TODO: Déterminer la condition (bool) qui correspond à aucune solution de l'équation et mettre la valeur dans la variable "naPasDeSolution"
    if delta < 0:
        naPasDeSolution = bool(True)
    else:
        naPasDeSolution = bool(False)

    if naPasDeSolution == True:
        # ces ligne de code seront executé si il y'a aucune racine
        # TODO: afficher sur l'écran "Aucune racine"
        print("Aucune racine")
        # ne pas modifier
        return None

    # TODO: Déterminer la condition (bool) qui correspond à une unique solution de l'équation et mettre la valeur dans "aUneSeuleSolution"
    if delta == 0:
        aUneSeuleSolution = bool(True)
    else:
        aUneSeuleSolution = bool(False)

    if aUneSeuleSolution == True:
        # ces ligne de code seront executé si il y'a une seule racine
        # TODO: afficher sur l'écran "Une seule racine"
        print("Une seule racine")
        # TODO: assigner a la variable x1 la valeur de la racine
        x1 = delta**(0.5)
        # ne pas modifier
        return x1

    # TODO: Déterminer la condition (bool) qui correspond à deux solutions de l'équation et mettre la valeur dans "aDeuxSolutions"
    if delta > 0:
        aDeuxSolutions = bool(True)

    if aDeuxSolutions == True:
        # TODO: afficher sur l'écran "Deux racines"
        print("Deux racines")
        # TODO: calculer la prmiere racine, assigner la a "x1"
        x1 = -1*(delta**(0.5))

        # TODO: calculer la deuxieme racine, assigner la a "x2"
        x2 = delta**(0.5)

        # ne pas modifier cette ligne
        return x1, x2


if __name__ == '__main__':
    a = int(input("Entrez a, non nul: "))
    b = int(input("Entrez b: "))
    c = int(input("Entrez c: "))

    print(resoudreEquation(a, b, c))
