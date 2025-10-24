# Para guardar y cargar partidas

import json
import os


def inicializar_archivo():
    if not os.path.exists("partidas_guardadas.json"):
        data = {"slot_1": None, "slot_2": None, "slot_3": None}
        with open("partidas_guardadas.json", "w") as archivo:
                json.dump(data, archivo)


def guardar_partida(slot: int, data):
    inicializar_archivo()
    
    if data:
        with open("partidas_guardadas.json", "r") as archivo:
            partidas_guardadas = json.load(archivo)
        
        partidas_guardadas[f"slot_{slot}"] = data
        # Posibilidad de guardar la fecha con "datetime"

        with open("partidas_guardadas.json", "w") as archivo:
            json.dump(partidas_guardadas, archivo)


def cargar_partida(slot: int):
    with open("partidas_guardadas.json", "r") as archivo:
        partidas_jugadas = json.load(archivo)
    
    data = partidas_jugadas[f"slot_{slot}"]

    return data


def borrar_partida(slot: int):
    with open("partidas_guardadas.json", "r") as archivo:
        partidas_guardadas = json.load(archivo)
    
    partidas_guardadas[f"slot_{slot}"] = None

    with open("partidas_guardadas.json", "w") as archivo:
        json.dump(partidas_guardadas, archivo)