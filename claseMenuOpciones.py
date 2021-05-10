
import os

from claseConjunto import Conjunto

class MenuOpciones:
    UNIR = 1
    DIFERENCIA = 2
    IGUALDAD = 3
    SALIR = 0
    __opc=""
    def __init__(self,opc=0):
        self.__opc=opc
    def menuOpciones (self):
        continuar = True
        while continuar:
            os.system ('cls')
            print (f''' Menú de opciones:
              {self.UNIR}) Unir dos conjuntos.
              {self.DIFERENCIA}) Diferencia de dos conjuntos.
              {self.IGUALDAD}) Verificar si dos conjuntos son iguales.
              {self.SALIR}) Salir.
''')
            opc = input ('Ingrese una opción: ')
            if opc.isdigit():
                self.__opc = int (opc)
                os.system ('cls')
                if self.__opc == self.UNIR:
                    print ('            UNIÓN DE DOS CONJUNTOS.')
                    conjunto1 = Conjunto()
                    conjunto2 = Conjunto()
                    cantidad = input ('Ingrese la cantidad de números del Primer Conjunto: ')
                    if cantidad.isdigit():
                        cantidad = int (cantidad)
                        for i in range (cantidad):
                            numero = input (f'{i+1}° Número: ')
                            if numero.isdigit():
                                numero = int (numero)
                                conjunto1.agregaNumero(numero)
                    cantidad = input ('Ingrese la cantidad de números del Segundo Conjunto: ')
                    if cantidad.isdigit():
                        cantidad = int (cantidad)
                        for i in range (cantidad):
                            numero = input (f'{i+1}° Número: ')
                            if numero.isdigit():
                                numero = int (numero)
                                conjunto2.agregaNumero(numero)
                    suma = conjunto1 + conjunto2
                    suma.ordenaConjunto()
                    print (f'{conjunto1} U {conjunto2} = {suma}.')                    
                elif self.__opc == self.DIFERENCIA:
                    print ('            DIFERENCIA ENTRE DOS CONJUNTOS.')
                    conjunto1 = Conjunto()
                    conjunto2 = Conjunto()
                    cantidad = input ('Ingrese la cantidad de números del Primer Conjunto: ')
                    if cantidad.isdigit():
                        cantidad = int (cantidad)
                        for i in range (cantidad):
                            numero = input (f'{i+1}° Número: ')
                            if numero.isdigit():
                                numero = int (numero)
                                conjunto1.agregaNumero(numero)
                    cantidad = input ('Ingrese la cantidad de números del Segundo Conjunto: ')
                    if cantidad.isdigit():
                        cantidad = int (cantidad)
                        for i in range (cantidad):
                            numero = input (f'{i+1}° Número: ')
                            if numero.isdigit():
                                numero = int (numero)
                                conjunto2.agregaNumero(numero)
                    resta = conjunto1 - conjunto2
                    resta.ordenaConjunto()
                    print (f'{conjunto1} ∩ {conjunto2} = {resta}.')
                elif self.__opc == self.IGUALDAD:
                    print ('            IGUALDAD ENTRE DOS CONJUNTOS.')
                    conjunto1 = Conjunto()
                    conjunto2 = Conjunto()
                    cantidad = input ('Ingrese la cantidad de números del Primer Conjunto: ')
                    if cantidad.isdigit():
                        cantidad = int (cantidad)
                        for i in range (cantidad):
                            numero = input (f'{i+1}° Número: ')
                            if numero.isdigit():
                                numero = int (numero)
                                conjunto1.agregaNumero(numero)
                    cantidad = input ('Ingrese la cantidad de números del Segundo Conjunto: ')
                    if cantidad.isdigit():
                        cantidad = int (cantidad)
                        for i in range (cantidad):
                            numero = input (f'{i+1}° Número: ')
                            if numero.isdigit():
                                numero = int (numero)
                                conjunto2.agregaNumero(numero)
                    if conjunto1 == conjunto2:
                        print (f'{conjunto1} = {conjunto2}.')
                    else:
                        print (f'{conjunto1} != {conjunto2}.')
                elif self.__opc == self.SALIR:
                    continuar = False
                else:
                    print ('Opción no válida.')
                input ('Presiona ENTER para continuar...')
            else:
                print ('Opción no válida.')
                input ('Presiona ENTER para continuar...')
        print ("Saliendo del Programa")