from carta import Carta
import pygame

class Juego:
    def __init__(self, screen):
        self.screen = screen
        self.screen_width = screen.get_width()
        self.screen_height = screen.get_height()

        self.cargar_imagenes()

    def cargar_imagenes(self):
        # Imágenes de fondo
        self.menu_principal = pygame.image.load("Graficos/Menu_principal.png")
        self.menu_juego = pygame.image.load("Graficos/Menú_Juego.png")
        self.menu_salir = pygame.image.load("Graficos/Control_Salida.png").convert_alpha()

    def cargar_botones(self):
        from boton import Boton
        
        botones = {
            "play": Boton("Graficos/Botones/Boton_Play.png", (560, 595)),
            "continuar": Boton("Graficos/Botones/Boton_Continuar.png", (self.screen_width/2 - 350/2, 25)),
            "controles": Boton("Graficos/Botones/Boton_Controles.png", (self.screen_width/2 - 350/2, 165)),
            "salir": Boton("Graficos/Botones/Boton_Salir.png", (self.screen_width/2 - 350/2, 305)),

            "shop": Boton("Graficos/Botones/Boton_Shop.png", (95, 305)),
            "jugar": Boton("Graficos/Botones/Boton_Jugar.png", (665, 645)),
            "descartar": Boton("Graficos/Botones/Boton_Descartar.png", (825, 645))

        }