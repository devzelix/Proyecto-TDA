from modulo_historial_navegacion.historial_navegacion import HistorialNavegacion

class Pestagna:

    def __init__(self, direccion):

        self.__historial_navegacion = HistorialNavegacion(direccion)
        if not self.__historial_navegacion.comprobar_direccion(direccion):

            return None

        else:

            self.__historial_navegacion.guardar_historial(self.__historial_navegacion.obtener_direccion())

    def interpretar_comando(self, comando):

        comando = comando.split(" ")
        if comando[0] == "ir":

            try:

                self.__historial_navegacion.ir(comando[1])

            except IndexError:

                print("Ingrese correctamente el comando.")

        elif comando[0] == "atras":

            self.__historial_navegacion.retroceder()

        elif comando[0] == "adelante":

            self.__historial_navegacion.avanzar()

        elif comando[0] == "mostrar_historial":

            self.__historial_navegacion.mostrar_historial()

        else:

            print("Comando inválido.")

    def obtener_direccion(self):

        return self.__historial_navegacion.obtener_direccion()