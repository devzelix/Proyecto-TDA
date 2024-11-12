from modulo_historial_navegacion.historial_navegacion import HistorialNavegacion

class Pestagna:

    def __init__(self, direccion):

        self.__historial_navegacion = HistorialNavegacion(direccion)
        if not self.__historial_navegacion.comprobar_direccion(direccion):

            return None

        else:

            print("Abriste una nueva pestagna con: " + self.__historial_navegacion.obtener_direccion())
            self.__historial_navegacion.guardar_historial(self.__historial_navegacion.obtener_direccion())

    def interpretar_comando(self, comando:str):

        comando = comando.split(" ")
        if comando[0] == "ir":

            self.__historial_navegacion.ir(comando[1])

        elif comando[0] == "atras":

            self.__historial_navegacion.retroceder()

        elif comando[0] == "adelante":

            self.__historial_navegacion.avanzar()

        else:

            print("Comando inválido.")

    def obtener_direccion(self):

        return self.__historial_navegacion.obtener_direccion()