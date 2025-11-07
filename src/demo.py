from src.juego import Juego
from src.animaciones import Transicion
from src.comodines import Comodin
from src.guardado import Guardado
from src.texto import *

# Pos boton jugar = (730, 670)
# Pos boton descartar = (925, 670)


class Demo:
    def __init__(self, juego: Juego, transicion: Transicion):
        self.juego = juego
        self.transicion = transicion
        self.activa = False
        self.fase = 1
        self.contador = 0
        self.funcionar = True
        self.raton = Cursor(1280 / 2, 720 / 2)
        self.guardado = Guardado()
        self.comodin = Comodin("calculadora")
        self.tiempo_fase = {fase: 90 for fase in range(1, 60)}
        self.fases_seleccion_cartas = {6, 8, 10, 12, 17, 19, 21, 23, 25, 32, 58, 60}
        self.indice_carta = 0
        self._seleccionando = False
        self._cartas_a_seleccionar = []
        self._pause_frames = 20
        self.guardado_previo = []

        filtro_tienda = pygame.Surface((1280, 720), masks=(0, 0, 0, 0))
        filtro_tienda.set_alpha(144)
        self.p_juego_tienda = self.juego.paginas[1].copy()
        self.p_juego_tienda.blit(filtro_tienda, (0, 0))

    def checkear_inicio(self):
        self.contador += 1
        if self.contador > 5 * 60:  # 5s x 60fps para esperar en total 5s
            self.activa = True
            self.crear_partidas_customizadas()
            self.contador = 0

    def checkear_siguiente(self, eventos):
        pass

    def ejecutar_demo(self, screen, eventos):
        self.checkear_siguiente(eventos)
        # Ir a pagina de Juego
        match self.fase:
            case 1:
                self.juego.mostrar_fondo = True
                Juego.num_transicion = 1
                Juego.paginas_transicion = [
                    self.juego.paginas[0],
                    self.juego.paginas[1],
                    1,
                ]
                self.transicion.iniciar(*Juego.paginas_transicion, Juego.num_transicion)

                # Cargar guardado 1
                self.juego.jugador.slot_seleccionado = 1
                self.juego.jugador.cargar_partida()
                self.fase += 1
            case 2:
                self.juego.mostrar_pagina_juego(screen)
            case 3:
                self.juego.mostrar_pagina_juego(screen)
                if self.funcionar:
                    self.funcionar = False
                    self.raton.asignar_posicion(410, 355)
            case 4:  # Mostrar info
                self.juego.mostrar_pantalla_info(screen)
            case 5:
                self.juego.mostrar_pagina_juego(screen)
            case 6:
                self.juego.mostrar_pagina_juego(screen)
                self.seleccionar_cartas([2, 5, 6, 7], self.juego)
            case 7:
                self.juego.mostrar_pagina_juego(screen)
                self.boton_jugar()
            case 8:
                self.juego.mostrar_pagina_juego(screen)
                self.seleccionar_cartas([0, 2, 5, 6, 7], self.juego)
            case 9:
                self.juego.mostrar_pagina_juego(screen)
                self.boton_descartar()
            case 10:
                self.juego.mostrar_pagina_juego(screen)
                self.seleccionar_cartas([3, 5, 6, 7], self.juego)
            case 11:
                self.juego.mostrar_pagina_juego(screen)
                self.boton_descartar()
            case 12:
                self.juego.mostrar_pagina_juego(screen)
                self.seleccionar_cartas([0, 1, 2, 3, 5], self.juego)
            case 13:
                self.juego.mostrar_pagina_juego(screen)
                self.boton_jugar()
            case 14:
                self.juego.mostrar_pagina_juego(screen)
                self.boton_jugar()
            case 15:
                self.abrir_tienda(
                    [Comodin("esteroides"), Comodin("gloton")]
                )  # Abrir tienda
                if self.funcionar:
                    self.funcionar = False
                    self.raton.asignar_posicion(200, 200)
                self.fase = 16
            case 16:
                self.mostrar_tienda(screen)
                self.boton_SR()
            case 17:
                self.guardado.guardar_partida(1, self.guardado_2)
                self.juego.jugador.cargar_partida()
                self.fase = 18
            case 18:
                self.juego.mostrar_pagina_juego(screen)
                if self.funcionar:
                    self.funcionar = False
                    self.raton.asignar_posicion(500, 500)
            case 19:
                self.juego.mostrar_pagina_juego(screen)
                self.seleccionar_cartas([5, 7], self.juego)
            case 20:
                self.juego.mostrar_pagina_juego(screen)
                self.boton_jugar()
            case 21:
                self.juego.mostrar_pagina_juego(screen)
                self.seleccionar_cartas([1, 2, 6, 7], self.juego)
            case 22:
                self.juego.mostrar_pagina_juego(screen)
                self.boton_descartar()
            case 23:
                self.juego.mostrar_pagina_juego(screen)
                self.seleccionar_cartas([4, 5, 6, 7], self.juego)
            case 24:
                self.juego.mostrar_pagina_juego(screen)
                self.boton_descartar()
            case 25:
                self.juego.mostrar_pagina_juego(screen)
                self.seleccionar_cartas([0, 1, 2, 3, 7], self.juego)
            case 26:
                self.juego.mostrar_pagina_juego(screen)
                self.boton_jugar()
            case 27:
                self.abrir_tienda([Comodin("calculadora"), Comodin("loco")])
                if self.funcionar:
                    self.funcionar = False
                    self.raton.asignar_posicion(200, 200)
                self.fase = 28
            case 28:
                self.mostrar_tienda(screen)
            case 29:
                self.mostrar_tienda(screen)
                self.raton.asignar_posicion(740, 320)
                self.juego.tienda.comodin_seleccionado = (
                    self.juego.tienda.tienda_comodines[0]
                )
                self.juego.tienda.tienda_comodines[0].seleccionada = True
            case 30:
                self.mostrar_tienda(screen)
                self.boton_comprar()
            case 31:
                self.mostrar_tienda(screen)
                self.boton_SR()
                # self.juego.jugador.comodines_mano = [Comodin("calculadora")]
            case 32:
                self.guardado.guardar_partida(1, self.guardado_3)
                self.juego.jugador.cargar_partida()
                self.fase = 33
            case 33:
                self.juego.mostrar_pagina_juego(screen)

                self.guardado.borrar_partida(1)
                self.guardado.borrar_partida(3)
                self.guardado.guardar_partida(2, self.guardado_5)

            case 34:
                self.juego.mostrar_fondo = True
                self.juego.mostrar_pagina_juego(screen)
                self.juego.mostrar_menu_salida(screen)
                if self.funcionar:
                    self.funcionar = False
                    self.raton.asignar_posicion(635, 485)  # Boton M Guardado
            case 35:
                self.juego.mostrar_fondo = True
                self.juego.mostrar_menu_guardado(screen)
            case 36:
                self.juego.mostrar_fondo = True
                self.juego.mostrar_menu_guardado(screen)
                if self.funcionar:
                    self.funcionar = False
                    self.raton.asignar_posicion(400, 350)  # Slot 1
            case 37:
                self.juego.jugador.slot_seleccionado = 1
                self.juego.mostrar_fondo = True
                self.juego.mostrar_menu_guardado(screen)
                if self.funcionar:
                    self.funcionar = False
                    self.raton.asignar_posicion(530, 550)  # Boton Guardar
            case 38:
                self.juego.jugador.guardar_partida()
            case 39:
                self.juego.mostrar_fondo = True
                self.juego.mostrar_menu_guardado(screen)
                if self.funcionar:
                    self.funcionar = False
                    self.raton.asignar_posicion(650, 350)  # Slot 2
            case 40:
                self.juego.jugador.slot_seleccionado = 2
                self.juego.mostrar_fondo = True
                self.juego.mostrar_menu_guardado(screen)
                if self.funcionar:
                    self.funcionar = False
                    self.raton.asignar_posicion(750, 550)  # Boton Cargar
            case 41:
                self.juego.jugador.cargar_partida()
            case 42:
                self.juego.mostrar_pagina_juego(screen)
            case 43:
                self.juego.mostrar_fondo = True
                self.juego.mostrar_pagina_juego(screen)
                self.juego.mostrar_menu_salida(screen)
                if self.funcionar:
                    self.funcionar = False
                    self.raton.asignar_posicion(635, 485)  # Boton M Guardado
            case 44:
                self.juego.mostrar_fondo = True
                self.juego.mostrar_menu_guardado(screen)
            case 45:
                self.juego.mostrar_fondo = True
                self.juego.mostrar_menu_guardado(screen)
                if self.funcionar:
                    self.funcionar = False
                    self.raton.asignar_posicion(650, 350)  # Slot 2
            case 46:
                self.juego.jugador.slot_seleccionado = 2
                self.juego.mostrar_fondo = True
                self.juego.mostrar_menu_guardado(screen)
                if self.funcionar:
                    self.funcionar = False
                    self.raton.asignar_posicion(980, 560)  # Boton Borrar
            case 47:
                self.juego.jugador.borrar_partida()
            case 48:
                self.juego.mostrar_fondo = True
                self.juego.mostrar_menu_guardado(screen)
                if self.funcionar:
                    self.funcionar = False
                    self.raton.asignar_posicion(400, 350)  # Slot 1
            case 49:
                self.juego.jugador.slot_seleccionado = 1
                self.juego.mostrar_fondo = True
                self.juego.mostrar_menu_guardado(screen)
                if self.funcionar:
                    self.funcionar = False
                    self.raton.asignar_posicion(750, 550)  # Boton Cargar
            case 50:
                self.juego.jugador.cargar_partida()
            case 51:
                self.juego.mostrar_pagina_juego(screen)
            case 52:
                self.juego.mostrar_pagina_juego(screen)
                self.seleccionar_cartas([4, 5, 6], self.juego)
            case 53:
                self.juego.mostrar_pagina_juego(screen)
                self.boton_jugar()
            case 54:
                self.juego.mostrar_pagina_juego(screen)
                self.seleccionar_cartas([1, 2, 3, 4, 6], self.juego)
            case 55:
                self.juego.mostrar_pagina_juego(screen)
                self.boton_descartar()
            case 56:
                self.juego.mostrar_pagina_juego(screen)
                self.seleccionar_cartas([3, 4, 5, 6, 7], self.juego)
            case 57:
                self.juego.mostrar_pagina_juego(screen)
                self.boton_jugar()
            case 58:
                self.abrir_tienda([Comodin("clon"), Comodin("gloton")])
                if self.funcionar:
                    self.funcionar = False
                    self.raton.asignar_posicion(200, 200)
                self.fase = 59
            case 59:
                self.mostrar_tienda(screen)
                self.boton_SR()
            case 60:
                self.guardado.guardar_partida(1, self.guardado_4)
                self.juego.jugador.cargar_partida()
                self.juego.jugador.niveles.es_boss = True
                self.juego.jugador.niveles.color_pantalla = (
                    self.juego.jugador.niveles.colores_boss[2]
                )
                self.juego.jugador.niveles.carta_invalida = 1
                for carta in self.juego.jugador.mazo.cartas:
                    if carta.valor == self.juego.jugador.niveles.carta_invalida:
                        carta.habilitada = False
                for carta in self.juego.jugador.mano:
                    if carta.valor == self.juego.jugador.niveles.carta_invalida:
                        carta.habilitada = False
                self.fase = 61
            case 61:
                self.juego.mostrar_pagina_juego(screen)
                if self.funcionar:
                    self.funcionar = False
                    self.raton.asignar_posicion(500, 500)
            case 62:
                self.juego.mostrar_pagina_juego(screen)
                self.seleccionar_cartas([1, 2], self.juego)
            case 63:
                self.juego.mostrar_pagina_juego(screen)
                self.boton_jugar()
            case 64:
                self.juego.mostrar_pagina_juego(screen)
                self.seleccionar_cartas([0, 6, 7], self.juego)
            case 65:
                self.juego.mostrar_pagina_juego(screen)
                self.boton_jugar()
            case 66:
                self.juego.mostrar_pagina_juego(screen)
                self.seleccionar_cartas([0, 5], self.juego)
            case 67:
                self.juego.mostrar_pagina_juego(screen)
                self.boton_jugar()
            case 68:
                self.juego.mostrar_fondo = True
                self.juego.mostrar_pagina_game_over(screen)
            case 69:
                self.juego.mostrar_fondo = True
                self.juego.mostrar_pagina_game_over(screen)
                self.boton_salir()
            case 70:
                self.juego.mostrar_fondo = True
                self.juego.mostrar_pagina_principal(screen)
            case _:
                self.cargar_guardado_previo()
                self.__init__(self.juego, self.transicion)
                # Cambiar pantalla al menú principal
                self.juego.mostrar_fondo = True
                self.juego.pagina_actual = 0  # <-- Si el menú principal es la página 0. Ajústalo si es otro índice.
                self.juego.reiniciar()
                return

        # Dibujar cursor
        if self.fase != 0:
            self.raton.dibujar(screen)

        # Si la fase es de selección de cartas no avanza
        if self.fase in self.fases_seleccion_cartas:
            return

        # Fases normales avanzar con temporizador
        self.contador += 1
        if self.contador >= self.tiempo_fase.get(self.fase, 60):
            self.contador = 0
            self.fase += 1
            self.funcionar = True

    def boton_jugar(self):
        if self.funcionar:  # Darle al boton de jugar
            self.funcionar = False
            self.raton.asignar_posicion(730, 670)
        if self.raton.checkear_pos():
            self.juego.jugador.jugar_cartas()
            self.fase += 1

    def boton_descartar(self):
        if self.funcionar:  # Darle al boton de descartar
            self.funcionar = False
            self.raton.asignar_posicion(925, 670)
        if self.raton.checkear_pos():
            self.juego.jugador.descartar_cartas("boton")
            self.fase += 1

    def boton_SR(self):
        self.raton.asignar_posicion(460, 300)
        if self.raton.checkear_pos():
            self.cerrar_tienda()
            self.fase += 1

    def boton_comprar(self):
        self.raton.asignar_posicion(460, 525)
        if self.raton.checkear_pos():
            self.juego.tienda.comprar()
            self.fase += 1

    def boton_salir(self):
        self.raton.asignar_posicion(640, 635)
        if self.raton.checkear_pos():
            self.fase += 1

    def seleccionar_cartas(self, cartas: list, juego: Juego):

        # Si no se ha iniciado la selección para esta lista se inicializa
        if not self._seleccionando:
            self._seleccionando = True
            self._cartas_a_seleccionar = list(cartas)
            self.indice_carta = 0
            self.contador = 0
            self.funcionar = False
            return

        # Si se estan seleccionando cartas
        if self.indice_carta < len(self._cartas_a_seleccionar):
            carta_id = self._cartas_a_seleccionar[self.indice_carta]
            # mover cursor hacia la carta actual
            self.raton.asignar_posicion_carta(carta_id)

            # esperar a que el cursor llegue
            if self.raton.checkear_pos():
                carta = juego.jugador.mano[carta_id]
                # marcar selección si no está marcada
                if not getattr(carta, "seleccionada", False):
                    carta.seleccionada = True
                    juego.jugador._cartas_seleccionadas.append(carta)

                self.contador += 1
                if self.contador >= self._pause_frames:
                    self.contador = 0
                    self.indice_carta += 1
        else:

            self._seleccionando = False
            self._cartas_a_seleccionar = []
            self.indice_carta = 0
            self.contador = 0
            self.funcionar = True
            self.fase += 1

    def abrir_tienda(self, comodines):
        self.juego.tienda.tienda_comodines = comodines
        self.juego.mostrar_fondo = True
        Juego.num_transicion = 2
        Juego.paginas_transicion = [self.juego.paginas[1], self.juego.paginas[3], 3]
        self.transicion.iniciar(*Juego.paginas_transicion, Juego.num_transicion)

    def mostrar_tienda(self, screen):
        screen.blit(self.p_juego_tienda, (0, 0))
        self.juego.mostrar_menu_tienda(screen)

    def cerrar_tienda(self):
        self.juego.mostrar_fondo = True
        Juego.num_transicion = 3
        Juego.paginas_transicion = [self.juego.paginas[1], self.juego.paginas[3], 1]
        self.transicion.iniciar(*Juego.paginas_transicion, Juego.num_transicion)

    def cargar_guardado_previo(self):
        for i in range(0, 3):
            if self.guardado_previo[i]:
                self.guardado.guardar_partida(i + 1, self.guardado_previo[i])
            else:
                self.guardado.borrar_partida(i + 1)

    def crear_guardado_previo(self):
        for i in range(1, 4):
            self.guardado_previo.append(self.guardado.cargar_partida(i))
            self.guardado.borrar_partida(i)

    def crear_partidas_customizadas(self):
        self.crear_guardado_previo()

        self.guardado_1 = {
            "puntos": 0,
            "puntos_nivel": 100,
            "nivel": 1,
            "puntos_cartas": 0,
            "multiplicador": 0,
            "dinero": 0,
            "limite_descartar": 3,
            "limite_jugar": 4,
            "comodines": [],
            "mano": [
                [5, "c"],
                [8, "b"],
                [7, "o"],
                [10, "c"],
                [9, "b"],
                [6, "c"],
                [7, "e"],
                [6, "e"],
            ],
            "mazo": [
                [10, "b"],
                [8, "e"],
                [4, "e"],
                [11, "c"],
                [8, "c"],
                [4, "b"],
                [12, "o"],
                [9, "o"],
                [1, "e"],
                [5, "e"],
                [1, "b"],
                [12, "b"],
                [2, "e"],
                [3, "e"],
                [5, "e"],
                [6, "c"],
                [6, "c"],
                [6, "c"],
                [6, "c"],
                [6, "c"],
                [6, "c"],
                [6, "c"],
                [6, "c"],
                [6, "c"],
                [6, "c"],
                [6, "c"],
                [6, "c"],
                [6, "c"],
                [6, "c"],
                [6, "c"],
                [6, "c"],
                [6, "c"],
                [6, "c"],
                [6, "c"],
                [6, "c"],
                [6, "c"],
                [6, "c"],
                [6, "c"],
                [6, "c"],
                [6, "c"],
            ],
            "cartas_jugadas": None,
        }

        self.guardado.guardar_partida(1, self.guardado_1)

        self.guardado_2 = {
            "puntos": 0,
            "puntos_nivel": 250,
            "nivel": 2,
            "puntos_cartas": 0,
            "multiplicador": 0,
            "dinero": 2,
            "limite_descartar": 3,
            "limite_jugar": 4,
            "comodines": [],
            "mano": [
                [4, "o"],
                [11, "e"],
                [10, "o"],
                [6, "e"],
                [7, "e"],
                [8, "o"],
                [5, "o"],
                [8, "c"],
            ],
            "mazo": [
                [9, "o"],
                [2, "c"],
                [6, "o"],
                [12, "c"],
                [10, "b"],
                [6, "c"],
                [2, "e"],
                [9, "c"],
                [2, "b"],
                [8, "b"],
                [1, "b"],
                [12, "b"],
                [2, "e"],
                [3, "e"],
                [5, "e"],
                [6, "c"],
                [6, "c"],
                [6, "c"],
                [6, "c"],
                [6, "c"],
                [6, "c"],
                [6, "c"],
                [6, "c"],
                [6, "c"],
                [6, "c"],
                [6, "c"],
                [6, "c"],
                [6, "c"],
                [6, "c"],
                [6, "c"],
                [6, "c"],
                [6, "c"],
                [6, "c"],
                [6, "c"],
                [6, "c"],
                [6, "c"],
                [6, "c"],
                [6, "c"],
                [6, "c"],
                [6, "c"],
            ],
            "cartas_jugadas": None,
        }

        self.guardado_3 = {
            "puntos": 0,
            "puntos_nivel": 625,
            "nivel": 3,
            "puntos_cartas": 0,
            "multiplicador": 0,
            "dinero": 1,
            "limite_descartar": 3,
            "limite_jugar": 4,
            "comodines": ["calculadora"],
            "mano": [
                [3, "e"],
                [8, "o"],
                [11, "b"],
                [1, "o"],
                [2, "e"],
                [2, "b"],
                [2, "c"],
                [9, "b"],
            ],
            "mazo": [
                [4, "e"],
                [6, "c"],
                [8, "e"],
                [4, "b"],
                [12, "b"],
                [5, "b"],
                [10, "b"],
                [1, "b"],
                [2, "b"],
                [8, "b"],
                [1, "b"],
                [12, "b"],
                [2, "e"],
                [6, "c"],
                [6, "c"],
                [6, "c"],
                [6, "c"],
                [6, "c"],
                [6, "c"],
                [6, "c"],
                [6, "c"],
                [6, "c"],
                [6, "c"],
                [6, "c"],
                [6, "c"],
                [3, "e"],
                [5, "e"],
                [6, "c"],
                [6, "c"],
                [6, "c"],
                [6, "c"],
                [6, "c"],
                [6, "c"],
                [6, "c"],
                [6, "c"],
                [6, "c"],
                [6, "c"],
                [6, "c"],
                [6, "c"],
                [6, "c"],
            ],
            "cartas_jugadas": None,
        }

        self.guardado_4 = {
            "puntos": 0,
            "puntos_nivel": 1564,
            "nivel": 4,
            "puntos_cartas": 0,
            "multiplicador": 0,
            "dinero": 3,
            "limite_descartar": 3,
            "limite_jugar": 4,
            "comodines": ["calculadora"],
            "mano": [
                [4, "o"],
                [1, "e"],
                [1, "o"],
                [6, "e"],
                [7, "e"],
                [10, "o"],
                [5, "o"],
                [8, "c"],
            ],
            "mazo": [
                [4, "b"],
                [4, "c"],
                [6, "o"],
                [1, "c"],
                [10, "b"],
                [6, "c"],
                [2, "e"],
                [9, "c"],
                [2, "b"],
                [8, "b"],
                [1, "b"],
                [12, "b"],
                [2, "e"],
                [6, "c"],
                [6, "c"],
                [6, "c"],
                [6, "c"],
                [6, "c"],
                [6, "c"],
                [6, "c"],
                [6, "c"],
                [6, "c"],
                [6, "c"],
                [6, "c"],
                [6, "c"],
                [3, "e"],
                [5, "e"],
                [6, "c"],
                [6, "c"],
                [6, "c"],
                [6, "c"],
                [6, "c"],
                [6, "c"],
                [6, "c"],
                [6, "c"],
                [6, "c"],
                [6, "c"],
                [6, "c"],
                [6, "c"],
                [6, "c"],
            ],
            "cartas_jugadas": None,
        }

        self.guardado_5 = {
            "puntos": 208,
            "puntos_nivel": 1562,
            "nivel": 5,
            "puntos_cartas": 14,
            "multiplicador": 2,
            "dinero": 2,
            "limite_descartar": 1,
            "limite_jugar": 2,
            "comodines": ["programador", "stonks"],
            "mano": [
                [4, "c"],
                [5, "c"],
                [8, "o"],
                [11, "e"],
                [9, "b"],
                [12, "c"],
                [7, "e"],
                [11, "o"],
            ],
            "mazo": [
                [1, "b"],
                [7, "b"],
                [9, "o"],
                [3, "c"],
                [1, "o"],
                [8, "c"],
                [1, "e"],
                [4, "e"],
                [6, "c"],
                [4, "o"],
                [11, "c"],
                [8, "b"],
                [4, "b"],
                [9, "e"],
                [1, "c"],
                [11, "b"],
                [3, "e"],
                [2, "o"],
                [6, "b"],
                [6, "e"],
                [9, "c"],
                [5, "o"],
                [10, "e"],
                [12, "e"],
                [12, "o"],
            ],
            "cartas_jugadas": [[2, "e"], [2, "c"]],
            "fecha": "06.11.25   23:49",
        }


class Cursor:
    def __init__(self, x, y):
        self.imagen = pygame.image.load(
            "Graficos/cursor.png"
        ).convert_alpha()  # Carga la imagen
        self.x = x
        self.y = y
        self.x_final = self.x
        self.y_final = self.y
        self.velocidad = 0.2

    def asignar_posicion_carta(self, carta: int):
        self.x_final = 570 + 75 * (carta)
        self.y_final = 560

    def asignar_posicion(self, posx, posy):
        self.x_final = posx
        self.y_final = posy

    def checkear_pos(self):
        dx = self.x_final - self.x
        dy = self.y_final - self.y
        dist2 = dx * dx + dy * dy
        return dist2 <= (3 * 3)

    def dibujar(self, screen):
        self._mover_hacia_destino()
        screen.blit(self.imagen, (self.x, self.y))

    def _mover_hacia_destino(self):
        self.x += (self.x_final - self.x) * self.velocidad
        self.y += (self.y_final - self.y) * self.velocidad
