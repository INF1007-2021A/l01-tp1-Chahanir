def fizzBuzz(n):
    # TODO imprimer la chaine de caractère appropriée avec la fonction print().
    #  Assigner ensuite la valeur à la variable resultat
    valeur = n
    if valeur % 3 == 0:
        if valeur % 5 == 0:
            resultat = 'fizzbuzz'

        else:
            resultat = 'fizz'
    elif valeur % 5 == 0:
        resultat = 'buzz'
    else:
        resultat = 'ledit'

    return resultat


if __name__ == '__main__':
    n = int(input("indiquez le nombre: "))
print (fizzBuzz(n))





