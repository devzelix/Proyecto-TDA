from modulo_gestion_descargas.gestion_descargas import GestionDescargas
from modulo_pestagnas_abiertas.pestagnas_abiertas import PestagnasAbiertas
from modulo_visualizacion_paginas.visualizacion import visualizar, listar_paginas
class NavegadorWeb:

    def __init__(self):

        self.__descargas = GestionDescargas()
        self.__pestagnas = PestagnasAbiertas()

    def interpretar_comandos(self):

        print("Bienvenido al simulador de Navegador Web en Consla.")
        print("Escribe un comando para comenzar. Usa 'ayuda' para ver la lista de comandos disponibles.")

        while True:

            comando = input("\n> ")
            instruccion = (comando.split(" "))[0]
            if instruccion == "descargar":

                try:

                    self.__descargas.descargar((comando.split(" "))[1])

                except IndexError:

                    print("Ingrese correctamente el comando.")

            elif instruccion == "mostrar_descargas":

                self.__descargas.mostrar_descargas()

            elif instruccion == "cancelar_descarga":

                try:

                    if (comando.split(" "))[1].isdigit():

                        self.__descargas.cancelar_descarga(int((comando.split(" "))[1]))

                    else:

                        print("Ingrese un número de descarga válido.")

                except IndexError:

                    print("Ingrese correctamente el comando.")

            elif instruccion == "nueva_pestagna":

                try:

                    self.__pestagnas.abrir_pestagna((comando.split(" "))[1])

                except IndexError:

                    print("Ingrese correctamente el comando.")

            elif instruccion == "cerrar_pestagna":

                if not self.__pestagnas.cerrar_pestagna():

                    print("Cerrando el navegador. ¡Hasta la próxima!")
                    self.__descargas.guardar_descargas()
                    break

            elif instruccion == "cambiar_pestagna":

                try:

                    if (comando.split(" "))[1].isdigit():

                        self.__pestagnas.cambiar_pestagna(int((comando.split(" "))[1]))

                    else:

                        print("Ingrese un número de pestagna válido.")

                except IndexError:

                    print("Ingrese correctamente el comando.")

            elif instruccion == "mostrar_pestagnas":

                self.__pestagnas.mostrar_pestagnas()

            elif instruccion == "mostrar_contenido":

                try:

                    visualizar(self.__pestagnas.obtener_direccion_pestagna_actual(), (comando.split(" "))[1])

                except IndexError:

                    print("Ingrese correctamente el comando.")

            elif instruccion == "listar_paginas":

                listar_paginas()

            elif instruccion == "salir":

                print("Cerrando el navegador. ¡Hasta la próxima!")
                self.__descargas.guardar_descargas()
                break

            else:

                self.__pestagnas.interpretar_comando(comando)