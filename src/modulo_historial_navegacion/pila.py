from modulo_historial_navegacion.nodo import Nodo

class Pila:

    def __init__(self):

        self.__ultimo = None

    def apilar(self, valor):

        if self.__ultimo:

            self.__ultimo = Nodo(valor, self.__ultimo)

        else:

            self.__ultimo = Nodo(valor, None)

    def desapilar(self):

        if self.__ultimo:

            self.__ultimo = self.__ultimo.obtener_anterior()

    def obtener_ultimo(self):

        return self.__ultimo