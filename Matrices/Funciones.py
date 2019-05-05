import While2 as f
vectores = {}

def ingresar_vector():
    """

    """
    vector = [input('¿Cual es el nombre de su vector?')]

    while True:
        num = input('Ingrese su vector o "s" para terminar')
        if num.lower() != 's':
            try:
                num = int(num)
                vector.append(num)
            except:
                print(num, 'no es un escalar')
        else:
            break
    return vector

def mostrar_vectores():
    for nombre in vectores:
        print(nombre, 'contiene', vectores[nombre])

def op_producto_escalar():
    while True:
        escalar = input('Ingrese su escalar ')
        try:
            escalar = int(escalar)
        except:
            print(escalar, 'no es un escalar')
            break

        seleccion = input('Cual es el nombre del vector con el cual quiere trabajar: ')
        mostrar_vectores()
        print('\n El producto escalar es: ', f.producto_escalar(escalar, vectores[seleccion]))
        break

def op_suma_vectores():
    valor = 1
    seleccion = []
    if (len(vectores) < 2):
        print('Debe haber ingresado por lo menos dos vectores para realizar la suma, Escriba 1 para hacerlo')
        return "No hay 2 vectores"
    while valor <= 2:
        try:
            print('escoja el vector ', valor)
            mostrar_vectores()
            seleccion.append(input())
            valor += 1
        except:
            print('No se encontro ningun vector, Ingrese un vector correcto')
    print('la suma es ', f.s_vectores(vectores[seleccion[0]], vectores[seleccion[1]]))

def op_producto_punto():

    valor = 1
    seleccion = []
    if (len(vectores) < 2):
        print('Debe haber ingresado por lo menos dos vectores para realizar el producto punto, Escriba 1 para hacerlo')
        return ""
    while valor <= 2:
        try:
            print('escoja el vector  ', valor)
            mostrar_vectores()
            seleccion.append(input())
            valor += 1
        except:
            print('No se encontro ningun vector, Ingrese un vector correcto')
    print('el producto punto es ', f.producto_punto(vectores[seleccion[0]], vectores[seleccion[1]]))

def op_mayor_elemento():
    valor = 1
    seleccion = []
    if (len(vectores) < 1):
        print('Debe haber ingresado por lo menos un vector para evaluar el mayor, Escriba 1 para hacerlo')
        return ""

    while valor <= 1:
        try:
            print('escoja el vector ', valor)
            mostrar_vectores()
            seleccion.append(input())
            valor += 1
        except:
            print('No se encontro ningun vector, Ingrese un vector correcto')
    print('el mayor elemento del vector es ', f.mayor_elemento(vectores[seleccion[0]]))

def op_menor_elemento():
    valor = 1
    seleccion = []
    if (len(vectores) < 1):
        print('Debe haber ingresado por lo menos un vector para evaluar el menor elemento, Escriba 1 para hacerlo')
        return ""
    while valor <= 1:
        try:
            print('escoja el vector ', valor)
            mostrar_vectores()
            seleccion.append(input())
            valor += 1
        except:
            print('No se encontro ningun vector, Ingrese un vector correcto')
    print('El menor elemento del vector es ', f.menor_elemento(vectores[seleccion[0]]))

def op_promedio():
    valor = 1
    seleccion = []
    if(len(vectores) <1 ):
        print('Debe haber ingresado por lo menos un vector para realizar el promedio, Escriba 1 para hacerlo')
        return ""
    while valor <= 1:
        try:
            print('escoja el vector ', valor)
            mostrar_vectores()
            seleccion.append(input())
            valor+=1
        except:
            print('No se encontro ningun vector, Ingrese un vector correcto')
    print('el promedio del vector es ', f.promedio(vectores[seleccion[0]]))

def op_comparar():
    valor = 1
    seleccion = []
    if(len(vectores) <2):
        print('Debe haber ingresado por lo menos dos vectores para realizar la comparacion, Escriba 1 para hacerlo')
        return ""
    while valor <= 2:
        try:
            print('escoja el vector ', valor)
            mostrar_vectores()
            seleccion.append(input())
            valor +=1
        except:
            print('No se encontro ningun vector, Ingrese un vector correcto')
    print('el vector ', seleccion[0] ,' es ',f.comparar(vectores[seleccion[0]],vectores[seleccion[1]]), ' que el vector ' , seleccion[1] )

def op_norma():
    valor = 1
    seleccion= []
    if(len (vectores) <1 ):
        print ('Debe haber ingresado por lo menos un vector, Escriba 1 para hacerlo')
        return None
    while valor <= 1:
        try:
            print('escoja el vector ', valor)
            mostrar_vectores()
            seleccion.append(input())
            valor += 1
        except:
            print('No se encontro ningun vector, Ingrese un vector correcto')

    print('La norma del vector es ',f.norma(vectores[seleccion[0]]))


def principal():

    Mensaje = '''\n \n Selecciones una ocpion:
    0. Salir
    1. Ingresar vector
    2. Mostrar Vectores
    3. Producto escalar
    4. Sumar vectores
    5. Producto punto
    6. Mayor elemento
    7. Menor elemento
    8. Promedio
    9. Norma
    10.Comparar
    '''

    while True:
        opcion = input(Mensaje)

        if opcion == '0':
            print('Gracias')
            break
        elif opcion == '1':
            vector = ingresar_vector()
            vectores[vector[0]] = vector[1:]
            print('Su vector', vector[0], 'es', vectores[vector[0]])
        elif opcion == '2':
            mostrar_vectores()
        elif opcion == '3':
            op_producto_escalar()
        elif opcion == '4':
            op_suma_vectores()
        elif opcion == '5':
            op_producto_punto()
        elif opcion == '6':
            op_mayor_elemento()
        elif opcion == '7':
            op_menor_elemento()
        elif opcion == '8':
            op_promedio()
        elif opcion == '9':
            op_norma()
        elif opcion == '10':
            op_comparar()
        else:
            print("Seleccione una opcion valida")

if __name__ == '__main__':
    principal()