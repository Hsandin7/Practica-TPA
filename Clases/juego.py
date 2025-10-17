from Clases.jugador import Jugador
from Clases.boton import Boton
import pygame

class Juego:
    # Atributos de clase
    transicion = False                      # Necesita la imagen cargada de ambas páginas,
    paginas_transicion = [None, None, 0]    # y el número de la 2 [pag1, pag2, num_pag2]
    
    def __init__(self):
        self.pagina_actual = 0      # Páginas: 0: Menú principal, 1: Juego, 2: Menu escape

        self.paginas = self.cargar_paginas()
        self.botones = self.cargar_botones()

        self.jugador = Jugador()
        

    def cargar_paginas(self):
        # Imágenes de fondo
        return [
            pygame.image.load("Graficos/Menu_principal.png"),   # 0: Menú principal
            pygame.image.load("Graficos/Menú_Juego.png"),       # 1: Juego
            pygame.image.load("Graficos/Control_Salida.png")    # 2: Menu escape
        ]
    
    def cargar_botones(self):
        return {
            "play":         Boton("Graficos/Botones/Boton_Play.png", 560, 595),

            "continuar":    Boton("Graficos/Botones/Boton_Continuar.png", 465, 25),
            "controles":    Boton("Graficos/Botones/Boton_Controles.png", 465, 165),
            "salir":        Boton("Graficos/Botones/Boton_Salir.png", 465, 305),

            "shop":         Boton("Graficos/Botones/Boton_Shop.png", 95, 305),
            "jugar":        Boton("Graficos/Botones/Boton_Jugar.png", 665, 645),
            "descartar":    Boton("Graficos/Botones/Boton_Descartar.png", 825, 645)
        }
    
    def reiniciar(self):
        self.__init__()


    # Página principal
    def mostrar_pagina_principal(self, screen):
        screen.blit(self.paginas[0], (0, 0))
        self.botones["play"].dibujar(screen)

    def actualizar_pagina_principal(self, eventos):
        if self.botones["play"].detectar_click(eventos):
            Juego.transicion = True
            Juego.paginas_transicion = [self.paginas[0],self.paginas[1], 1]
            print(Juego.transicion)


    # Página de juego
    def mostrar_pagina_juego(self, screen):
        screen.blit(self.paginas[1], (0,0))
        self.botones["shop"].dibujar(screen)
        self.botones["jugar"].dibujar(screen)
        self.botones["descartar"].dibujar(screen)

        self.jugador.mostrar_mano(screen)
        self.jugador.mostrar_puntos(screen)

    def actualizar_pagina_juego(self, eventos):
        self.jugador.actualizar(eventos)

        if self.botones["shop"].detectar_click(eventos):
            pass    ## Por hacer
        
        elif self.botones["jugar"].detectar_click(eventos):
            self.jugador.jugar_cartas()     ## Por hacer
        
        elif self.botones["descartar"].detectar_click(eventos):
            self.jugador.descartar_cartas()


    # Menú de salida
    def mostrar_menu_salida(self, screen):
        screen.blit(self.paginas[2], (0,0))
        
        self.botones["continuar"].dibujar(screen)
        self.botones["controles"].dibujar(screen)
        self.botones["salir"].dibujar(screen)

    def actualizar_menu_salida(self, eventos):
        if self.botones["continuar"].detectar_click(eventos):
            self.pagina_actual = 1
        elif self.botones["controles"].detectar_click(eventos):
            pass
        elif self.botones["salir"].detectar_click(eventos):
            Juego.transicion = True
            Juego.paginas_transicion = [self.paginas[2],self.paginas[0], 0]
            self.reiniciar()


