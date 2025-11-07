import random
import pygame
from src.jugador import Jugador
from src.comodines import Comodin
from src._utilidades import (
    mostrar_texto,
    mostrar_texto_centrado,
    mostrar_texto_multilinea,
)


class Tienda:
    """Clase Tienda: Hace toda la funcionalidad de la tienda.
    Inicializa los atributos:
    - Los comodines disponibles en la tienda, ademas de que los muestra.
    - Esta la funcion de cambiar de comodines y comprar.
    - Se resta del dinero el precio del comodin.
    """

    def __init__(self, jugador: Jugador):
        self.jugador = jugador
        self.comodines_disponibles = [
            "gloton",
            "stonks",
            "matematico",
            "calculadora",
            "loco",
            "doblete",
            "esteroides",
            "programador",
            "clon",
        ]
        self.coste_cambiar = 2
        self.tienda_comodines = [None, None]
        self.comodin_seleccionado = None
        self.poblar()
        self.imagen_descripcion = pygame.image.load(
            "Graficos/descripcion_comodines_tienda.png"
        )

    def poblar(self):
        """
        La funcion poblar tienda sirve para mostrar los comodines que puede comprar en la tienda,
        y que con el random hace que no se puedan repetir un mismo comodin en la tienda.
        """
        n = min(2, len(self.comodines_disponibles))
        nombres = random.sample(
            self.comodines_disponibles, n
        )  # Elige dos o menos comodines en funcion de los que haya disponibles

        while len(nombres) < 2:
            nombres.append(None)

        for i in range(2):
            self.tienda_comodines[i] = Comodin(nombres[i])

        # Deseleccionar cualquier comodín anterior
        self.comodin_seleccionado = None

    def mostrar(self, screen):
        """
        La funcion mostrar, muestra la informacion del precio de los comodines y el dinero del juegador.
        """
        mostrar_texto_centrado(
            screen, f"{self.jugador.dinero}$", 900, 150, 40
        )  # Mostrar dinero actual del jugador

        color_coste = (
            (255, 255, 0) if self.jugador.dinero >= self.coste_cambiar else (255, 0, 0)
        )  # Amarillo si se puede pagar Rojo si no
        mostrar_texto(screen, f"{self.coste_cambiar}$", 525, 400, 30, color_coste)
        x = 690
        y = 250
        for comodin in self.tienda_comodines:
            if comodin:
                comodin.asignar_posicion(x, y)
                comodin.dibujar(screen)
                color_precio = (
                    (255, 255, 0)
                    if self.jugador.dinero >= comodin.precio
                    else (255, 0, 0)
                )  # Amarillo si se puede pagar Rojo si no
                mostrar_texto_centrado(
                    screen,
                    f"{comodin.precio}$",
                    comodin.rect.midbottom[0],
                    comodin.rect.bottom + 3,
                    20,
                    color_precio,
                )
                if comodin.seleccionada:
                    screen.blit(comodin.imagen_hover, (comodin.x, comodin.y))

                    # Mostrar descripcion
                    screen.blit(self.imagen_descripcion, (0, 0))
                    gris = (220, 220, 220)
                    mostrar_texto(
                        screen,
                        f"{self.comodin_seleccionado.nombre.capitalize()}",
                        670,
                        438,
                        30,
                    )
                    color_rareza = {
                        "comun": (245, 245, 245),
                        "raro": (170, 235, 145),
                        "epico": (170, 50, 255),
                    }
                    mostrar_texto_centrado(
                        screen,
                        f"{self.comodin_seleccionado.rareza.capitalize()}",
                        920,
                        445,
                        20,
                        color_rareza[self.comodin_seleccionado.rareza],
                    )
                    mostrar_texto_multilinea(
                        screen,
                        f"{self.comodin_seleccionado.descripcion}",
                        670,
                        480,
                        20,
                        gris,
                        290,
                    )
            x += 150

    def actualizar(self, eventos):
        """
        Devuelve si un comodin esta seleccionado o no.
        """
        # Selección de comodines
        for comodin in self.tienda_comodines:
            if comodin and comodin.detectar_seleccion(eventos):
                if comodin.seleccionada:
                    comodin.seleccionada = False
                    self.comodin_seleccionado = None
                else:
                    for c in self.tienda_comodines:
                        if c:
                            c.seleccionada = False
                    comodin.seleccionada = True
                    self.comodin_seleccionado = comodin

    def cambiar(self):
        """
        Funcion del boton cambiar.
        """
        # Botón "Cambiar"
        if self.jugador.dinero >= self.coste_cambiar:
            self.jugador.dinero -= self.coste_cambiar
            self.coste_cambiar += 2
            self.poblar()

    def comprar(self):
        """
        Funcion del boton comprar.
        """
        # Botón "Comprar"
        if (
            self.comodin_seleccionado
            and self.jugador.dinero >= self.comodin_seleccionado.precio
            and len(self.jugador.comodines_mano) < 5
        ):
            self.jugador.dinero -= self.comodin_seleccionado.precio
            self.jugador.comodines_mano.append(self.comodin_seleccionado)
            idx = self.tienda_comodines.index(self.comodin_seleccionado)
            self.tienda_comodines[idx] = None
            self.comodines_disponibles.remove(self.comodin_seleccionado.nombre)
            self.comodin_seleccionado = None
