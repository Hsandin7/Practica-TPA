import json
import os
from datetime import datetime

class Guardado:
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