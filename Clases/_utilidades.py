# Las utilidades implementadas tienen un cache. Esto se lleva a cabo creando un
# diccionario con la informacion que se vaya cargando, para asi no tener que cargar
# los elementos una y otra vez, ahorrando tiempo de ejecucion y dandole limpieza al juego

"""
Como usar:
    dentro de la clase que se quiera importar se hace:
        from Clases._utilidades import funcion_que_se_quiera_usar
    o, si se quieren importar todas las funciones:
        from Clases._utilidades import *
"""

import pygame

# Se hace cache de cada uno de los tamanos de fuente
_fuentes = {}
def mostrar_texto(screen, texto: str, posx, posy, tamano=30, color=(255,255,255)):
    if tamano not in _fuentes:
        _fuentes[tamano] = pygame.font.Font("./tipografia_naipo.ttf", tamano)
    fuente = _fuentes[tamano]
    
    texto_renderizado = fuente.render(texto, True, color)
    screen.blit(texto_renderizado, (posx, posy))

def mostrar_texto_centrado(screen, texto, posx_centrada, posy, tamano=30, color=(255,255,255)):
    if tamano not in _fuentes:
        _fuentes[tamano] = pygame.font.Font("./tipografia_naipo.ttf", tamano)
    fuente = _fuentes[tamano]
    
    texto_renderizado = fuente.render(texto, True, color)
    posx = posx_centrada - texto_renderizado.get_width()//2
    screen.blit(texto_renderizado, (posx, posy))


# Cache de los diferentes sonidos del juego
_sonidos = {}
def reproducir_sonido(ruta):
    if ruta not in _sonidos:
        _sonidos[ruta] = pygame.mixer.Sound(ruta)
    _sonidos[ruta].play()