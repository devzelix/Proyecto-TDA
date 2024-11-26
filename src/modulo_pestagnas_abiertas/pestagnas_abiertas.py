from modulo_pestagnas_abiertas.pestagna import Pestagna
from modulo_pestagnas_abiertas.lista_doble_enlazada import ListaDobleEnlazada

class PestagnasAbiertas:

    def __init__(self):

        self.__pestagnas = ListaDobleEnlazada()
        self.__pestagnas.agregar_nodo(Pestagna("www.inicio.com"))
        self.__pestagna_actual = self.__pestagnas.obtener_nodo_actual().obtener_valor()

    def abrir_pestagna(self, direccion):

        pestagna = Pestagna(direccion)
        if pestagna:

            self.__pestagnas.agregar_nodo(pestagna)
            self.__pestagna_actual = self.__pestagnas.obtener_nodo_actual().obtener_valor()
            print("Abriste una nueva pestagna con: " + self.__pestagna_actual.obtener_direccion())

    def cerrar_pestagna(self):

        print("Cerrando la pestagna con: " + self.__pestagna_actual.obtener_direccion())
        if self.__pestagnas.eliminar_nodo():

            self.__pestagna_actual = self.__pestagnas.obtener_nodo_actual().obtener_valor()
            print("Ahora estas en la pestagna con: " + self.__pestagna_actual.obtener_direccion())
            return True

        else:

            return False

    def cambiar_pestagna(self, numero):

        if self.__pestagnas.obtener_nodo(numero):

            self.__pestagna_actual = self.__pestagnas.obtener_nodo_actual().obtener_valor()
            print("Ahora estas en la pestagna con: " + self.__pestagna_actual.obtener_direccion())

        else:

            print("Pestagna no encontrada.")

    def mostrar_pestagnas(self):

        print("Pestagnas abiertas:\n")
        pestagnas = self.__pestagnas.obtener_elementos()
        for i in range(len(pestagnas)):

            print(str(i + 1) + ". " + pestagnas[i].obtener_direccion())

    def obtener_direccion_pestagna_actual(self):

        return self.__pestagna_actual.obtener_direccion()

    def interpretar_comando(self, comando):

        self.__pestagna_actual.interpretar_comando(comando)