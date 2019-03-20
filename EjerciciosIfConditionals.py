def mensaje_negativo(numero):
    """
    (float) -> str
    Escribe un mensaje para evaluar un numero negativo
    >>> mensaje_negativo(-10.0)
    'El numero es negativo'
    >>> mensaje_negativo(898)
    'El numero es positivo'

    :param numero: num el numero a evaluar
    :return: str con el mensaje de la evaluación
    """
    if numero < 0:
        return 'El numero es negativo'
    return 'El numero es positivo'

def compara_edades(edad1, edad2):
    """
    (int, int) -> str
    Genera un mensaje segun la diferencia de edad:
    la primera o la segunda mas joven o iguales
    >>> compara_edades(10, 20)
    'El primero es mas joven'
    >>> compara_edades(89, 56)
    'El segundo es mas joven'
    >>> compara_edades(56, 56)
    'Tienen la misma edad'

    :param edad1: int la edad del primero
    :param edad2: int la edad del segundo
    :return: mensaje asociado a la diferencia de edad
    """
    if edad1 > edad2:
        return 'El segundo es mas joven'
    elif edad1 == edad2:
        return 'Tienen la misma edad'
    else:
        return 'El primero es mas joven'


def es_parentesis(caracter):
    """
    (str of len == 1) -> str
    >>> es_parentesis('(')
    'Es parentesis'
    >>> es_parentesis('x')
    'No es parentesis'
    >>> es_parentesis('xa')
    Traceback (most recent call last):
    ..
    TypeError: xa no es un parentesis

    :param caracter: str el caracter a evaluar
    :return: str el mensaje de la validacion
    """
    if len(caracter) != 1:
        raise TypeError(str(caracter) + ' no es un parentesis')
    elif caracter in '()': # caracter == '(' or caracter == ')':
        return 'Es parentesis'
    return 'No es parentesis'


def dividir(dividendo, divisor):
    '''
    (num, num) -> num
    Divide un numero entre otro
    >>> dividir(6, 2)
    3.0
    >>> dividir(1,0)
    Traceback (most recent call last):
    ..
    ZeroDivisionError: No dividiras por 0
    >>> dividir('hola', 100)
    Traceback (most recent call last):
    ..
    TypeError: hola no es un numero

    :param dividendo: num el dividendo a evaluar
    :param divisor: num el divisor a evaluar
    :return: la división entre dividendo y divisor
    '''
    if  int != type(dividendo) != float:
        raise TypeError(str(dividendo) + ' no es un numero')
    elif int != type(divisor) != float:
        raise TypeError(str(divisor) + ' no es un numero')
    elif divisor == 0:
        raise ZeroDivisionError('No dividiras por 0')
    return dividendo / divisor

def doble_impar(numero):
    '''
    (int) -> str

    Recibe un numero y define cual es la mitad del numero, asi mismo indica si es impar la mitad

    >>> doble_impar(14)
    'El doble del numero es un numero impar'

    >>> doble_impar(12)
    'El doble del numero no es un numero impar'

    >>> doble_impar(0)
    'El doble del numero no es un numero impar'

    >>> doble_impar('Adios')
    Traceback (most recent call last):
    ..
    TypeError: Adios no es un numero o es un float


    :param numero: El numero ingresado
    :return: El numero primo si es el doble del enterado
    '''

    if int != type(numero):
        raise TypeError(str(numero) + ' no es un numero o es un float')
    elif (numero/2) % 2 == 0:
        return 'El doble del numero no es un numero impar'
    else:
        return 'El doble del numero es un numero impar'

def comparar_cuadrado(num1,num2):
    """
    (int,int) -> str

    >>> comparar_cuadrado(2,4)
    'El segundo es el cuadrado del primero'

    >>> comparar_cuadrado(2,3)
    'El segundo es menor que el cuadrado del primero'

    >>> comparar_cuadrado(2,5)
    'El segundo es mayor que el cuadrado del primero'

    >>> comparar_cuadrado('bye', 100)
    Traceback (most recent call last):
    ..
    TypeError: Alguno de los datos ingresados no es un numero

    :param num1: Numero ingresado para evaluar el cuadrado
    :param num2: Numero ingresado para evaluar si es mayor o menos
    :return: Define si el cuadrado del primer numero es mayor o menor
    """

    if int != type(num1) or int != type(num2):
        raise TypeError('Alguno de los datos ingresados no es un numero')
    elif (num1*num1) == num2:
        return 'El segundo es el cuadrado del primero'
    elif (num1*num1) < num2:
        return 'El segundo es mayor que el cuadrado del primero'
    else:
        return 'El segundo es menor que el cuadrado del primero'

def numero_primo(num):
    '''
    (int)-> str: si es primo o no
    >>> numero_primo(2)
    'es un numero primo'
    >>> numero_primo(4)
    'no es un numero primo'
    >>> numero_primo('s')
    Traceback (most recent call last):
    ..
    TypeError: <class 'str'> no es un entero

    :param num: numero a determinar si es o no primo
    :return: str: mensaje si el numero es primo o no
    '''

    if(int != type(num)):
        raise TypeError(str(type(num)) + ' no es un entero')
    elif ((num%2==0 and num!=2) or (num%3==0 and num!=3) or (num%5==0 and num!=5) or (num%7==0 and num != 7)):
        return 'no es un numero primo'
    else:
        return 'es un numero primo'



