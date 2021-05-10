

from claseConjunto import Conjunto

from claseMenuOpciones import MenuOpciones


def test():
    Conjunto1 = Conjunto()
    Conjunto2 = Conjunto()
    Conjunto3 = Conjunto()
    Conjunto4 = Conjunto()
    Conjunto1.agregaNumero(1)
    Conjunto1.agregaNumero(2)
    Conjunto2.agregaNumero('A')
    Conjunto3.agregaNumero('+')
    Conjunto4.agregaNumero(1)
    Conjunto4.agregaNumero(2)
    Conjunto4.agregaNumero('F')
    print ('Test: ')
    print (Conjunto1)
    print (Conjunto2)
    print (Conjunto3)
    print (Conjunto4)
    input ('Presiona ENTER para continuar...')


if __name__ == '__main__':
    unMenu = MenuOpciones()
    test()
    unMenu.menuOpciones()