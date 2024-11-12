class Nodo:

    def __init__(self, valor, anterior):

        self.__valor = valor
        self.__anterior = anterior
        self.__siguiente = None

    def obtener_valor(self):

        return self.__valor

    def obtener_anterior(self):

        return self.__anterior

    def obtener_siguiente(self):

        return self.__siguiente

    def establecer_valor(self, valor):

        self.__valor = valor

    def establecer_anterior(self, anterior):

        self.__anterior = anterior

    def establecer_siguiente(self, siguiente):

        self.__siguiente = siguiente