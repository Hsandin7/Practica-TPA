from Clases.mazo import Mazo
from Clases.jugador import Jugador
from Clases.boton import Boton
import pygame

class Juego:
    def __init__(self, screen):
        self._screen = screen
        self.screen_width = screen.get_width()
        self.screen_height = screen.get_height()
        self.pagina_actual = 0      # Páginas: 0: Menú principal, 1: Juego, 2: Menu escape

        self._cargar_imagenes()
        self.botones = self.cargar_botones()

        self.mazo = Mazo()
        self.jugador = Jugador(self.mazo)
        

    def _cargar_imagenes(self):
        # Imágenes de fondo
        self.menu_principal = pygame.image.load("Graficos/Menu_principal.png")
        self.menu_juego = pygame.image.load("Graficos/Menú_Juego.png")
        self.menu_salir = pygame.image.load("Graficos/Control_Salida.png").convert_alpha()

    def cargar_botones(self):
        return {
            "play": Boton("Graficos/Botones/Boton_Play.png", (560, 595)),

            "continuar": Boton("Graficos/Botones/Boton_Continuar.png", (self.screen_width/2 - 350/2, 25)),
            "controles": Boton("Graficos/Botones/Boton_Controles.png", (self.screen_width/2 - 350/2, 165)),
            "salir": Boton("Graficos/Botones/Boton_Salir.png", (self.screen_width/2 - 350/2, 305)),

            "shop": Boton("Graficos/Botones/Boton_Shop.png", (95, 305)),
            "jugar": Boton("Graficos/Botones/Boton_Jugar.png", (665, 645)),
            "descartar": Boton("Graficos/Botones/Boton_Descartar.png", (825, 645))
        }


    def mostrar_pagina_principal(self, eventos):
        self._screen.blit(self.menu_principal, (0, 0))
        self.botones["play"].dibujar(self._screen)

        if self.botones["play"].detectar_click(eventos):
            self.pagina_actual = 1


    def mostrar_pagina_juego(self, eventos):
        self._screen.blit(self.menu_juego, (0,0))
        self.botones["shop"].dibujar(self._screen)
        self.botones["jugar"].dibujar(self._screen)
        self.botones["descartar"].dibujar(self._screen)

        self.jugador.mostrar_mano(self._screen)

        if self.botones["shop"].detectar_click(eventos):
            pass    ## Por hacer
        elif self.botones["jugar"].detectar_click(eventos):
            pass    ## Por hacer
        elif self.botones["descartar"].detectar_click(eventos):
            pass    ## Por hacer
        

    def mostrar_menu_salida(self, eventos):
        self._screen.blit(self.menu_salir, (0,0))
        
        self.botones["continuar"].dibujar(self._screen)
        self.botones["controles"].dibujar(self._screen)
        self.botones["salir"].dibujar(self._screen)

        if self.botones["continuar"].detectar_click(eventos):
            self.pagina_actual = 1
        elif self.botones["controles"].detectar_click(eventos):
            pass
        elif self.botones["salir"].detectar_click(eventos):
            self.pagina_actual = 0


   
    def mostrar_cartas(self):
        self.jugador.mostrar_mano()
