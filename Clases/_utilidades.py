# Las utilidades implementadas tienen un caché. Esto se lleva a cabo creando un
# diccionario con la información que se vaya cargando, para así no tener que cargar
# los elementos una y otra vez, ahorrando tiempo de ejecución y dándole limpieza al juego

"""
Como usar:
    dentro de la clase que se quiera importar se hace:
        from Clases._utilidades import funcion_que_se_quiera_usar
    o, si se quieren importar todas las funciones:
        from Clases._utilidades import *
"""

import pygame

# Se hace caché de cada uno de los tamaños de fuente
_fuentes = {}
def mostrar_texto(screen, texto: str, posx, posy, tamaño=30, color=(255,255,255)):
    if tamaño not in _fuentes:
        _fuentes[tamaño] = pygame.font.Font("./tipografia_naipo.ttf", tamaño)
    fuente = _fuentes[tamaño]
    
    texto_renderizado = fuente.render(texto, True, color)
    screen.blit(texto_renderizado, (posx, posy))

def mostrar_texto_centrado(screen, texto, posx_centrada, posy, tamaño=30, color=(255,255,255)):
    if tamaño not in _fuentes:
        _fuentes[tamaño] = pygame.font.Font("./tipografia_naipo.ttf", tamaño)
    fuente = _fuentes[tamaño]
    
    texto_renderizado = fuente.render(texto, True, color)
    posx = posx_centrada - texto_renderizado.get_width()//2
    screen.blit(texto_renderizado, (posx, posy))


# Caché de los diferentes sonidos del juego
_sonidos = {}
def reproducir_sonido(ruta):
    if ruta not in _sonidos:
        _sonidos[ruta] = pygame.mixer.Sound(ruta)
    _sonidos[ruta].play()