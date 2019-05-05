from While2 import producto_punto as pp

# def suma_matrices(matriz1,matriz2):
#     """
#     "Funcioòn que suma dos matrices"
#
#     (list of list of int) -> list of num
#
#     >>> suma_matrices([[1,2,3],[2,3,3],[2,2,3]],[[3,2,1],[3,2,1],[3,2,1]])
#     [[4,4,4],[5,5,4],[5,4,4]]
#
#     >>> suma_matrices([[1,2,3]],[[3,2,1]])
#     [[4,4,4]]
#
#     :param matriz1: Matriz1 ingresada
#     :param matriz2: Matriz2 ingresada
#     :return: Suma de matrices
#     """
#     filas = int(input("Introduzca el numero de filas de sus matrices: "))
#     columnas = int(input("Introduzca el numero de columnas de sus matrices: "))
#
#     matriz1 = []
#     matriz2 = []
#     matriz3 = []
#
#     for i in range (filas):
#         matriz1.append([0] * columnas)
#         matriz2.append([0] * columnas)
#
#     print("Ingrese su matriz 1")
#
#     for i in range(filas):
#         for j in range(columnas):
#             matriz1[i][j] = float(input('Elemento (%d,%d): ' % (i, j)))
#
#     print('Ingrese su matriz 2')
#
#     for i in range(filas):
#         for j in range(columnas):
#             matriz2[i][j] = float(input('Elemento (%d,%d): ' %(i, j)))
#
#     for i in range(filas):
#         for j in range(columnas):
#             matriz3[i][j] += matriz1[i][j] + matriz2[i][j]
#
#     print('Su matriz resultante es \n' + matriz3)

# vector = [1, 2, 8, 9]
#
# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

def vector_columna(matrix, indice):
    """
    (list of list of num, int) -> list of num

    Obtiene el vector columna para la matriz dada

    >>> vector_columna([[1,2,3], [4,5,6], [7,8,9]], 0)
    [1, 4, 7]

    >>> vector_columna([[1,2,3], [4,5,6], [7,8,9]], 2)
    [3, 6, 9]

    >>> vector_columna([[1,2,3], [4,5,6], [7,8,9]], 1)
    [2, 5, 8]

    :param matriz: la matriz para extraer
    :param indice: el indice del vector columna
    :return: el vector generado
    """
    resultado = []
    for i in range(0, len(matrix)):
        resultado.append(matrix[i][indice])
    return resultado

def producto_matrices(matriz_1, matriz_2):
    """
    (list of list of num, list of list of num) -> list of list of num

    Calcula el producto de dos matrices

    >>> producto_matrices([[1,2],[3,4]], [[1,2],[3,4]])
    [[7, 10], [15, 22]]

    :param matriz_a: La primer matriz
    :param matriz_b: La segunda Matriz
    :return: matriz_1 * matriz_2
    """
    matriz_resultante = []
    # Este for recorre las filas de A
    for i in range(0, len(matriz_1)):
        # Este for recorre las columnas de B
        vector_fila = []
        for j in range(0, len(matriz_1)):
            # print('Fila de a', matriz_1[i])
            # print('Columna de b', vector_columna(matriz_2, j))
            vector_fila.append(pp(matriz_1[i], vector_columna(matriz_2, j)))
        matriz_resultante.append(vector_fila)
    return matriz_resultante


# print(producto_matrices([[1, 2], [3, 4]], [[1, 2], [3, 4]]))