def tringulo(*args):

    if len(set(args)) <= 1:
        return 'triangulo equilatero'
    elif len(set(args)) == 2:
        return 'tringulo Isosceles'
    return


print(tringulo(8, 5, 3))
