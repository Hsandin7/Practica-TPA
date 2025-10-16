# Encapsula todo lo relacionado con la mano, el mazo y las acciones del jugador

import pygame
from Clases.mazo import Mazo
from Clases.evaluador_cartas import Evaluador_Cartas
from Clases._utilidades import mostrar_texto, mostrar_texto_centrado

from Clases.carta import Carta

class Jugador:
    def __init__(self):
        self.puntos = 0
        self.puntos_cartas = 0
        self.multiplicador = 0
        self.mazo = Mazo()
        self._mano = [self.mazo.robar() for _ in range(0,8)]
        self._cartas_jugadas = list()
        self._limite_seleccion = 5        

    
    def mostrar_puntos(self, screen):
        puntos_formateados = f"{self.puntos:,}".replace(",", ".")
        mostrar_texto_centrado(screen, puntos_formateados, 900, 125, 50)
        mostrar_texto_centrado(screen, f"{self.multiplicador}", 950, 190)
        mostrar_texto_centrado(screen, f"{self.puntos_cartas}", 845, 190)
        
        puntos_formateados = f"{self.puntos:,}".replace(",", ".")       # Cambiar por el objetivo de puntos
        mostrar_texto_centrado(screen, puntos_formateados, 400, 125, 50)

    def mostrar_mano(self, screen):      
        pos_x = 535
        for carta in self._mano:
            carta.x_final = pos_x
            if carta.seleccionada:
                carta.y_final = 450
            else:
                carta.y_final = 500
            carta.dibujar(screen)
            
            pos_x += 75
        
        if self._cartas_jugadas is not []:
            pos_x = 850 - float( (len(self._cartas_jugadas)-1) / 2 ) * 100          # Posicion inicial
            for carta in self._cartas_jugadas:
                carta.x_final = pos_x
                carta.y_final = 300
                carta.dibujar(screen)
                pos_x += 100
        
        mostrar_texto(screen, f"{len([carta for carta in self._mano if carta.seleccionada])}/5", 1170, 500, 20)


    def actualizar(self, eventos):
        for carta in self._mano:
            carta.detectar_seleccion(eventos)
        for carta in self._cartas_jugadas:
            carta.detectar_seleccion(eventos)

    def jugar_cartas(self):
        seleccionadas = [carta for carta in self._mano if carta.seleccionada]
        if len(seleccionadas) <= self._limite_seleccion:
            if seleccionadas is not []:        # Comprueba que haya cartas seleccionadas
                evaluador = Evaluador_Cartas(seleccionadas)
                evaluacion = evaluador.evaluar()
                self._cartas_jugadas = evaluacion["Cartas"]
                self.puntos_cartas = evaluacion["Valor"]
                self.multiplicador = evaluacion["Multiplicador"]
                self.puntos += self.puntos_cartas * self.multiplicador
                print(evaluacion)      # Para debugging pero se tendrá que reemplazar con algo que use el resultado
                print(self._cartas_jugadas)
                self.descartar_cartas()         # Una vez jugadas se descartan

    def descartar_cartas(self):
        seleccionadas = [carta for carta in self._mano if carta.seleccionada]
        if len(seleccionadas) <= self._limite_seleccion:
            for carta in seleccionadas:
                self._mano.remove(carta)
            while len(self._mano) is not 8:
                self._mano.append(self.mazo.robar())