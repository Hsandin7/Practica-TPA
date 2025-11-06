from src.juego import Juego
from src.animaciones import Transicion
from src.tienda import Tienda
from src.comodines import Comodin
from src.guardado import *
from src._utilidades import *

# Pos boton jugar = (730, 670)
# Pos boton descartar = (925, 670)

class Demo:
    def __init__(self):
        self.activa = False
        self.fase = 1
        self.contador = 0
        self.funcionar = True
        self.raton = Cursor(1280/2, 720/2)
        self.guardado = Guardado()
        self.comodin = Comodin("calculadora")
    
    def checkear_inicio(self):
        self.contador += 1
        if self.contador > 5*60:   # 2s x 60fps para esperar en total 2s
            self.activa = True
            self.crear_partidas_customizadas()
            self.contador = 0

    def checkear_siguiente(self, eventos):
        for event in eventos:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
                print(f"Fase: {self.fase}")
                self.fase += 1
                self.funcionar = True
                self.contador = 0

    def ejecutar_demo(self, screen, juego: Juego, transicion: Transicion, eventos):
        self.checkear_siguiente(eventos)
        # Ir a pagina de Juego
        match self.fase:
            case 1:
                juego.mostrar_fondo = True
                Juego.num_transicion = 1
                Juego.paginas_transicion = [juego.paginas[0], juego.paginas[1], 1]
                transicion.iniciar( Juego.paginas_transicion[0],Juego.paginas_transicion[1],Juego.paginas_transicion[2],Juego.num_transicion)
                
                # Cargar guardado 1
                juego.jugador.slot_seleccionado = 1
                juego.jugador.cargar_partida()
                self.fase += 1
            case 2:
                juego.mostrar_pagina_juego(screen)
            case 3:
                juego.mostrar_pagina_juego(screen)
                if self.funcionar:
                    self.funcionar = False
                    self.raton.asignar_posicion(410, 355)
            case 4:     # Mostrar info
                juego.mostrar_pantalla_info(screen)
            case 5:
                juego.mostrar_pagina_juego(screen)
            case 6:
                juego.mostrar_pagina_juego(screen)
                self.seleccionar_cartas([2, 5, 6, 7], juego)
            case 7:
                juego.mostrar_pagina_juego(screen)
                self.boton_jugar(juego)
            case 8:
                juego.mostrar_pagina_juego(screen)
                self.seleccionar_cartas([0, 2, 5, 6, 7], juego)
            case 9:
                juego.mostrar_pagina_juego(screen)
                self.boton_descartar(juego)
            case 10:
                juego.mostrar_pagina_juego(screen)
                self.seleccionar_cartas([3, 5, 6, 7], juego)
            case 11:
                juego.mostrar_pagina_juego(screen)
                self.boton_descartar(juego)
            case 12:
                juego.mostrar_pagina_juego(screen)
                self.seleccionar_cartas([0, 1, 2, 3, 5], juego)
            case 13:
                juego.mostrar_pagina_juego(screen)
                self.boton_jugar(juego)
            case 14:
                juego.mostrar_pagina_juego(screen)
                self.boton_jugar(juego)
            case 15:
                juego.tienda.comodines_disponibles = [
                    "esteroides", 
                    "gloton"
                ]

                juego.tienda.poblar()

                if self.funcionar:
                    self.funcionar = False
                    self.raton.asignar_posicion(200, 200)

                self.fase = 16

            case 16:
                juego.mostrar_pagina_juego(screen)
                juego.mostrar_menu_tienda(screen)
                self.boton_SR()
            case 17:
                self.guardado.guardar_partida(1, self.guardado_2)
                juego.jugador.cargar_partida()
            case 18:
                juego.mostrar_pagina_juego(screen)
                if self.funcionar:
                    self.funcionar = False
                    self.raton.asignar_posicion(410, 355)
            case 19:
                juego.mostrar_pagina_juego(screen)
                self.seleccionar_cartas([5, 7], juego)
            case 20:
                juego.mostrar_pagina_juego(screen)
                self.boton_jugar(juego)
            case 21:
                juego.mostrar_pagina_juego(screen)
                self.seleccionar_cartas([1, 2, 6, 7], juego)
            case 22:
                juego.mostrar_pagina_juego(screen)
                self.boton_descartar(juego)
            case 23:
                juego.mostrar_pagina_juego(screen)
                self.seleccionar_cartas([4, 5, 6, 7], juego)
            case 24:
                juego.mostrar_pagina_juego(screen)
                self.boton_descartar(juego)
            case 25:
                juego.mostrar_pagina_juego(screen)
                self.seleccionar_cartas([0, 1, 2, 3, 7], juego)
            case 26:
                juego.mostrar_pagina_juego(screen)
                self.boton_jugar(juego)
            case 27:
                juego.tienda.comodines_disponibles = [
                    "calculadora", 
                    "loco"
                ]

                juego.tienda.poblar()

                if self.funcionar:
                    self.funcionar = False
                    self.raton.asignar_posicion(200, 200)

                self.fase = 28

            case 28:
                juego.mostrar_pagina_juego(screen)
                juego.mostrar_menu_tienda(screen)
            case 29:
                juego.mostrar_pagina_juego(screen)
                juego.mostrar_menu_tienda(screen)
                self.raton.asignar_posicion(self.comodin.x, self.comodin.y)
            case 30:
                juego.mostrar_pagina_juego(screen)
                juego.mostrar_menu_tienda(screen)
                self.boton_comprar()
            case 31:
                juego.mostrar_pagina_juego(screen)
                juego.mostrar_menu_tienda(screen)
                self.boton_SR()
                juego.jugador.comodines_mano = [Comodin("calculadora")]
            case 32:
                self.guardado.guardar_partida(1, self.guardado_3)
                juego.jugador.cargar_partida()
            case 33:
                juego.mostrar_pagina_juego(screen)
                if self.funcionar:
                    self.funcionar = False
                    self.raton.asignar_posicion(410, 355)
        if self.fase is not 0: self.raton.dibujar(screen)


    def boton_jugar(self, juego: Juego):
        if self.funcionar:          # Darle al boton de jugar
            self.funcionar = False
            self.raton.asignar_posicion(730, 670)
        if self.raton.checkear_pos():
            juego.jugador.jugar_cartas()
            self.fase +=1

    def boton_descartar(self, juego: Juego):
        if self.funcionar:          # Darle al boton de jugar
            self.funcionar = False
            self.raton.asignar_posicion(925, 670)
        if self.raton.checkear_pos():
            juego.jugador.descartar_cartas("boton")
            self.fase +=1

    def boton_SR(self):
        self.raton.asignar_posicion(460, 300)
        if self.raton.checkear_pos():
            self.fase +=1

    def boton_comprar(self):
        self.raton.asignar_posicion(460, 525)
        if self.raton.checkear_pos():
            self.fase +=1

    def seleccionar_cartas(self, cartas: list, juego: Juego):
        if self.raton.checkear_pos() and self.contador < len(cartas):
            self.raton.asignar_posicion_carta(cartas[self.contador])
            juego.jugador.mano[cartas[self.contador]].seleccionada = True
            juego.jugador._cartas_seleccionadas.append(juego.jugador.mano[cartas[self.contador]])
            self.contador += 1

    def crear_partidas_customizadas(self):
        self.guardado_1 = {
            "puntos":           0,
            "puntos_nivel":     100,
            "nivel":            1,
            "puntos_cartas":    0,
            "multiplicador":    0,
            "dinero":           0,

            "limite_descartar": 3,
            "limite_jugar":     4,

            "comodines":        None,
            "mano":             [[5,"c"], [8,"b"], [7,"o"], [10,"c"], [9,"b"], [6,"c"], [7,"e"], [6,"e"]],
            "mazo":             [[10,"b"], [8,"e"], [4,"e"], [11,"c"],     [8,"c"], [4,"b"], [12,"o"], [9,"o"], [1,"e"] ,[5, "e"], [1, "b"], [12, "b"], [2, "e"], 
                                 [3, "e"], [5, "e"], [6, "c"], [6, "c"], [6, "c"], [6, "c"], [6, "c"], [6, "c"],],
            "cartas_jugadas":   None
        }

        self.guardado.guardar_partida(1, self.guardado_1)

        self.guardado_2 = {
            "puntos":           0,
            "puntos_nivel":     250,
            "nivel":            2,
            "puntos_cartas":    0,
            "multiplicador":    0,
            "dinero":           2,

            "limite_descartar": 3,
            "limite_jugar":     4,

            "comodines":        None,
            "mano":             [[4,"o"], [11,"e"], [10,"o"], [6,"e"], [7,"e"], [8,"o"], [5,"o"], [8,"c"]],
            "mazo":             [[9,"o"], [2,"c"],     [6,"o"], [12,"c"], [10,"b"], [6,"c"],     [2,"e"], [9,"c"], [2,"b"] ,[8, "b"], 
                                 [1, "b"], [12, "b"], [2, "e"], 
                                 [3, "e"], [5, "e"], [6, "c"], [6, "c"], [6, "c"], [6, "c"], [6, "c"], [6, "c"],],
            "cartas_jugadas":   None
        }

        self.guardado_3 = {
            "puntos":           0,
            "puntos_nivel":     625,
            "nivel":            2,
            "puntos_cartas":    0,
            "multiplicador":    0,
            "dinero":           4,

            "limite_descartar": 3,
            "limite_jugar":     4,

            "comodines":        ["calculadora"],
            "mano":             [[4,"o"], [11,"e"], [10,"o"], [6,"e"], [7,"e"], [8,"o"], [5,"o"], [8,"c"]],
            "mazo":             [[9,"o"], [2,"c"],     [6,"o"], [12,"c"], [10,"b"], [6,"c"],     [2,"e"], [9,"c"], [2,"b"] ,[8, "b"], 
                                 [1, "b"], [12, "b"], [2, "e"], 
                                 [3, "e"], [5, "e"], [6, "c"], [6, "c"], [6, "c"], [6, "c"], [6, "c"], [6, "c"],],
            "cartas_jugadas":   None
        }

class Cursor:
    def __init__(self, x, y):
        self.imagen = pygame.image.load("Graficos/cursor.png").convert_alpha()   # Carga la imagen
        self.x = x
        self.y = y
        self.x_final = self.x
        self.y_final = self.y
        self.velocidad = 0.2
    
    def asignar_posicion_carta(self, carta: int):
        self.x_final = 590 + 90*(carta-1)
        self.y_final = 560

    def asignar_posicion(self, posx, posy):
        self.x_final = posx
        self.y_final = posy
    
    def checkear_pos(self):
        if self.x_final-1 <= self.x <= self.x_final+1 and self.y_final-1 <= self.y <= self.y_final+1:
            return True
        else:
            return False

    def dibujar(self, screen):
        self._mover_hacia_destino()
        screen.blit(self.imagen, (self.x, self.y))

    def _mover_hacia_destino(self):
        self.x += (self.x_final - self.x) * self.velocidad
        self.y += (self.y_final - self.y) * self.velocidad