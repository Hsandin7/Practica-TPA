# Encapsula todo lo relacionado con la mano, el mazo y las acciones del jugador

import pygame
from Clases.mazo import Mazo
from Clases.carta import Carta
from Clases.evaluador_cartas import Evaluador_Cartas
from Clases._utilidades import *
from Clases.animaciones import Animador_Texto
from Clases.guardado import *

class Jugador:
    def __init__(self):
        self.puntos = 0
        self.puntos_cartas = 0
        self.multiplicador = 0
        self.slot_seleccionado = 0
        
        self.evaluador =        Evaluador_Cartas()
        self.animador_texto =   Animador_Texto()
        self.mazo =             Mazo()
        
        self.mano = [self.mazo.robar() for _ in range(0,8)]
        
        self._cartas_seleccionadas =    list()
        self._cartas_jugadas =          list()
        self._cartas_descartadas =      list()
        
        self.limite_seleccion = 5
        self.limite_jugar = 4
        self.limite_descartar = 3
        inicializar_archivo_guardado()

    
    def mostrar_puntos(self, screen):
        puntos_formateados = f"{self.puntos:,}".replace(",", ".")
        mostrar_texto_centrado(screen, puntos_formateados, 900, 125, 50)
        mostrar_texto_centrado(screen, f"{self.multiplicador}", 950, 190)
        mostrar_texto_centrado(screen, f"{self.puntos_cartas}", 845, 190)
        
        # Cambiar por el objetivo de puntos del nivel
        puntos_formateados = f"{self.puntos:,}".replace(",", ".")
        mostrar_texto_centrado(screen, puntos_formateados, 400, 125, 50)

        # Muestra los puntos obtenidos que se suman al total
        self.animador_texto.dibujar(screen)


    def mostrar_cartas(self, screen):
        # Mostrar cartas de la mano / Animacion de seleccion de carta
        pos_x = 535
        for carta in self.mano:
            carta.x_final = pos_x
            if carta.seleccionada:
                carta.y_final = 450
            else:
                carta.y_final = 500
            carta.dibujar(screen)
            
            pos_x += 75

        # Animacion para las cartas jugadas
        if self._cartas_jugadas:
            pos_x = 850 - float( (len(self._cartas_jugadas)-1) / 2 ) * 100
            for carta in self._cartas_jugadas:
                carta.x_final = pos_x
                carta.y_final = 300
                carta.dibujar(screen)
                pos_x += 100
    
        # Animacion para las cartas descartadas
        if self._cartas_descartadas:
            for carta in self._cartas_descartadas:
                carta.x_final = screen.get_width()+1
                carta.y_final = 350
                carta.dibujar(screen)
        
        # Mostrar num de cartas seleccionadas
        mostrar_texto(screen, f"{len(self._cartas_seleccionadas)}/5", 1170, 500, 20)

        # Temporal?
        mostrar_texto_centrado(screen, f"{len(self.mazo.cartas)}", 1230, 600, 50)


    def actualizar(self, eventos):      # Comprueba si alguna carta es seleccionada, si esto se cumple, se anade a self._cartas_seleccionadas
        for carta in self.mano:
            match carta.detectar_seleccion(eventos):
                case True:
                    self._cartas_seleccionadas.append(carta)
                case False:
                    self._cartas_seleccionadas.remove(carta)
                case _:
                    continue
            

    def jugar_cartas(self):
        if len(self._cartas_seleccionadas) <= self.limite_seleccion and self._cartas_seleccionadas:    # Comprueba que haya cartas seleccionadas
            self.limite_jugar -= 1
            evaluacion = self.evaluador.evaluar(self._cartas_seleccionadas)
            self._cartas_jugadas = evaluacion["Cartas"]
            self.puntos_cartas = evaluacion["Valor"]
            self.multiplicador = evaluacion["Multiplicador"]
            self.puntos += self.puntos_cartas * self.multiplicador
            
            # print(evaluacion)      # Para debugging
            # print(self._cartas_jugadas)
            
            for carta in self._cartas_jugadas:      # Quita las cartas que se hayan jugado para que el resto se descarte correctamente
                self.mano.remove(carta)
                self._cartas_seleccionadas.remove(carta)
            self.descartar_cartas()                 # Las cartas que no se hayan jugado se descartan
            self.animador_texto.iniciar(f"{self.puntos_cartas * self.multiplicador}", 1100, 150,y_final=90)

    def descartar_cartas(self):
        self._cartas_descartadas.clear()
        if len(self._cartas_seleccionadas) <= self.limite_seleccion and self._cartas_seleccionadas:
            for carta in self._cartas_seleccionadas:
                self._cartas_descartadas.append(carta)
                self.mano.remove(carta)
            self._cartas_seleccionadas.clear()
        while len(self.mano) is not 8:
            self.mano.append(self.mazo.robar())


    # Manjo de partidas guardadas
    def guardar_partida(self):
        # mazo y mano se guardan como listas de strings con el valor y el palo concatenados
        datos = {
            "puntos":           self.puntos,
            "puntos_cartas":    self.puntos_cartas,
            "multiplicador":    self.multiplicador,
            "mazo":             [[c._valor, c._palo] for c in self.mazo.cartas],
            "mano":             [[c._valor, c._palo] for c in self.mano],
            "cartas_jugadas":   [[c._valor, c._palo] for c in self._cartas_jugadas]
        }
        guardar_partida(self.slot_seleccionado, datos)
    
    def cargar_partida(self):
        datos = cargar_partida(self.slot_seleccionado)
        if datos:
            self.puntos =           datos["puntos"]
            self.puntos_cartas =    datos["puntos_cartas"]
            self.multiplicador =    datos["multiplicador"]
            self.mazo.cartas =      [Carta(c[0], c[1]) for c in datos["mazo"]]
            self.mano =             [Carta(c[0], c[1]) for c in datos["mano"]]
            self._cartas_jugadas =  [Carta(c[0], c[1]) for c in datos["cartas_jugadas"]]
            return True
        else:
            return None
    
    def borrar_partida(self):
        borrar_partida(self.slot_seleccionado)
    
    def mostrar_info_slots(self, screen):
        x = 300
        for slot in range(1, 4):
            datos = cargar_partida(slot)
            mostrar_texto(screen, f"Guardado {slot}", x, 170, 30)
            if datos:
                mostrar_texto(screen, f"Puntos: {datos["puntos"]}", x, 215, 20)
                # Cambiar por informacion diferente
                mostrar_texto(screen, f"Puntos: {datos["puntos"]}", x, 245, 20)
                mostrar_texto(screen, f"Puntos: {datos["puntos"]}", x, 275, 20)
                mostrar_texto(screen, f"Puntos: {datos["puntos"]}", x, 305, 20)
            else:
                mostrar_texto(screen, "Vacio", x, 215, 20)
            x += 250