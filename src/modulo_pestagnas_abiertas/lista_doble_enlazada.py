from modulo_pestagnas_abiertas.nodo import Nodo

class ListaDobleEnlazada:

    def __init__(self):

        self.__cabeza = None
        self.__nodo_actual = None

    def agregar_nodo(self, valor):

        if self.__cabeza:

            actual = self.__cabeza
            while actual.obtener_siguiente():

                actual = actual.obtener_siguiente()

            nodo = Nodo(valor, actual)
            actual.establecer_siguiente(nodo)
            self.__nodo_actual = nodo

        else:

            self.__cabeza = Nodo(valor, None)
            self.__nodo_actual = self.__cabeza

    def obtener_nodo(self, numero):

        if numero >= 1:

            actual = self.__cabeza
            contador = 1
            while actual:

                if contador == numero:

                    self.__nodo_actual = actual
                    return True

                actual = actual.obtener_siguiente()
                contador += 1 

        else:

            return False

    def eliminar_nodo(self):

        if self.__nodo_actual == self.__cabeza:

            self.__cabeza = self.__cabeza.obtener_siguiente()
            self.__cabeza.establecer_anterior(None)
            self.__nodo_actual = self.__cabeza

        else:

            actual = self.__cabeza.obtener_siguiente()
            while actual:

                if actual == self.__nodo_actual:

                    anterior = actual.obtener_anterior()
                    siguiente = actual.obtener_siguiente()
                    anterior.establecer_siguiente(siguiente)
                    siguiente.establecer_anterior(anterior)
                    self.__nodo_actual = siguiente
                    break

                actual = actual.obtener_siguiente()

    def obtener_elementos(self):

        elementos = []
        actual = self.__cabeza
        while actual:

            elementos.append(actual.obtener_valor())
            actual = actual.obtener_siguiente()

        return elementos

    def obtener_nodo_actual(self):

        return self.__nodo_actual