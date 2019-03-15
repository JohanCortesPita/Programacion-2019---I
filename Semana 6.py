#numero = input('Ingrese un numero')

#try:
#    print('Su numero {0} al cuadrado es {1}'.format(numero, float(numero) ** 2))

#except:

#    print("'{0}' no es un numero".format(numero))

num1 = input('Ingrese el numero a dividir')
num2 = input('Ingrese el dividiendo')

try:

    print('Su numero {0} divido por {1} es {2}'.format(num1,num2, float(num1) / float(num2) ))

except ZeroDivisionError:

    print("no dividiras por 0")

except ValueError:

    print('Ingrese solo numeros')