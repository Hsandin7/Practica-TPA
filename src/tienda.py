import random
import pygame
from src.jugador import Jugador
from src.comodines import Comodin
from src._utilidades import mostrar_texto, mostrar_texto_centrado

class Tienda:
    def __init__(self, jugador: Jugador):
        self.jugador = jugador
        self.comodines_disponibles = [
            "gloton", "stonks", "matematico", "calculadora", "loco",
            "doblete", "esteroides", "programador", "clon"
        ]
        self.coste_cambiar = 2
        self.tienda_comodines = [None, None]
        self.comodin_seleccionado = None
        self.poblar()

    def poblar(self):
        pos_slot_1 = (690, 250)
        pos_slot_2 = (840, 250)

        nombres = random.sample(self.comodines_disponibles, 2)
        self.tienda_comodines[0] = Comodin(nombres[0])
        self.tienda_comodines[0].asignar_posicion(*pos_slot_1)
        
        self.tienda_comodines[1] = Comodin(nombres[1])
        self.tienda_comodines[1].asignar_posicion(*pos_slot_2)

        # Deseleccionar cualquier comodín anterior
        self.comodin_seleccionado = None

    def mostrar(self, screen):
        mostrar_texto_centrado(screen, f"{self.jugador.dinero}$", 900, 150, 40)     # Mostrar dinero actual del jugador
        
        color_coste = (255, 255, 0) if self.jugador.dinero >= self.coste_cambiar else (255, 0, 0)   # Amarillo si se puede pagar Rojo si no
        mostrar_texto(screen, f"{self.coste_cambiar}$", 525, 400 , 30, color_coste)

        for comodin in self.tienda_comodines:
            if comodin:
                comodin.dibujar(screen)
                color_precio = (255, 255, 0) if self.jugador.dinero >= comodin.precio else (255, 0, 0)      # Amarillo si se puede pagar Rojo si no
                mostrar_texto_centrado(screen, f"{comodin.precio}$", comodin.rect.midbottom[0], comodin.rect.bottom + 3, 20, color_precio)
                if comodin.seleccionada:
                    screen.blit(comodin.imagen_hover, (comodin.x, comodin.y))

    def actualizar(self, eventos):
        # Selección de comodines
        for comodin in self.tienda_comodines:
            if comodin and comodin.detectar_seleccion(eventos):
                if comodin.seleccionada:
                    comodin.seleccionada = False
                    self.comodin_seleccionado = None
                else:
                    for c in self.tienda_comodines:
                        if c: c.seleccionada = False
                    comodin.seleccionada = True
                    self.comodin_seleccionado = comodin

    def cambiar(self):
        # Botón "Cambiar"
        if self.jugador.dinero >= self.coste_cambiar:
            self.jugador.dinero -= self.coste_cambiar
            self.coste_cambiar += 2
            self.poblar()

    def comprar(self):
        # Botón "Comprar"
        if self.comodin_seleccionado and self.jugador.dinero >= self.comodin_seleccionado.precio and len(self.jugador.comodines_mano) < 5:
            self.jugador.dinero -= self.comodin_seleccionado.precio
            self.jugador.comodines_mano.append(self.comodin_seleccionado)
            idx = self.tienda_comodines.index(self.comodin_seleccionado)
            self.tienda_comodines[idx] = None
            self.comodin_seleccionado = None