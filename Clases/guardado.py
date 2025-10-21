# Para guardar y cargar partidas

import json

def guardar_partida(data):
    if data:
        with open("partidas_guardadas.json", "w") as archivo:
            json.dump(data, archivo)


def cargar_partida():
    with open("partidas_guardadas.json", "r") as archivo:
        data2 = json.load(archivo)
    return data2

# data = {
#     "nombre": "Miguel",
#     "edad": 25
# }

# guardar_partida(data)
# print(cargar_partida())

# si = cargar_partida()
# for elemento in si.items():
#     print(elemento)