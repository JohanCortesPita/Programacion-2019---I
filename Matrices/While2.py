import math as m

def producto_escalar(escalar,vector):
    """
    num, list of num -> list of num

    "Funcion que calcula el producto escalar de un vector"

    >>> producto_escalar(2, (1,2,3))
    [2, 4, 6]

    :param escalar: El producto escalar
    :param vector: El vector ingresado
    :return: El producto escalar del vector
    """

    res = []
    cont = 0
    while cont < len(vector):
        res.append(escalar * vector[cont])
        cont += 1
    return res

def s_vectores(vector_1,vector_2):
    '''
    Calcula la suma de dos vectores

    (list of num, list of num) -> list of num2

    >>> s_vectores([1,2,3], [3,2,1])
    [4, 4, 4]
    >>> s_vectores([5,5,5], [5,5,5])
    [10, 10, 10]
    >>> s_vectores([1,2,3,4], [5,6,7])
    Traceback (most recent call last):
    ...
    ValueError: Los vectores tienen diferente dimesión

    :param vector_1: El vector ingresado
    :param vector_2: El vector a sumar
    :return: La suma de los vectores
    '''

    if len(vector_1) == len(vector_2):
        resultante = []
        for i in range(0, len(vector_1)):
            resultante.append(vector_1[i] + vector_2[i])
        return resultante
    else:
        raise ValueError('Los vectores tienen diferente dimesión')

def producto_punto(vector_1, vector_2):
    """
    (list of num, list of num) -> num

    Funcion que Calcula el producto punto de dos vectores

    >>> producto_punto([1, 2, 3], [1, 2, 3])
    14
    >>> producto_punto([2, 2, 2], [1, 2, 3])
    12
    >>> producto_punto([1, 2, 3, 4], [1, 2, 3])
    Traceback (most recent call last):
    ...
    ValueError: Los vectores tienen diferente dimensión

    :param v1: Vector 1
    :param v2: Vecotr 2
    :return: Calcula el producto punto de los dos vectores
    """
    if len(vector_1) == len(vector_2):
       resultado = 0
       for i in range(0, len(vector_1)):
           resultado += vector_1[i] * vector_2[i]
       return resultado
    else:
       raise ValueError('Los vectores tienen diferente dimensión')

def mayor_elemento(vector):
    '''

    Funcion que define cual es el mayor elemento del vector

    list of num -> num

    >>> mayor_elemento([1, 2, 3])
    3
    >>> mayor_elemento([4, 5, 6])
    6

    :param vector: Vector a calcular el mayor elemento
    :return: El elemento mayor del vector
    '''

    maximo = 0

    while maximo == 0:
        for i in range(len(vector)):
            if vector[i] > maximo:
                maximo = vector[i]
    return maximo


def menor_elemento(vector):
    '''
    Funcion que define cual es el mayor elemento del vector

    list of num -> num

    >>> menor_elemento([1,2,3])
    1
    >>> menor_elemento([4,5,6])
    4

    :param vector: Vector a calcular el mayor elemento
    :return: El elemento mayor del vector
    '''

    menor = 1000

    while menor == 1000:
        for i in range(len(vector)):
            if vector[i] < menor:
                menor = vector[i]
    return menor

def promedio(vector):
    '''
    Funcion que define el promedio del vector

    list of num -> num

    >>> promedio([2, 2, 2])
    2.0

    >>> promedio([2, 4, 6])
    4.0

    :param promedio: Ingresa el vector a validar
    :return: Retorna el promedio del vector
    '''

    sumaparcial = 0

    for valor in vector:
        sumaparcial += valor

    cantidad = len(vector)

    return sumaparcial/float(cantidad)
#

def comparar(vector_1, vector_2):
    """
    Funcion que compara dos vectores y retorna si es mayor menos o son iguales

    list of num -> str

    >>> comparar([1,2,3],[4,5,6])
    'menor'
    >>> comparar([2,9,7],[1,1,1,])
    'mayor'
    >>> comparar([2,2,2],[2,2,2])
    'igual'

    :param vector_1: Vector 1
    :param vector_2: Vector 2
    :return: Retorna si el vector 1 es mayor menor o igual
    """

    if norma(vector_1) > norma(vector_2):
        return 'mayor'
    elif norma(vector_1) < norma(vector_2):
        return 'menor'
    return 'igual'

def norma(vector):
    """
    Funciona que retorna la norma del vector

    list of num -> num

    >>> norma([2,5,4])
    11.0

    >>> norma([4,4,4])
    12.0

    :param vector: Vector a calcular
    :return: Retorna la norma del vector
    """

    norma = 0

    while norma == 0:
        for element in vector:
            norma += element
    return m.sqrt(norma**2)
