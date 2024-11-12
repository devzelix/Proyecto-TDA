class Nodo:

    def __init__(self, valor, anterior):

        self.__valor = valor
        self.__anterior = anterior

    def obtener_valor(self):

        return self.__valor

    def obtener_anterior(self):

        return self.__anterior

    def modificar_anterior(self, anterior):

        self.__anterior = anterior