# ------------------------------
# Script: testingCrearemos.py
# Descripción: Prueba para el software contenido en mychar.py
# Autor: Laura Ramos Granados
# Fecha: 3 de noviembre de 2025
# ------------------------------

import unittest 
from mychar import cadena_mas_larga

class Test(unittest.TestCase):
    """
    Guía de prueba con unittest para la función cadena_mas_larga
    """
    
    # Bloque 1: Casos entradas normales    
    def test_lista_ejemplo_devuelve_abcd(self):
        """
        Caso 1: 
        Lista requerida, donde el argumento es una lista correcta, con dos elementos empatados con la longitud más alta. Se espera que elija el menor alfabéticamemnte
        """ 
        self.assertEqual(cadena_mas_larga(["a", "ab", "abc", "dddd", "abcd"]), "abcd")

    def test_desempate_misma_longitud_desempata_alfabetico_ignora_mayusculas(self):
        """
        Caso 2: 
        Lista donde todos los ítems son de la misma longitud. Se espera que elija el menor alfabéticamemnte y se demuestre que no importa la mayúscula
        """
        self.assertEqual(cadena_mas_larga(["boom", "meme", "Zzzz"]), "boom")
        self.assertEqual(cadena_mas_larga(["Baaa", "woof", "meow"]), "Baaa")

    def test_empate_total_misma_minusculas_conserva_primera(self):
        """
        Caso 3:
        Si dos cadenas empatan y su .lower() es el mismo, entonces debe mantenerse la primera
        """
        self.assertEqual(cadena_mas_larga(["Kafka", "kafka"]), "Kafka")        
        self.assertEqual(cadena_mas_larga(["chewbacca", "Chewbacca"]), "chewbacca")   

    def test_cadena_con_espacios_internos_cuenta_como_larga(self):
        """
        Caso 4:
        Los espacios internos cuentan
        """
        self.assertEqual(cadena_mas_larga(["hola mundo", "python rules", "otra"]), "python rules")

    def  test_espacios_laterales_no_cuentan_para_la_longitud(self):
        """
        Caso 5:
        Los espacios laterales no cuentan y no se devuelven en el resultado
        """
        self.assertEqual(cadena_mas_larga(["", "  ", "ah","  ooh  "]),"ooh")

    # Bloque 2: Casos lista vacía y elementos en blanco

    def test_lista_vacia_devuelve_cadena_vacia(self):
        """
        Caso 6:
        Si no hay elementos, devuelve cadena vacía
        """
        self.assertEqual(cadena_mas_larga([]), "")

    def test_todo_blanco_devuelve_vacia(self):
        """
        Caso 7:
        Si todos son espacios en blanco, devuelve cadena vacía
        """
        self.assertEqual(cadena_mas_larga(["   ", ""]), "")     

    # Bloque 3: Casos caracteres del español
    def test_unicode_acentos_virgula_y_dieresis(self):
        """
        Caso 8:
        Debe funcionar con acentos, ñ, diéresis. En el
        empate por longitud, igualmente gana el orden alfabético ignorando mayúsculas, Si empata con acentos, gana la sin tilde. Se repeta el orden unicode
        """
        self.assertEqual(cadena_mas_larga(["mañana", "camion", "acción", "pingüino"] ), "pingüino")
        self.assertEqual(cadena_mas_larga(["pingüin", "pingüín"]), "pingüin")


    # Bloque 4: Casos de mal uso
    def test_no_lista_dispara_typeerror(self):
        """
        Caso 9:
        Conforma el comportamiento cuando el argumento dado no es  tipo lista.Se espera que la función lance una excepción del tipo TypeError
        """    
        with self.assertRaises(TypeError):
            cadena_mas_larga("hola")
        with self.assertRaises(TypeError):
            cadena_mas_larga(("a", "b"))

    def test_elementos_no_str_dispara_valueerror(self):
        """
        Caso 10:
        Caso en que la lista contiene elementos que no son cadenas de texto.  La función debe lanzar una excepción ValueError
        """    
        with self.assertRaises(ValueError):
            cadena_mas_larga(["hola", 123, "adios"])
        with self.assertRaises(ValueError):
            cadena_mas_larga(["ok", None])