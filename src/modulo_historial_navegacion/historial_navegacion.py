from modulo_historial_navegacion.pila import Pila
from datetime import datetime
import csv

class HistorialNavegacion:

    def __init__(self, direccion_actual):

        self.__pila_atras = Pila()
        self.__pila_siguiente = Pila()
        self.__direccion_actual = self.comprobar_direccion(direccion_actual)

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

    def guardar_historial(self, direccion):

        datos = None
        with open("assets/files/historial_navegacion.csv", newline="") as archivo:

            lector = csv.reader(archivo, delimiter=",")
            datos = list(lector)

        with open("assets/files/historial_navegacion.csv", "w", newline="") as archivo:

            escritor = csv.writer(archivo, delimiter=",")
            if datos:

                tiempo = datetime.now()
                fecha = str(tiempo.day)
                while len(fecha) < 2:

                    fecha = "0" + fecha

                fecha += "/" + str(tiempo.month)
                while len(fecha) < 5:

                    fecha = fecha[0:3] + "0" + fecha[3]

                fecha += "/" + str(tiempo.year)
                hora = str(tiempo.hour)
                while len(hora) < 2:

                    hora = "0" + hora

                hora += ":" + str(tiempo.minute)
                while len(hora) < 5:

                    hora = hora[0:3] + "0" + hora[3]

                datos.append([direccion, fecha, hora])
                escritor.writerows(datos)

    def ir(self, direccion):

        direccion = self.comprobar_direccion(direccion)

        if direccion:

            if self.__direccion_actual:

                self.__pila_atras.apilar(self.__direccion_actual)

            self.__direccion_actual = direccion
            print("Visitando: " + direccion)
            self.guardar_historial(direccion)
            return True

        else:

            print("Dirección no encontrada.")
            return False

    def retroceder(self):

        if self.__pila_atras.obtener_ultimo():

            direccion = self.__pila_atras.obtener_ultimo().obtener_valor()
            print("Regresando a: " + direccion)
            self.__pila_atras.desapilar()
            self.__pila_siguiente.apilar(self.__direccion_actual)
            self.__direccion_actual = direccion
            self.guardar_historial(direccion)

        else:

            print("No se puede realizar esta acción.")

    def avanzar(self):

        if self.__pila_siguiente.obtener_ultimo():

            direccion = self.__pila_siguiente.obtener_ultimo().obtener_valor()
            print("Avanzando a: " + direccion)
            self.__pila_siguiente.desapilar()
            self.__pila_atras.apilar(self.__direccion_actual)
            self.__direccion_actual = direccion
            self.guardar_historial(direccion)

        else:

            print("No se puede realizar esta acción.")

    def mostrar_historial(self):

        with open("assets/files/historial_navegacion.csv", newline="") as archivo:

            lector = csv.reader(archivo, delimiter=",")
            historial = list(lector)
            if historial:

                if len(historial) > 2:

                    print("Historial de Navegación:\n")

                    for i in range(1, len(historial)):

                        print(str(i) + ". " + historial[i][0] + "   " + historial[i][1] + "   " + historial[i][2])

                else:

                    print("Historial de navegación vacío.")

    def obtener_direccion(self):

        return self.__direccion_actual