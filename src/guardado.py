import json
import os
from datetime import datetime
from src._utilidades import *


class Guardado:
    """
    Clase Guardado: sirve para guardar los datos de partida.

        Inicializacion de atributos:
        - El atributo archivo guardado sirve para guardar la partida en curso.
        - La funcion inicializar archivo guardado sirve para guardar la partida en la nube, hay tres espacios disponibles.
        - Hay funciones donde, puedes borrar la partida guardada, que se muestre los datos de la partida guardada, y para cargar
        la partida nuevamente.
    """

    def __init__(self):
        self.archivo_guardado = "partidas_guardadas.json"
        self.inicializar_archivo_guardado()

    def inicializar_archivo_guardado(self):
        if not os.path.exists(self.archivo_guardado):
            data = {"slot_1": None, "slot_2": None, "slot_3": None}
            with open(self.archivo_guardado, "w", encoding="utf-8") as archivo:
                json.dump(data, archivo, indent=4)

    def guardar_partida(self, slot: int, data):
        clave_slot = self._validar_slot(slot)
        if data:
            with open(self.archivo_guardado, "r", encoding="utf-8") as archivo:
                partidas_guardadas = json.load(archivo)

            data["fecha"] = datetime.now().strftime("%d.%m.%y   %H:%M")
            partidas_guardadas[clave_slot] = data

            with open(self.archivo_guardado, "w", encoding="utf-8") as archivo:
                json.dump(partidas_guardadas, archivo, indent=4)

    def cargar_partida(self, slot: int):
        clave_slot = self._validar_slot(slot)
        with open(self.archivo_guardado, "r", encoding="utf-8") as archivo:
            partidas_jugadas = json.load(archivo)

        data = partidas_jugadas[clave_slot]

        return data

    def borrar_partida(self, slot: int):
        clave_slot = self._validar_slot(slot)
        with open(self.archivo_guardado, "r", encoding="utf-8") as archivo:
            partidas_guardadas = json.load(archivo)

        partidas_guardadas[clave_slot] = None

        with open(self.archivo_guardado, "w", encoding="utf-8") as archivo:
            json.dump(partidas_guardadas, archivo, indent=4)

    def _validar_slot(self, slot):
        if slot not in (1, 2, 3):
            raise ValueError("El número de slot debe ser 1, 2 o 3.")
        return f"slot_{slot}"

    def mostrar_info_slots(self, screen):
        x = 305
        gris = (220, 220, 220)
        for slot in range(1, 4):
            datos = self.cargar_partida(slot)
            mostrar_texto(
                screen,
                f"Guardado {slot}",
                x - 5,
                170,
                30,
            )
            y = 215

            if datos:
                textos = [
                    f"{datos["fecha"]}",
                    f"Nivel: {datos["nivel"]}",
                    f"Dinero: {datos["dinero"]}",
                    f"Puntos: {datos["puntos"]}",
                    f"Objetivo: {datos["puntos_nivel"]}",
                ]
                for texto in textos:
                    mostrar_texto(screen, texto, x, y, 20, gris)
                    y += 30
                if datos["comodines"]:
                    mostrar_texto(screen, "Comodines:", x, y, 20, gris)
                    x_copy = x - 5
                    y += 28
                    for n, comodin in enumerate(datos["comodines"], start=1):
                        mostrar_texto(screen, comodin, x_copy, y, 15, gris)
                        y += 20
                        if n == 3:
                            x_copy += 100
                            y -= 60
                else:
                    mostrar_texto(screen, "Comodines: cero", x, y, 20, gris)

            else:
                mostrar_texto(screen, "Vacio", x, 215, 20, gris)
            x += 250
