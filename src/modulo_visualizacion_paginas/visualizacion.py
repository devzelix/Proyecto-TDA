from bs4 import BeautifulSoup
import csv

def comprobar_direccion(direccion):

    with open("assets/files/host/host.csv", newline="") as archivo:

        lector = csv.reader(archivo, delimiter=",")
        datos = list(lector)
        datos.pop(0)
        for fila in datos:

            for columna in fila:

                if columna == direccion:

                    return fila[2]

        return None

def obtener_ruta(direccion):

    with open("assets/files/host/host.csv", newline="") as archivo:

        lector = csv.reader(archivo, delimiter=",")
        datos = list(lector)
        for fila in datos:

            for columna in fila:

                if columna == direccion:

                    return fila[0]

        return None

def visualizar(direccion, modalidad):

    if comprobar_direccion(direccion):

        ruta = obtener_ruta(direccion)

        with open(ruta, "r", encoding="utf-8") as archivo:

            content = archivo.read()

        if modalidad == "basico":

            print(content)

        elif modalidad == "texto_plano":

            bs = BeautifulSoup(content, "html.parser")
            text = bs.get_text()
            print(text)

        else:

            print("Modalidad inválida.")

    else:

        print("Dirección inválida.")

def listar_paginas():

    with open("assets/files/host/host.csv", "r", newline="") as archivo:

        lector = csv.reader(archivo)
        datos = list(lector)
        datos.pop(0)
        print("Páginas Web Disponibles:\n")
        for sitio in datos:

            print("- " + sitio[2])