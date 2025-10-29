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
            pygame.image.load("Graficos/menu_tienda.png"),          # 3: M Tienda
            pygame.image.load("Graficos/menu_guardado.png"),        # 4: M Guardado
            pygame.image.load("Graficos/game_over.png"),            # 5: P GAME OVER
            pygame.image.load("Graficos/pantalla_info.png")         # 6: P Info

        ]
    
    def cargar_botones(self):
        return {
            # P Principal
            "play":         Boton("Graficos/Botones/boton_play.png", 560, 595),

            # P Juego
            "jugar":        Boton("Graficos/Botones/boton_jugar.png", 665, 645),
            "descartar":    Boton("Graficos/Botones/boton_descartar.png", 825, 645),
            "info":         Boton("Graficos/Botones/boton_info.png", 360, 335),

            # M Salida
            "continuar":    Boton("Graficos/Botones/boton_continuar.png", 465, 25),
            "controles":    Boton("Graficos/Botones/boton_controles.png", 465, 165),
            "salir":        Boton("Graficos/Botones/boton_salir.png", 465, 305),
            "save":         Boton("Graficos/Botones/boton_save.png", 595, 425),

            # M Tienda
            "boton_SR":     Boton("Graficos/Botones/boton_siguiente_ronda.png", 345, 250),
            "cambiar":      Boton("Graficos/Botones/boton_cambiar.png", 345, 380),
            "comprar":      Boton("Graficos/Botones/boton_comprar.png", 345, 485),
        
            # M Guardado
            "guardar":      Boton("Graficos/Botones/boton_guardar.png", 435, 515),
            "cargar":       Boton("Graficos/Botones/boton_cargar.png", 655, 515),
            "papelera":     Boton("Graficos/Botones/boton_papelera.png", 960, 525),
            "slot1":        Boton("Graficos/Botones/boton_partida_guardada.png", 285, 155),
            "slot2":        Boton("Graficos/Botones/boton_partida_guardada.png", 535, 155),
            "slot3":        Boton("Graficos/Botones/boton_partida_guardada.png", 785, 155),

            # P Game Over
            "game_over":    Boton("Graficos/Botones/boton_game_over.png", 565, 605)
        }
    
    def reiniciar(self):
        self.jugador = Jugador()


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

        self.botones["jugar"].dibujar(screen)
        self.botones["descartar"].dibujar(screen)
        self.botones["info"].dibujar(screen)


        self.jugador.mostrar_cartas(screen)
        self.jugador.mostrar_puntos(screen)

    def actualizar_pagina_juego(self, eventos):
        if self.jugador.sig_nivel:
            self.jugador.sig_nivel = False
            self.pagina_actual = 3      # M Tienda

        self.jugador.actualizar(eventos)
        
        if self.botones["jugar"].detectar_click(eventos):
            self.jugador.jugar_cartas()
            if self.jugador.game_over:          # Transicion game over
                self.pagina_actual = 5      # P GAME OVER
                self.jugador.game_over = False
        elif self.botones["descartar"].detectar_click(eventos):
            self.jugador.descartar_cartas("boton")
        
        elif self.botones["info"].detectar_click(eventos):
            self.pagina_actual = 6




    # Menu de salida
    def mostrar_menu_salida(self, screen):
        if self.mostrar_fondo:                      # Muestra el fondo una sola vez (Para que funcione bien la transparencia)
            self.mostrar_pagina_juego(screen)
            screen.blit(self.paginas[2], (0,0))
            self.mostrar_fondo = False
            
        self.botones["continuar"].dibujar(screen)
        self.botones["controles"].dibujar(screen)
        self.botones["salir"].dibujar(screen)
        self.botones["save"].dibujar(screen)

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
        elif self.botones["save"].detectar_click(eventos):
            self.mostrar_fondo = True
            self.pagina_actual = 4


    # Tienda
    def mostrar_menu_tienda(self, screen):
        if self.mostrar_fondo:                      # Muestra el fondo una sola vez (Para que funcione bien la transparencia)
            screen.blit(self.paginas[3], (0,0))
            self.mostrar_fondo = False

        self.botones["boton_SR"].dibujar(screen)
        self.botones["cambiar"].dibujar(screen)
        self.botones["comprar"].dibujar(screen)

    def actualizar_menu_tienda(self, eventos):
        if self.botones["boton_SR"].detectar_click(eventos):
            self.pagina_actual = 1
            self.mostrar_fondo = True
        elif self.botones["cambiar"].detectar_click(eventos):
            pass
        elif self.botones["comprar"].detectar_click(eventos):
            pass
    

    # Menu Guardado
    def mostrar_menu_guardado(self, screen):
        if self.mostrar_fondo:                      # Muestra el fondo una sola vez
            screen.blit(self.paginas[4], (0,0))
            self.mostrar_fondo = False

        self.botones["guardar"].dibujar(screen)
        self.botones["cargar"].dibujar(screen)
        self.botones["papelera"].dibujar(screen)
        self.botones["slot1"].dibujar(screen)
        self.botones["slot2"].dibujar(screen)
        self.botones["slot3"].dibujar(screen)

        # Mostrar informacion de cada slot
        self.jugador.mostrar_info_slots(screen)

        # Overlay oscurecido del slot seleccionado
        if 1 <= self.jugador.slot_seleccionado <= 3:
            slot_seleccionado = self.botones[f"slot{self.jugador.slot_seleccionado}"]
            screen.blit(slot_seleccionado.imagen_hover, (slot_seleccionado.x, slot_seleccionado.y))

    def actualizar_menu_guardado(self, eventos):
        if self.botones["guardar"].detectar_click(eventos):
            self.jugador.guardar_partida()
        elif self.botones["cargar"].detectar_click(eventos):
            if self.jugador.cargar_partida():
                self.pagina_actual = 1
        elif self.botones["papelera"].detectar_click(eventos):
            self.jugador.borrar_partida()
        elif self.botones["slot1"].detectar_click(eventos):
            self.jugador.slot_seleccionado = 1
        elif self.botones["slot2"].detectar_click(eventos):
            self.jugador.slot_seleccionado = 2
        elif self.botones["slot3"].detectar_click(eventos):
            self.jugador.slot_seleccionado = 3


    # Pagina GAME OVER                  # Implemetación de graficos por hacer
    def mostrar_pagina_game_over(self, screen):
        if self.mostrar_fondo:                      # Muestra el fondo una sola vez
            screen.blit(self.paginas[5], (0,0))
            self.mostrar_fondo = False
        
        self.botones["game_over"].dibujar(screen)

    def actualizar_pagina_game_over(self, eventos):
        if self.botones["game_over"].detectar_click(eventos):
            self.pagina_actual = 0
            self.mostrar_fondo =  True
            self.reiniciar()

    # Pagina Info
    def mostrar_pantalla_info(self, screen):
        if self.mostrar_fondo:                      # Muestra el fondo una sola vez
            screen.blit(self.paginas[6], (0,0))
            self.mostrar_fondo = False

            
