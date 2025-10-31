from Clases.jugador import Jugador
from Clases.boton import Boton
from Clases.comodines import Comodin
from Clases._utilidades import mostrar_texto, mostrar_texto_centrado
import pygame
import random

class Juego:
    # Atributos de clase
    num_transicion = None                   # Necesita la imagen cargada de ambas paginas,
    paginas_transicion = [None, None, 0]    # y el numero de la 2 [pag1, pag2, num_pag2]
    
    def __init__(self):
        self.pagina_actual = 0      
        self.paginas = self.cargar_paginas()
        self.botones = self.cargar_botones()
        self.mostrar_fondo = True

        self.jugador = Jugador()
        
        self.coste_cambiar = 2 
        self.tienda_comodines = [None, None]
        self.comodin_seleccionado = None
        
        self.comodines_disponibles = [
            "gloton", "stonks", "matematico", "calculadora", "loco", 
            "doblete", "esteroides", "programador", "clon"
        ]
        

    def cargar_paginas(self):
        # Imagenes de fondo
        return [
            pygame.image.load("Graficos/pagina_principal.png"),     # 0: P Principal
            pygame.image.load("Graficos/pagina_juego.png"),         # 1: P Juego
            pygame.image.load("Graficos/menu_salida.png"),          # 2: M Salida
            pygame.image.load("Graficos/menu_tienda.png"),          # 3: M Tienda
            pygame.image.load("Graficos/menu_guardado.png"),        # 4: M Guardado
            pygame.image.load("Graficos/game_over.png"),            # 5: P GAME OVER
            pygame.image.load("Graficos/pantalla_info.png")         # 6: M Info

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
    
    def poblar_tienda(self):
        pos_slot_1 = (690, 250)
        pos_slot_2 = (840, 250)
        
        # Elegir nombres de comodines aleatoriamente
        nombre1 = random.choice(self.comodines_disponibles)
        nombre2 = random.choice(self.comodines_disponibles)
        
        # Crear objetos Comodin y asignarles posición
        self.tienda_comodines[0] = Comodin(nombre1)
        self.tienda_comodines[0].asignar_posicion(pos_slot_1[0], pos_slot_1[1])
        
        self.tienda_comodines[1] = Comodin(nombre2)
        self.tienda_comodines[1].asignar_posicion(pos_slot_2[0], pos_slot_2[1])
        
        # Deseleccionar cualquier comodin anterior
        self.comodin_seleccionado = None
        self.tienda_comodines[0].seleccionada = False
        self.tienda_comodines[1].seleccionada = False

    def reiniciar(self):
        self.jugador = Jugador()
        self.coste_cambiar = 2
        self.tienda_comodines = [None, None]
        self.comodin_seleccionado = None

    # Pagina principal
    def mostrar_pagina_principal(self, screen):
        if self.mostrar_fondo:                      # Muestra el fondo una sola vez
            screen.blit(self.paginas[0], (0, 0))
            self.mostrar_fondo = False

        self.botones["play"].dibujar(screen)

    def actualizar_pagina_principal(self, eventos):
        if self.botones["play"].detectar_click(eventos):
            self.mostrar_fondo = True
            Juego.num_transicion = 1        # Transicion 1
            Juego.paginas_transicion = [self.paginas[0], self.paginas[1], 1]    # De la pagina 0 a la 1


    # Pagina de juego
    def mostrar_pagina_juego(self, screen):
        screen.blit(self.paginas[1], (0,0))
        if self.jugador.niveles.es_boss:
            
            if self.jugador.carta_inhabilitada is None:
                valor_inhabilitado = random.randint(1,12)
                print(f"Valor BOSS inavilitado {valor_inhabilitado}")
                self.jugador.carta_inhabilitada = valor_inhabilitado

                for carta in self.jugador.mazo.cartas + self.jugador.mano:
                    if carta.valor == valor_inhabilitado:
                        carta.habilitada = False

            filtro_color = pygame.Surface(screen.get_size(), pygame.SRCALPHA)

            r, g, b = self.jugador.niveles.color_pantalla
            filtro_color.fill((r , g, b, 120))
            screen.blit(filtro_color, (0,0))

        else:
            if self.jugador.carta_inhabilitada is not None:
                for carta in self.jugador.mazo.cartas + self.jugador.mano:
                    carta.habilitada = True
                self.jugador.carta_inhabilitada = None

        self.botones["jugar"].dibujar(screen)
        self.botones["descartar"].dibujar(screen)
        self.botones["info"].dibujar(screen)


        self.jugador.mostrar_cartas(screen)
        self.jugador.mostrar_puntos(screen)
        self.jugador.mostrar_comodines_mano(screen)

    def actualizar_pagina_juego(self, eventos):
        self.jugador.actualizar(eventos)
        
        if self.botones["jugar"].detectar_click(eventos):
            self.jugador.jugar_cartas()
            if self.jugador.game_over:          # Transicion game over
                self.jugador.game_over = False
                self.mostrar_fondo = True
                Juego.num_transicion = 4        # Transicion 4 (Transicion de Game Over)
                Juego.paginas_transicion = [self.paginas[1], self.paginas[5], 5]    # De la pagina 1 a la 5
            elif self.jugador.sig_nivel:
                self.jugador.sig_nivel = False
                self.mostrar_fondo = True
                self.poblar_tienda()
                Juego.num_transicion = 2        # Transicion 2 (La bajada de la tienda)
                Juego.paginas_transicion = [self.paginas[1], self.paginas[3], 3]    # De la pagina 1 a la 3
        elif self.botones["descartar"].detectar_click(eventos):
            self.jugador.descartar_cartas("boton")
        
        elif self.botones["info"].detectar_click(eventos):
            self.pagina_actual = 6
            # self.jugador.sig_nivel = False
            # self.mostrar_fondo = True
            # Juego.num_transicion = 2        # Transicion 2 (La bajada de la tienda)
            # Juego.paginas_transicion = [self.paginas[1], self.paginas[6], 6]    # De la pagina 1 a la 6




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
            Juego.num_transicion = 1        # Transicion 1
            Juego.paginas_transicion = [self.paginas[2],self.paginas[0], 0]     # De la pagina 2 a la 0
            self.reiniciar()
        elif self.botones["save"].detectar_click(eventos):
            self.mostrar_fondo = True
            self.pagina_actual = 4


    # Tienda
    def mostrar_menu_tienda(self, screen):
        if self.mostrar_fondo:
            screen.blit(self.paginas[3], (0,0))
            self.mostrar_fondo = False

        # Dibujar botones base
        self.botones["boton_SR"].dibujar(screen)
        self.botones["cambiar"].dibujar(screen)
        self.botones["comprar"].dibujar(screen)

        # Mostrar dinero actual del jugador
        mostrar_texto_centrado(screen, f"{self.jugador.dinero}$", 900, 150, 40, (255, 255, 255))

        color_coste = (255, 255, 0) # Amarillo si se puede pagar
        if self.jugador.dinero < self.coste_cambiar:
            color_coste = (255, 0, 0) # Rojo si no
        
        # Posición al lado del botón "Cambiar"
        mostrar_texto(screen, f"{self.coste_cambiar}$", 525, 400 , 30, color_coste)

        for comodin in self.tienda_comodines:
            if comodin: # Dibujar solo si el slot no está vendido (no es None)
                comodin.dibujar(screen)
                
                # Mostrar precio
                color_precio = (255, 255, 0) # Amarillo
                if self.jugador.dinero < comodin.precio:
                    color_precio = (255, 0, 0) # Rojo
                mostrar_texto_centrado(screen, f"{comodin.precio}$", comodin.rect.midbottom[0], comodin.rect.bottom + 3, 20, color_precio)
                
                # Resaltar si está seleccionado
                # if comodin.seleccionada: # Usamos el atributo del comodín
                #     screen.blit(comodin.imagen_hover, (comodin, comodin.y))

    def actualizar_menu_tienda(self, eventos):
        
        # Detectar clics en comodines para seleccionar
        for comodin in self.tienda_comodines:
            if comodin and comodin.detectar_seleccion(eventos):
                if comodin.seleccionada: # Si ya estaba seleccionado
                    comodin.seleccionada = False
                    self.comodin_seleccionado = None
                else: # Si no estaba seleccionado
                    # Deseleccionar el otro (si lo hay)
                    for c in self.tienda_comodines:
                        if c: c.seleccionada = False
                    # Seleccionar este
                    comodin.seleccionada = True
                    self.comodin_seleccionado = comodin

        # Detectar clics en botones
        if self.botones["boton_SR"].detectar_click(eventos):
            self.mostrar_fondo = True
            Juego.num_transicion = 3
            Juego.paginas_transicion = [self.paginas[1], self.paginas[3], 1]
            self.coste_cambiar = 2 # Resetear coste al salir
        
        elif self.botones["cambiar"].detectar_click(eventos):
            if self.jugador.dinero >= self.coste_cambiar:
                self.jugador.dinero -= self.coste_cambiar
                self.coste_cambiar += 2 # Incrementar coste
                self.poblar_tienda() # Cargar 2 nuevos comodines
            else:
                pass

        # Lógica de "Comprar"
        elif self.botones["comprar"].detectar_click(eventos):
            if self.comodin_seleccionado and \
               self.jugador.dinero >= self.comodin_seleccionado.precio and \
               len(self.jugador.comodines_mano) < 5:
                
                # Pagar
                self.jugador.dinero -= self.comodin_seleccionado.precio
                
                # Añadir comodín al jugador
                self.jugador.comodines_mano.append(self.comodin_seleccionado)
                
                # Quitar comodín de la tienda
                try:
                    index = self.tienda_comodines.index(self.comodin_seleccionado)
                    self.tienda_comodines[index] = None # Poner el slot a None
                except ValueError:
                    pass # El comodín ya no estaba
                
                # Deseleccionar
                self.comodin_seleccionado = None
    

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
            self.mostrar_fondo = True
            Juego.num_transicion = 5        # Transicion 5 (Desintegracion a la pagina de inicio)
            Juego.paginas_transicion = [self.paginas[5], self.paginas[0], 0]    # De la pagina 3 a la 1
            
            self.pagina_actual = 0
            self.mostrar_fondo =  True
            self.reiniciar()

    # Menu Info
    def mostrar_pantalla_info(self, screen):
        if self.mostrar_fondo:                      # Muestra el fondo una sola vez
            screen.blit(self.paginas[6], (0,0))
            self.mostrar_fondo = False

            
