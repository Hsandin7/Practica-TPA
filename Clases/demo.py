from Clases.juego import Juego
from Clases.animaciones import Transicion
from Clases.guardado import *
from Clases._utilidades import *


class Demo:
    def __init__(self):
        self.activa = False
        self.contador = 0
        self.funcionar = True
    
    def checkear_inicio(self, pag_actual):
        if pag_actual == 0:
            self.contador += 1
        else:
            self.contador = 0
        
        if self.contador > 2*60:   # 30s x 60fps para esperar en total 30s
            self.activa = True
            self.crear_partidas_customizadas()
            self.contador = 0

    def ejecutar_demo(self, screen, juego: Juego, transicion: Transicion):
        self.contador += 1
        if self.contador % 60 == 0: print(self.contador/60)
        
        # Ir a pagina de Juego
        if self.contador <= 1:
            if self.funcionar:
                self.funcionar = False
                juego.mostrar_fondo = True
                Juego.num_transicion = 1        # Transicion 1
                Juego.paginas_transicion = [juego.paginas[0], juego.paginas[1], 1]
                transicion.iniciar( Juego.paginas_transicion[0],
                                    Juego.paginas_transicion[1],
                                    Juego.paginas_transicion[2],
                                    Juego.num_transicion)
                
                # Cargar guardado 1
                juego.jugador.slot_seleccionado = 1
                juego.jugador.cargar_partida()

        # Mostrar info
        elif self.contador < 30*60:
            juego.mostrar_pagina_juego(screen)
            mostrar_texto(screen,"Pagina de informacion")


        # Seleccionar cartas
        elif self.contador < 250*60:
            if self.funcionar:
                pass
    



    def crear_partidas_customizadas(self):
        self.guardado_1 = {
            "puntos":           0,
            "puntos_nivel":     100000,
            "nivel":            1,
            "puntos_cartas":    0,
            "multiplicador":    0,

            "limite_descartar": 3,
            "limite_jugar":     4,

            "mano":             [[1,"o"], [2,"o"], [3,"o"], [4,"o"], [5,"o"], [6,"o"], [7,"o"], [8,"o"]],
            "mazo":             [[10,"e"], [10,"e"], [10,"e"], [10,"e"], [10,"e"], [10,"e"], [10,"e"], [10,"e"], [10,"e"], [10,"e"], [10,"e"], [10,"e"]],
            "cartas_jugadas":   None
        }
        guardar_partida(1, self.guardado_1)








class cursor:
    def __init__(self, x, y):
        self.imagen = pygame.image.load("Graficos/cursor.png").convert_alpha()   # Carga la imagen
        self.x = x
        self.y = y
        self.x_final = self.x
        self.y_final = self.y
        self.velocidad = 0.2
    
    def _mover_hacia_destino(self):
        x = self.x
        y = self.y
        x += (self.x_final - self.x) * self.velocidad
        y += (self.y_final - self.y) * self.velocidad
        self._asignar_posicion(x, y)
    
    def _asignar_posicion(self, posx, posy):
        self.x = posx
        self.y = posy

    def dibujar(self, screen):
        self._mover_hacia_destino()
        screen.blit(self.imagen, (self.x, self.y))
