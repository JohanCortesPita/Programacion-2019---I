#cadena = 'weggergerhterhtbhfmag{war{njqeewjofvn '

#for letra in cadena:
    #print(letra)

def es_vocal(letra):
    """

    Valida si una letra es vocal

    >>> es_vocal('a')
    True
    >>> es_vocal('b')
    False
    >>> es_vocal('ae')
    Traceback (most recent call last):
    ..
    ValueError: ae no es una letra

    >>> es_vocal('1')
    Traceback (most recent call last):
    ..
    ValueError: 1 no es una letra

    :param letra:
    :return:
    """
    if (len(letra) == 1 and letra.isalpha()):
        return letra in 'aeiouAEIOU'
    raise ValueError(letra + ' no es una letra')

def contar_vocales(cadena):
    """

    :param cadena:
    :return:
    """
    pass

    contador = 0

    for letra in cadena:
        if es_vocal(letra):
            contador += 1
    return  contador

def contar_consonante(cadena):
    return len(cadena) - contar_vocales(cadena)



