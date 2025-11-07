# Las utilidades implementadas tienen un cache. Esto se lleva a cabo creando un
# diccionario con la informacion que se vaya cargando, para asi no tener que cargar
# los elementos una y otra vez, ahorrando tiempo de ejecucion y dandole limpieza al juego

"""
Como usar:
    dentro de la clase que se quiera importar se hace:
        from src._utilidades import funcion_que_se_quiera_usar
    o, si se quieren importar todas las funciones:
        from src._utilidades import *
"""

import pygame

# Se hace cache de cada uno de los tamanos de fuente y se cargan a traves de esta funcion
_fuentes = {}


def cargar_fuente(tamano):
    if tamano not in _fuentes:
        _fuentes[tamano] = pygame.font.Font("./tipografia_naipo.ttf", tamano)
    return _fuentes[tamano]


def mostrar_texto(
    screen, texto: str, posx: int, posy: int, tamano=30, color=(255, 255, 255)
):
    fuente = cargar_fuente(tamano)

    texto_renderizado = fuente.render(texto, True, color)
    screen.blit(texto_renderizado, (posx, posy))


def mostrar_texto_centrado(
    screen, texto: str, posx_centrada: int, posy: int, tamano=30, color=(255, 255, 255)
):
    fuente = cargar_fuente(tamano)

    texto_renderizado = fuente.render(texto, True, color)
    posx = posx_centrada - texto_renderizado.get_width() // 2
    screen.blit(texto_renderizado, (posx, posy))


def mostrar_texto_transparente(
    screen,
    texto: str,
    posx: int,
    posy: int,
    opacidad: int,
    tamano=30,
    color=(255, 255, 255),
):
    fuente = cargar_fuente(tamano)

    texto_renderizado = fuente.render(texto, True, color)
    superficie = pygame.Surface(texto_renderizado.get_size(), pygame.SRCALPHA)
    superficie.blit(texto_renderizado, (0, 0))
    superficie.set_alpha(opacidad)
    screen.blit(superficie, (posx, posy))


def mostrar_texto_multilinea(
    screen,
    texto: str,
    posx: int,
    posy: int,
    tamano=20,
    color=(255, 255, 255),
    ancho_max=300,
):
    fuente = cargar_fuente(tamano)
    palabras = texto.split(" ")
    lineas = []
    linea_actual = ""

    for palabra in palabras:
        prueba = linea_actual + palabra + " "
        if fuente.size(prueba)[0] > ancho_max:
            lineas.append(linea_actual)
            linea_actual = palabra + " "
        else:
            linea_actual = prueba
    lineas.append(linea_actual)

    for i, linea in enumerate(lineas):
        texto_renderizado = fuente.render(linea.strip(), True, color)
        screen.blit(texto_renderizado, (posx, posy + i * (tamano + 4)))


# Cache de los diferentes sonidos del juego
_sonidos = {}


def reproducir_sonido(ruta: str):
    if ruta not in _sonidos:
        _sonidos[ruta] = pygame.mixer.Sound(ruta)
    _sonidos[ruta].play()
