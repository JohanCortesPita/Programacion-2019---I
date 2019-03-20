from unittest import TestCase

import EjerciciosIfConditionals as c

class TestMensaje_negativo(TestCase):
    def test_mensaje_negativo(self):
        self.assertEqual(c.mensaje_negativo(-10), 'El numero es negativo')
        self.assertEqual(c.mensaje_negativo(1), 'El numero es positivo')

class Testcompara_edades(TestCase):
    def test_compara_edades(self):
        self.assertEqual(c.compara_edades(10, 20), 'El primero es mas joven')
        self.assertEqual(c.compara_edades(89, 56), 'El segundo es mas joven')
        self.assertEqual(c.compara_edades(3, 3), 'Tienen la misma edad')

class Testes_parentesis(TestCase):
    def test_es_parentesis(self):
        self.assertEqual(c.es_parentesis('('), 'Es parentesis')
        self.assertEqual(c.es_parentesis('x'), 'No es parentesis')
        self.assertRaises(TypeError, c.es_parentesis, 'No es un parentesis')

class Testdividir(TestCase):
    def test_dividir(self):
        self.assertEqual(c.dividir(6, 2), 3.0)
        self.assertRaises(TypeError, c.dividir, 'No dividiras por 0')

class Testdoble_impar(TestCase):
    def test_dobleimpar(self):
        self.assertEqual(c.doble_impar(14), 'El doble del numero es un numero impar')
        self.assertEqual(c.doble_impar(12), 'El doble del numero no es un numero impar')
        self.assertRaises(TypeError, c.doble_impar, 'no es un numero o es un float')

class Testcomparar_cuadrado(TestCase):
    def test_comparar_cuadrado(self):
        self.assertEqual(c.comparar_cuadrado(2, 4), 'El segundo es el cuadrado del primero')
        self.assertEqual(c.comparar_cuadrado(2, 3), 'El segundo es menor que el cuadrado del primero')
        self.assertRaises(TypeError, c.comparar_cuadrado, 'Alguno de los datos ingresados no es un numero')

class Testnumero_primo(TestCase):
    def test_numero_primo(self):
        self.assertRaises(TypeError, c.numero_primo, 's')
        self.assertEqual(c.numero_primo(2), 'es un numero primo')
        self.assertEqual(c.numero_primo(4), 'no es un numero primo')







