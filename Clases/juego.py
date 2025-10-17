from Clases.jugador import Jugador
from Clases.boton import Boton
import pygame

class Juego:
    # Atributos de clase
    transicion = False                      # Necesita la imagen cargada de ambas paginas,
    paginas_transicion = [None, None, 0]    # y el numero de la 2 [pag1, pag2, num_pag2]
    
    def __init__(self):
        self.pagina_actual = 0      # Paginas: 0: P Principal, 1: P Juego, 2: M Salida, 3: M tienda

        self.paginas = self.cargar_paginas()
        self.botones = self.cargar_botones()
        self.mostrar_fondo = True

        self.jugador = Jugador()
        

    def cargar_paginas(self):
        # Imagenes de fondo
        return [
            pygame.image.load("Graficos/pagina_principal.png"),     # 0: P Principal
            pygame.image.load("Graficos/pagina_juego.png"),         # 1: P Juego
            pygame.image.load("Graficos/menu_salida.png"),          # 2: M Salida
            pygame.image.load("Graficos/menu_tienda.png")           # 3: M Tienda
        ]
    
    def cargar_botones(self):
        return {
            "play":         Boton("Graficos/Botones/boton_play.png", 560, 595),

            "continuar":    Boton("Graficos/Botones/boton_continuar.png", 465, 25),
            "controles":    Boton("Graficos/Botones/boton_controles.png", 465, 165),
            "salir":        Boton("Graficos/Botones/boton_salir.png", 465, 305),

            "shop":         Boton("Graficos/Botones/boton_shop.png", 95, 305),
            "jugar":        Boton("Graficos/Botones/boton_jugar.png", 665, 645),
            "descartar":    Boton("Graficos/Botones/boton_descartar.png", 825, 645),

            "boton_SR":     Boton("Graficos/Botones/boton_siguiente_ronda.png", 345, 250),
            "cambiar":      Boton("Graficos/Botones/boton_cambiar.png", 345, 380),
            "comprar":      Boton("Graficos/Botones/boton_comprar.png", 345, 485)
        }
    
    def reiniciar(self):
        self.__init__()


    # Pagina principal
    def mostrar_pagina_principal(self, screen):
        if self.mostrar_fondo:                      # Muestra el fondo una sola vez
            screen.blit(self.paginas[0], (0, 0))
            self.mostrar_fondo = False

        self.botones["play"].dibujar(screen)

    def actualizar_pagina_principal(self, eventos):
        if self.botones["play"].detectar_click(eventos):
            self.mostrar_fondo = True
            Juego.transicion = True
            Juego.paginas_transicion = [self.paginas[0],self.paginas[1], 1]


    # Pagina de juego
    def mostrar_pagina_juego(self, screen):
        screen.blit(self.paginas[1], (0,0))

        self.botones["shop"].dibujar(screen)
        self.botones["jugar"].dibujar(screen)
        self.botones["descartar"].dibujar(screen)

        self.jugador.mostrar_cartas(screen)
        self.jugador.mostrar_puntos(screen)

    def actualizar_pagina_juego(self, eventos):
        self.jugador.actualizar(eventos)

        if self.botones["shop"].detectar_click(eventos):
            self.pagina_actual = 3
            self.mostrar_fondo = True
        
        elif self.botones["jugar"].detectar_click(eventos):
            self.jugador.jugar_cartas()     ## Por hacer
        
        elif self.botones["descartar"].detectar_click(eventos):
            self.jugador.descartar_cartas()


    # Menu de salida
    def mostrar_menu_salida(self, screen):
        if self.mostrar_fondo:                      # Muestra el fondo una sola vez (Para que funcione bien la transparencia)
            screen.blit(self.paginas[2], (0,0))
            self.mostrar_fondo = False
            
        self.botones["continuar"].dibujar(screen)
        self.botones["controles"].dibujar(screen)
        self.botones["salir"].dibujar(screen)

    def actualizar_menu_salida(self, eventos):
        if self.botones["continuar"].detectar_click(eventos):
            self.pagina_actual = 1
            self.mostrar_fondo = True
        elif self.botones["controles"].detectar_click(eventos):
            pass
        elif self.botones["salir"].detectar_click(eventos):
            Juego.transicion = True
            Juego.paginas_transicion = [self.paginas[2],self.paginas[0], 0]
            self.reiniciar()


    # Tienda
    def mostrar_Tienda(self, screen):
        if self.mostrar_fondo:                      # Muestra el fondo una sola vez (Para que funcione bien la transparencia)
            screen.blit(self.paginas[3], (0,0))
            self.mostrar_fondo = False

        self.botones["boton_SR"].dibujar(screen)
        self.botones["cambiar"].dibujar(screen)
        self.botones["comprar"].dibujar(screen)

    def actualizar_Tienda(self, eventos):
        if self.botones["boton_SR"].detectar_click(eventos):
            self.pagina_actual = 1
            self.mostrar_fondo = True
        elif self.botones["cambiar"].detectar_click(eventos):
            pass
        elif self.botones["comprar"].detectar_click(eventos):
            pass