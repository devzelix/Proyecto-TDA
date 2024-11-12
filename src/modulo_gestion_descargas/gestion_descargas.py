from modulo_gestion_descargas.cola import Cola
import csv
from datetime import datetime
import os

class GestionDescargas:

    def __init__(self):

        self.__descargas = Cola()

    def comprobar_direccion(self, direccion):

        with open("assets/files/host/host.csv", newline="") as archivo:

            lector = csv.reader(archivo, delimiter=",")
            datos = list(lector)
            datos.pop(0)
            for fila in datos:

                for columna in fila:

                    if columna == direccion:

                        return fila[2]

            return None

    def obtener_ruta(self, direccion):

        with open("assets/files/host/host.csv", newline="") as archivo:

            lector = csv.reader(archivo, delimiter=",")
            datos = list(lector)
            for fila in datos:

                for columna in fila:

                    if columna == direccion:

                        return fila[0]

            return None

    def descargar(self, direccion):

        direccion = self.comprobar_direccion(direccion)
        if direccion:

            print("Iniciando descarga de: " + direccion)
            self.__descargas.encolar(direccion)

        else:

            print("Archivo no encontrado.")

    def mostrar_descargas(self):

        cola_aux = Cola()
        contador = 0
        descarga = self.__descargas.desencolar()
        while descarga:

            if contador == 0:

                print("Cola de descargas:\n")

            contador += 1
            print(str(contador) + ". " + descarga)
            cola_aux.encolar(descarga)
            descarga = self.__descargas.desencolar()

        if contador == 0:

            print("La cola de descarga esta vacía.")

        else:

            self.__descargas = cola_aux

    def cancelar_descarga(self, numero):

        cola_aux = Cola()
        contador = 0
        descarga = self.__descargas.desencolar()
        descarga_cancelada = ""
        while descarga:

            contador += 1
            if contador == numero:

                descarga_cancelada = descarga

            else:

                cola_aux.encolar(descarga)

            descarga = self.__descargas.desencolar()

        if contador == 0:

            print("La cola de descarga esta vacía.")

        else:

            if descarga_cancelada != "":

                print("Descarga cancelada: " + descarga_cancelada)

            else:

                print("Descarga no encontrada.")

            self.__descargas = cola_aux

    def guardar_descargas(self):

        datos = None
        with open("assets/files/descargas.csv", newline="") as archivo:

            lector = csv.reader(archivo, delimiter=",")
            datos = list(lector)

        with open("assets/files/descargas.csv", "w", newline="") as archivo:

            escritor = csv.writer(archivo, delimiter=",")
            if datos:

                descarga = self.__descargas.desencolar()
                while descarga:

                    tiempo = datetime.now()
                    fecha = str(tiempo.day)
                    while len(fecha) < 2:

                        fecha = "0" + fecha

                    fecha += "/" + str(tiempo.month)
                    while len(fecha) < 5:

                        fecha = fecha[0:3] + "0" + fecha[3]

                    fecha += "/" + str(tiempo.year)

                    tamagno = (os.path.getsize(self.obtener_ruta(descarga))) / 1024

                    datos.append([descarga, f"{tamagno:.2f}", fecha])
                    descarga = self.__descargas.desencolar()

                escritor.writerows(datos)