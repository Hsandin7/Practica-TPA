from src.jugador import Jugador
from src.tienda import Tienda
from src.boton import Boton
import pygame


class Juego:
    """
    Clase Juego: La clase juego es la que se encarga de cargar todas las paginas y todo la interfaz del jugador.

        Inicializa los atributos:
            - la pagina actual que inicializa en 0
            - la pagina, esta llama a la funcion cargar paginas y situa al jugador en la pagina que debe.
            - el atributo botones llama a la funcion cargar botones y le muestra al jugador los botones adecuados a la situación de la partida.
            - el atributo mostrar fondo esta inicializado a true para mostrar el fondo al jugador.
            - el atributo jugador llama a la clase jugador.
            - el atributo tienda llama a la clase tienda.

    """

    # Atributos de clase
    num_transicion = None  # Necesita la imagen cargada de ambas paginas,
    paginas_transicion = [None, None, 0]  # y el numero de la 2 [pag1, pag2, num_pag2]

    def __init__(self):
        self.pagina_actual = 0
        self.paginas = self.cargar_paginas()
        self.botones = self.cargar_botones()
        self.mostrar_fondo = True

        self.jugador = Jugador()
        self.tienda = Tienda(self.jugador)

    def cargar_paginas(self):
        """Funcion cargar_paginas: Almacena todas las paginas del juego y muestra al jugador la pantalla que debe en cada situación."""
        # Imagenes de fondo
        return [
            pygame.image.load("Graficos/pagina_principal.png"),  # 0: P Principal
            pygame.image.load("Graficos/pagina_juego.png"),  # 1: P Juego
            pygame.image.load("Graficos/menu_salida.png"),  # 2: M Salida
            pygame.image.load("Graficos/menu_tienda.png"),  # 3: M Tienda
            pygame.image.load("Graficos/menu_guardado.png"),  # 4: M Guardado
            pygame.image.load("Graficos/game_over.png"),  # 5: P GAME OVER
            pygame.image.load("Graficos/pantalla_info.png"),  # 6: M Info
        ]

    def cargar_botones(self):
        """Funcion cargar_botones: Carga todas las instancias de los botones para poder ser usadas por el jugador."""
        return {
            # P Principal
            "play": Boton("Graficos/Botones/boton_play.png", 560, 595),
            # P Juego
            "jugar": Boton("Graficos/Botones/boton_jugar.png", 665, 645),
            "descartar": Boton("Graficos/Botones/boton_descartar.png", 825, 645),
            "info": Boton("Graficos/Botones/boton_info.png", 360, 335),
            # M Salida
            "continuar": Boton("Graficos/Botones/boton_continuar.png", 465, 25),
            "controles": Boton("Graficos/Botones/boton_controles.png", 465, 165),
            "salir": Boton("Graficos/Botones/boton_salir.png", 465, 305),
            "save": Boton("Graficos/Botones/boton_save.png", 595, 425),
            # M Tienda
            "boton_SR": Boton("Graficos/Botones/boton_siguiente_ronda.png", 345, 250),
            "cambiar": Boton("Graficos/Botones/boton_cambiar.png", 345, 380),
            "comprar": Boton(
                "Graficos/Botones/boton_comprar.png",
                345,
                485,
                "Sonidos/sonido_comprar.mp3",
            ),
            # M Guardado
            "guardar": Boton("Graficos/Botones/boton_guardar.png", 435, 515),
            "cargar": Boton("Graficos/Botones/boton_cargar.png", 655, 515),
            "papelera": Boton("Graficos/Botones/boton_papelera.png", 960, 525),
            "slot1": Boton("Graficos/Botones/boton_partida_guardada.png", 285, 155),
            "slot2": Boton("Graficos/Botones/boton_partida_guardada.png", 535, 155),
            "slot3": Boton("Graficos/Botones/boton_partida_guardada.png", 785, 155),
            # P Game Over
            "game_over": Boton("Graficos/Botones/boton_game_over.png", 565, 605),
        }

    def reiniciar(self):
        """Funcion reiniciar: Reinicia la partida creando un nuevo jugador."""
        self.jugador = Jugador()
        self.tienda = Tienda(self.jugador)

    # Pagina principal
    def mostrar_pagina_principal(self, screen):
        """Funcion mostrar_pagina_principal: La función muestra el fondo una unica vez y dibuja el boton de play para que el usuario pueda empezar a jugar."""
        if self.mostrar_fondo:  # Muestra el fondo una sola vez
            screen.blit(self.paginas[0], (0, 0))
            self.mostrar_fondo = False

        self.botones["play"].dibujar(screen)

    def actualizar_pagina_principal(self, eventos):
        """Funcion mostrar_pagina_principal: La función muestra el fondo una unica vez y dibuja el boton de play para que el usuario pueda empezar a jugar."""
        if self.botones["play"].detectar_click(eventos):
            self.mostrar_fondo = True
            Juego.num_transicion = 1  # Transicion 1
            Juego.paginas_transicion = [
                self.paginas[0],
                self.paginas[1],
                1,
            ]  # De la pagina 0 a la 1

    # Pagina de juego
    def mostrar_pagina_juego(self, screen):
        """Funcion mostrar_pagina_juego: Muestra por pantalla la pagina del juego como los botones, fondo o el filtro de color cuando se alcanza un jefe."""
        if self.jugador.niveles.es_boss:
            self.jugador.niveles.dibujar_filtro_pantalla(screen)
        else:
            screen.blit(self.paginas[1], (0, 0))

        self.botones["jugar"].dibujar(screen)
        self.botones["descartar"].dibujar(screen)
        self.botones["info"].dibujar(screen)

        self.jugador.mostrar_cartas(screen)
        self.jugador.mostrar_puntos(screen)

    def actualizar_pagina_juego(self, eventos):
        """Funcion mostrar_pagina_principal: Procesa eventos y los clicks que se hacen en los botones,
        muestra cuando el jugador se pasa un nivel y accede a la tieda, o muestra el panel de informacion cuando se hace click en el boton de informacion.
        """
        self.jugador.actualizar(eventos)

        if self.botones["jugar"].detectar_click(eventos):
            self.jugador.jugar_cartas()
            if self.jugador.game_over:  # Transicion game over
                self.jugador.game_over = False
                self.mostrar_fondo = True
                Juego.num_transicion = 4  # Transicion 4 (Transicion de Game Over)
                Juego.paginas_transicion = [
                    self.paginas[1],
                    self.paginas[5],
                    5,
                ]  # De la pagina 1 a la 5
            elif self.jugador.nivel_completado:
                self.jugador.nivel_completado = False
                self.tienda.poblar()
                self.mostrar_fondo = True
                Juego.num_transicion = 2  # Transicion 2 (La bajada de la tienda)
                Juego.paginas_transicion = [
                    self.paginas[1],
                    self.paginas[3],
                    3,
                ]  # De la pagina 1 a la 3
        elif self.botones["descartar"].detectar_click(eventos):
            self.jugador.descartar_cartas("boton")

        elif self.botones["info"].detectar_click(eventos):
            self.pagina_actual = 6
            # self.jugador.nivel_completado = False
            # self.mostrar_fondo = True
            # Juego.num_transicion = 2        # Transicion 2 (La bajada de la tienda)
            # Juego.paginas_transicion = [self.paginas[1], self.paginas[6], 6]    # De la pagina 1 a la 6

    # Menu de salida
    def mostrar_menu_salida(self, screen):
        """Funcion mostrar_menu_salida: Esta funcion muestra el fonddo y muestra los botones continuar, controles, salir y save."""
        if (
            self.mostrar_fondo
        ):  # Muestra el fondo una sola vez (Para que funcione bien la transparencia)
            self.mostrar_pagina_juego(screen)
            screen.blit(self.paginas[2], (0, 0))
            self.mostrar_fondo = False

        self.botones["continuar"].dibujar(screen)
        self.botones["controles"].dibujar(screen)
        self.botones["salir"].dibujar(screen)
        self.botones["save"].dibujar(screen)

    def actualizar_menu_salida(self, eventos):
        """Funcion actualizar_menu_salida: Detecta los botones continuar, controles, salir y save, y realiza las respectivas funciones de cada boton."""
        if self.botones["continuar"].detectar_click(eventos):
            self.pagina_actual = 1
            self.mostrar_fondo = True
        elif self.botones["controles"].detectar_click(eventos):
            pass
        elif self.botones["salir"].detectar_click(eventos):
            Juego.num_transicion = 1  # Transicion 1
            Juego.paginas_transicion = [
                self.paginas[2],
                self.paginas[0],
                0,
            ]  # De la pagina 2 a la 0
            self.reiniciar()
        elif self.botones["save"].detectar_click(eventos):
            self.mostrar_fondo = True
            self.pagina_actual = 4

    # Tienda
    def mostrar_menu_tienda(self, screen):
        """Funcion mostrar_menu_tienda: Aquí muestra los botonesde la tienda y el fondo de la misma."""
        screen.blit(self.paginas[3], (0, 0))

        self.botones["boton_SR"].dibujar(screen)
        self.botones["cambiar"].dibujar(screen)
        self.botones["comprar"].dibujar(screen)

        self.tienda.mostrar(screen)

    def actualizar_menu_tienda(self, eventos):
        """Funcion actualizar_menu_tienda: Aquí se detectan los clicks en los botones de la tienda y se realizan las respectivas funciones de cada uno."""
        self.tienda.actualizar(eventos)

        if self.botones["boton_SR"].detectar_click(eventos):
            self.mostrar_fondo = True
            Juego.num_transicion = 3
            Juego.paginas_transicion = [self.paginas[1], self.paginas[3], 1]
            self.tienda.coste_cambiar = 2  # Resetear coste al salir

        elif self.botones["cambiar"].detectar_click(eventos):
            self.tienda.cambiar()
        elif self.botones["comprar"].detectar_click(eventos):
            self.tienda.comprar()

    # Menu Guardado
    def mostrar_menu_guardado(self, screen):
        """Funcion mostrar_menu_guardado: Esta funcion muestra todos los botones del menú de guardado,
        muestra la información de cada eslot y muestra el overlay mas oscuro del
        slot que se selecciona."""
        if self.mostrar_fondo:  # Muestra el fondo una sola vez
            screen.blit(self.paginas[4], (0, 0))
            self.mostrar_fondo = False

        self.botones["guardar"].dibujar(screen)
        self.botones["cargar"].dibujar(screen)
        self.botones["papelera"].dibujar(screen)
        self.botones["slot1"].dibujar(screen)
        self.botones["slot2"].dibujar(screen)
        self.botones["slot3"].dibujar(screen)

        # Mostrar informacion de cada slot
        self.jugador.guardado.mostrar_info_slots(screen)

        # Overlay oscurecido del slot seleccionado
        if self.jugador.slot_seleccionado:
            slot_seleccionado = self.botones[f"slot{self.jugador.slot_seleccionado}"]
            screen.blit(
                slot_seleccionado.imagen_hover,
                (slot_seleccionado.x, slot_seleccionado.y),
            )

    def actualizar_menu_guardado(self, eventos):
        """Funcion actualizar_menu_guardado: Aquí se realizan las funciones del los botones del menú de guardado y se selecciona el slot donde se va a guardar."""
        if self.botones["guardar"].detectar_click(eventos):
            self.jugador.guardar_partida()
        elif self.botones["cargar"].detectar_click(eventos):
            if self.jugador.cargar_partida():
                self.pagina_actual = 1
        elif self.botones["papelera"].detectar_click(eventos):
            self.jugador.borrar_partida()
        elif self.botones["slot1"].detectar_click(eventos):
            if self.jugador.slot_seleccionado != 1:
                self.jugador.slot_seleccionado = 1
            else:
                self.jugador.slot_seleccionado = None
        elif self.botones["slot2"].detectar_click(eventos):
            if self.jugador.slot_seleccionado != 2:
                self.jugador.slot_seleccionado = 2
            else:
                self.jugador.slot_seleccionado = None
        elif self.botones["slot3"].detectar_click(eventos):
            if self.jugador.slot_seleccionado != 3:
                self.jugador.slot_seleccionado = 3
            else:
                self.jugador.slot_seleccionado = None

    # Pagina GAME OVER                  # Implemetación de graficos por hacer
    def mostrar_pagina_game_over(self, screen):
        """Funcion mostrar_pagina_game_over: Esta fucnion dibuja la pantalla de game over con su fondo y su botón."""
        if self.mostrar_fondo:  # Muestra el fondo una sola vez
            screen.blit(self.paginas[5], (0, 0))
            self.mostrar_fondo = False

        self.botones["game_over"].dibujar(screen)

    def actualizar_pagina_game_over(self, eventos):
        """Funcion actualizar_pagina_game_over: Detecta el click al botón de game over y reinicia el juego volviendo al menú principal con su respectiva transicción."""
        if self.botones["game_over"].detectar_click(eventos):
            self.mostrar_fondo = True
            Juego.num_transicion = (
                5  # Transicion 5 (Desintegracion a la pagina de inicio)
            )
            Juego.paginas_transicion = [
                self.paginas[5],
                self.paginas[0],
                0,
            ]  # De la pagina 3 a la 1
            self.reiniciar()

    # Menu Info
    def mostrar_pantalla_info(self, screen):
        """Funcion mostrar_pantalla_info: Muestra la pantalla de información con todas las jugadas y cuantos puntos suman cada una."""
        if self.mostrar_fondo:  # Muestra el fondo una sola vez
            screen.blit(self.paginas[6], (0, 0))
            self.mostrar_fondo = False
