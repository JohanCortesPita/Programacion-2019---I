from Funciones import ingresar_vector
from uso_archivos import *
import funciones_matrices as f

RUTA_MATRICES = 'mis_matrices.json'
matrices = leer(RUTA_MATRICES)

def leer_matriz():
    """
    Lee una matriz por teclado
    :return: (list of list of int) la matriz del usuario
    """
    resultado = []
    while True:
        entrada = input('Desea ingresar una fila? s/n ')
        if entrada == 'n':
            break
        resultado.append(ingresar_vector())
    return resultado


def mostrar_matrices():
    for fila in matrices:
        print('Contiene', matrices[fila])

def op_producto_matrices():
    valor = 1
    seleccion = []
    if (len(matrices) < 2):
        print('Debe haber ingresado al menos dos matrices para realizar la comparación')
        return ""
    while valor <= 2:
        try:
            print('Escoja la matriz', valor)
            mostrar_matrices()
            seleccion.append(input())
            valor += 1
        except:
            print('No se encontro ninguna matriz, Ingrese una matriz correcta')
    print('El producto de las matrices es ', f.producto_matrices(matrices[seleccion[0], matrices[seleccion[1]]] ))

def principal():
    """
    Funcion principal del menu

    :return: none
    """
    while True:

        MENU = """
        **********Menu**********
        0. Salir
        1. Ingresar Matriz
        2. Ver Matrices
        3. Suma Vectores
        4. Producto Punto
        ************************
        """

        seleccion = input(MENU)
        if seleccion == '0':
            print('Suerte')
            break
        elif seleccion == "1":
            nombre = input('cual es el nombre de su matriz ')
            matriz = leer_matriz()
            matrices[nombre] = matriz
        elif seleccion == "2":
            print('Sus matrices')
            for matriz in matrices:
                print(matriz, "=")
                print(matrices[matriz])
        elif seleccion == '4':
            op_producto_matrices()
    else:
            print("Seleccion invalida")


    if guardar(RUTA_MATRICES, matrices):
        print('Se guardaron exitosamente sus matrices')
    else:
        print('No se han podido guardar las matrices')


if __name__ == '__main__':
    principal()

