import json
import os

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
        if data:
            with open(self.archivo_guardado, "r", encoding="utf-8") as archivo:
                partidas_guardadas = json.load(archivo)
            
            partidas_guardadas[f"slot_{slot}"] = data
            # Posibilidad de guardar la fecha con "datetime"

            with open(self.archivo_guardado, "w", encoding="utf-8") as archivo:
                json.dump(partidas_guardadas, archivo, indent=4)


    def cargar_partida(self, slot: int):
        with open(self.archivo_guardado, "r", encoding="utf-8") as archivo:
            partidas_jugadas = json.load(archivo)
        
        data = partidas_jugadas[f"slot_{slot}"]

        return data


    def borrar_partida(self, slot: int):
        with open(self.archivo_guardado, "r", encoding="utf-8") as archivo:
            partidas_guardadas = json.load(archivo)
        
        partidas_guardadas[f"slot_{slot}"] = None

        with open(self.archivo_guardado, "w", encoding="utf-8") as archivo:
            json.dump(partidas_guardadas, archivo, indent=4)