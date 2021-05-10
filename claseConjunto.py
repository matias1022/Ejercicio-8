

class Conjunto:
    __lista=[]

    def __init__(self):
        self.__lista = []

    def agregaNumero(self,numero):
        if type(numero) == int:
            if numero not in self.__lista:
                self.__lista.append(numero)

    def getLongitudConjunto(self):
        return len(self.__lista)

    def getNumero(self,indice):
        return self.__lista[indice]

    def getConjunto(self):
        return self.__lista

    def ordenaConjunto(self):
        return self.__lista.sort()

    def __add__ (self, unConjunto):
        aux=Conjunto()
        if type(aux) == type(unConjunto):
                nuevoConjunto = Conjunto()
                for i in range(len(self.__lista)+unConjunto.getLongitudConjunto()):
                    if i<len(self.__lista):
                        nuevoConjunto.agregaNumero(self.__lista[i])
                    else:
                        nuevoConjunto.agregaNumero(unConjunto.getNumero(i-len(self.__lista)))
                return nuevoConjunto

    def __sub__(self, unConjunto):
        aux=Conjunto()
        if type(aux) == type(unConjunto):
                nuevoConjunto = Conjunto()
                for i in range(len(self.__lista)):
                    if self.__lista[i] not in unConjunto.getConjunto():
                        nuevoConjunto.agregaNumero(self.__lista[i])
                return nuevoConjunto

    def __eq__(self, unConjunto):
        aux=Conjunto()
        if type(aux) == type(unConjunto):
            if len(self.__lista) == unConjunto.getLongitudConjunto():
                i=0
                iguales = True
                while ((i<len(self.__lista)) and (iguales == True)):
                    if unConjunto.getNumero(i) not in self.__lista:
                        iguales = False
                    i+=1
                return iguales
    
    def __str__(self):
        s='{'
        long = len(self.__lista)
        for i in range(long):
            numero = self.__lista[i]
            if i == long-1:
                s += str(numero)
            else:
                s += str(numero) + ','
        s+='}'
        return s