from Clases.juego import Juego
from Clases.animaciones import Transicion
from Clases.guardado import *
from Clases._utilidades import *

# Pos boton jugar = (730, 670)
# Pos boton descartar = (925, 670)

class Demo:
    def __init__(self):
        self.activa = False
        self.fase = 1
        self.contador = 0
        self.funcionar = True
        self.raton = Cursor(1280/2, 720/2)
    
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
                self.seleccionar_cartas([3, 4, 5, 6], juego)
            case 7:
                juego.mostrar_pagina_juego(screen)
                self.boton_jugar(juego)
            case 8:
                juego.mostrar_pagina_juego(screen)
                self.seleccionar_cartas([1, 2, 3, 6, 7], juego)
            case 9:
                juego.mostrar_pagina_juego(screen)
                self.boton_jugar(juego)
                juego.comprobar_exito()
                transicion.iniciar( Juego.paginas_transicion[0],Juego.paginas_transicion[1],Juego.paginas_transicion[2],Juego.num_transicion)
                if Juego.num_transicion:
                    self.fase += 1



        if self.fase is not 0: self.raton.dibujar(screen)


    def boton_jugar(self, juego: Juego):
        if self.funcionar:          # Darle al boton de jugar
            self.funcionar = False
            self.raton.asignar_posicion(730, 670)
        if self.raton.checkear_pos():
            juego.jugador.jugar_cartas()
    def seleccionar_cartas(self, cartas: list, juego: Juego):
        if self.raton.checkear_pos() and self.contador < len(cartas):
            self.raton.asignar_posicion_carta(cartas[self.contador])
            juego.jugador.mano[cartas[self.contador]].seleccionada = True
            juego.jugador._cartas_seleccionadas.append(juego.jugador.mano[cartas[self.contador]])
            self.contador += 1

    def crear_partidas_customizadas(self):
        self.guardado_1 = {
            "puntos":           0,
            "puntos_nivel":     100000,
            "nivel":            1,
            "puntos_cartas":    0,
            "multiplicador":    0,

            "limite_descartar": 3,
            "limite_jugar":     4,

            "mano":             [[12,"b"], [8,"b"], [9,"b"], [5,"e"], [4,"o"], [4,"b"], [5,"o"], [11,"e"]],
            "mazo":             [[3,"b"], [5,"b"], [10,"c"], [12,"o"],     [10,"e"], [10,"e"], [10,"e"], [10,"e"], [10,"e"], [10,"e"], [10,"e"], [10,"e"]],
            "cartas_jugadas":   None
        }
        guardar_partida(1, self.guardado_1)








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