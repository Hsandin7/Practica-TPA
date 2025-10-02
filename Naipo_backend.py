import pygame


# cartas de cada tipo

class carta:
    def __init__(self, tipo):
        self._tipo = tipo

class carta_normal(carta):
    def __init__(self, tipo, palo, numero):
        tipo = "normal"
        super().__init__(tipo)
        self._palo = palo
        self._numero = numero

class comodin(carta):
    def __init__(self, tipo):
        tipo = "comodin"
        super().__init__(tipo)


class juego:
    def __init__(self, puntos, mano, comodines):
        self._puntos = puntos
        self._mano = mano
        self._comodines = comodines
    
    def descartar_cartas():
        pass

    def jugar_cartas():
        pass
    
    def nueva_mano():
        pass




# Diccionarios...:
# comodines = {
#     "Pereira": comodin(1)
#     "wasdwasd": comodin()

# }