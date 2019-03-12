from unittest import TestCase
import condicionales as c

class Test_ejercicios(TestCase):
    def test_ejrcicios(self):
        #Ejercicio 1 y 2
        self.assertRaises(TypeError, c.numero_negativo, 'c')
        self.assertEqual(c.numero_negativo(-1), 'el numero es negativo')
        self.assertEqual(c.numero_negativo(1), 'el numero es positivo')
        #Ejercicio 3
        self.assertRaises(TypeError,c.quien_es_mayor,'s','c')
        self.assertEqual(c.quien_es_mayor(3,5),'El mayor es el segundo')
        self.assertEqual(c.quien_es_mayor(5,4),'El mayor es el primero')
        self.assertRaises(TypeError, c.par_o_impar, 's')
        #Ejercicio 4
        self.assertRaises(TypeError,c.parentesis,'asd')
        self.assertEqual(c.parentesis('('),'El caracter es un parentesis')
        self.assertEqual(c.parentesis('x'),'El caracter no es un parentesis')
        #Ejercicio 5
        self.assertRaises(TypeError,c.par_o_impar,'xxx')
        self.assertEqual(c.par_o_impar(2),'el numero es par')
        self.assertEqual(c.par_o_impar(1),'el numero es impar')
        #Ejercicio 6
        self.assertRaises(TypeError,c.el_doble_impar,'x')
        self.assertEqual(c.el_doble_impar(4),'El numero 4 es el doble de 2.0, que es par')
        self.assertEqual(c.el_doble_impar(10),'El numero 10 es el doble de 5.0, que es impar')
        #Ejercicio 7
        self.assertRaises(TypeError,c.cuadrado_del_primero,'x','y')
        self.assertEqual(c.cuadrado_del_primero(4,16),'El segundo es el cuadrado del primero.')
        self.assertEqual(c.cuadrado_del_primero(10,20),'El segundo es menor que el cuadrado del primero.')

        #Ejercicio 8
        self.assertRaises(TypeError,c.numero_primo,'ddd')
        self.assertEqual(c.numero_primo(13),'es un numero primo')
        self.assertEqual(c.numero_primo(1872),'no es un numero primo')
