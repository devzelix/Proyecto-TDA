from modulo_gestion_descargas.gestion_descargas import GestionDescargas
from modulo_pestagnas_abiertas.pestagnas_abiertas import PestagnasAbiertas
from modulo_visualizacion_paginas.visualizacion import visualizar, listar_paginas
class NavegadorWeb:

    def __init__(self):

        self.__descargas = GestionDescargas()
        self.__pestagnas = PestagnasAbiertas()

    def interpretar_comandos(self):

        print("Bienvenido al simulador de Navegador Web en Consola.")
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

            elif instruccion == "ayuda":

                print("Lista de Comandos:")
                print("\n- ir <url o ip> (Te dirigira a la direccion indicada en la misma pestagna)")
                print("- atras (Te redirige a la direccion anterior de la pestagna)")
                print("- adelante (te redirige a la direccion siguiente de la pestagna)")
                print("- mostrar_historial (te muestra el historial de navegacion completo)")
                print("- nueva_pestagna <url o ip> (Te crea una nueva pestagna con la direccion indicada)")
                print("- cerrar_pestagna (Te cierra la pestagna actual)")
                print("- cambiar_pestagna <n> (Te cambia a la pestagna que corresponda al numero indicado)")
                print("- mostrar_pestagnas (Te muestra todas las pestagnas abiertas)")
                print("- descargar <url> (Te agnade a la cola de descarga el archivo de la url indicada)")
                print("- mostrar_descargas (Te muestra todas las descargas que estan pendientes)")
                print("- listar_paginas (Te muestra el url de todas las paginas disponibles)")
                print("- mostrar_contenido <modalidad> (Te muestra el contenido de la pagina cual te encuentras ya sea en 'basico' o 'texto_plano')")
                print("- salir (Cierra el navegador)")

            elif instruccion == "salir":

                print("Cerrando el navegador. ¡Hasta la próxima!")
                self.__descargas.guardar_descargas()
                break

            else:

                self.__pestagnas.interpretar_comando(comando)