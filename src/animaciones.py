import pygame
from src._utilidades import Texto
import random


class Transicion:
    """
    Clase Transicion: Contiene las transiciones de pantalla del juego.
    """

    def __init__(self):
        self.valor = 0  # Un valor estandar para poder crear animaciones progresivas
        self.fase = ""  # expandir , contraer
        self.paginas = [None, None]
        self.num_pagina_destino = 0
        self.angulo = 0
        self.animacion = 0

    def iniciar(
        self, pagina_actual, pagina_destino, num_pagina_destino, num_transicion
    ):
        """
        Funcion Iniciar: Configura la animacion que se va a ejecutar.
        """
        self.paginas = [pagina_actual.copy(), pagina_destino.copy()]
        for pag in self.paginas:
            pag.convert_alpha()
        self.num_pagina_destino = num_pagina_destino
        self.animacion = num_transicion
        match num_transicion:
            case 1:
                self.fase = "expandir"
                self.valor = 0
            case 2:
                self.fase = "bajar"
                self.valor = 0
            case 3:
                self.fase = "subir"
                self.valor = 720
            case 4:
                self.fase = "aparecer"
                self.valor = 0
            case 5:
                self.fase = "desintegrarse"
                self.valor = 0
                self.posibles_coordenadas = [
                    (x, y)
                    for x in range(0, int(1280 / 40))
                    for y in range(0, int(720 / 40))
                ]
            case _:
                pass

    def actualizar(self, screen):
        """
        Funcion actualizar: Actualiza la transicion correspondiente.
        """
        match self.animacion:
            case 1:
                return self.animacion_inicio(screen)
            case 2 | 3:
                return self.animacion_tienda(screen)
            case 4 | 5:
                return self.animacion_gameover(screen)
            case _:
                pass

    def animacion_inicio(self, screen):  # Animacion de inicio
        """
        Funcion animacion inicio: La animacion de la pantalla de inicio.
        """
        ancho_pantalla = screen.get_width()
        alto_pantalla = screen.get_height()

        if self.fase == "expandir":
            screen.blit(
                self.paginas[0], (0, 0)
            )  # Se muestra la pantalla de fondo primero
            self.valor += (ancho_pantalla - self.valor + 1) * 0.3
            if self.valor >= ancho_pantalla:
                self.valor = ancho_pantalla
                self.fase = "contraer"
        elif self.fase == "contraer":
            screen.blit(
                self.paginas[1], (0, 0)
            )  # Se muestra la pantalla de fondo primero
            self.valor -= (ancho_pantalla - self.valor + 1) * 0.2
            if self.valor <= 0:
                self.fase = ""
                return self.num_pagina_destino

        posx = ancho_pantalla / 2 - self.valor / 2
        posy = 0
        pygame.draw.rect(screen, (0, 0, 0), [posx, posy, self.valor, alto_pantalla])

        return None

    def animacion_tienda(self, screen):  # Animacion bajada y subida de la Tienda
        """
        Funcion animacion tienda: Anima la tienda al abrir y cerrarla.
        """
        ancho_pantalla = screen.get_width()
        alto_pantalla = screen.get_height()

        screen.blit(self.paginas[0], (0, 0))

        pantalla_oscurecida = pygame.Surface((ancho_pantalla, alto_pantalla))
        pantalla_oscurecida.set_alpha(self.valor * 0.2)
        screen.blit(pantalla_oscurecida, (0, 0))

        if self.fase == "bajar":
            self.valor += int((alto_pantalla - self.valor) * 0.15) + 1
        elif self.fase == "subir":
            self.valor -= int((alto_pantalla - self.valor) * 0.15) + 1

        screen.blit(self.paginas[1], (0, self.valor - alto_pantalla))

        if self.valor >= alto_pantalla or self.valor <= 0:
            return self.num_pagina_destino
        else:
            return None

    def animacion_gameover(self, screen):
        """
        Funcion animacion gameover: Animacion para cuando pierdes el juego.
        """
        if self.fase == "aparecer":
            pantalla_go = self.paginas[1]
            pantalla_go.set_alpha(self.valor)
            self.valor += (255 - self.valor) * 0.01

            screen.blit(pantalla_go, (0, 0))
            if self.valor >= 100:
                return self.num_pagina_destino
        elif self.fase == "desintegrarse":
            superficie_borrado = pygame.Surface(
                (40, 40),
                pygame.SRCALPHA,
            )

            for _ in range(10):
                if self.posibles_coordenadas:
                    coordenada = random.choice(self.posibles_coordenadas)
                    self.posibles_coordenadas.remove(coordenada)
                    coordenada = (coordenada[0] * 40, coordenada[1] * 40)
                    self.paginas[0].blit(
                        superficie_borrado,
                        coordenada,
                        special_flags=pygame.BLEND_RGBA_MULT,
                    )
                else:
                    return self.num_pagina_destino

            screen.blit(self.paginas[1], (0, 0))
            screen.blit(self.paginas[0], (0, 0))

        return None


class Animador_Texto:
    """
    Clase animador texto: Anima los textos en pantalla.
    Esta clase tiene posibilidad de expansion para crear nuevas animaciones.

    Inicializacion de atributos:
    - Texto: texto que se va a escribir.
    - X, y: posicion del texto, con posicion final.
    - La mayoria son todos atributos del texto.
    """

    def __init__(self):
        # Estado actual del texto animado
        self.texto = str()
        self.x = 0
        self.y = 0
        self.x_final = 0
        self.y_final = 0
        self.opacidad = 255
        self.color = (255, 255, 255)
        self.tamano = 30
        self.vel_movimiento = 0.1
        self.vel_opacidad = 3
        self.activo = False

    def iniciar(
        self, texto, x, y, x_final=None, y_final=None, color=(255, 255, 255), tamano=40
    ):
        """
        Funcion iniciar: Inicializa la animacion.
        """
        self.texto = texto
        self.x = x
        self.y = y
        self.x_final = x_final if x_final is not None else x
        self.y_final = y_final if y_final is not None else y
        self.color = color
        self.tamano = tamano
        self.opacidad = 255
        self.activo = True

    def actualizar(self):
        """
        Funcion actualizar: Actualiza la animacion.
        """
        if not self.activo:
            return

        # El texto sube ligeramente
        self.y -= (self.y - self.y_final) * self.vel_movimiento

        # Se desvanece progresivamente
        self.opacidad -= self.vel_opacidad
        if self.opacidad <= 0:
            self.opacidad = 0
            self.activo = False  # La animación termina

    def dibujar(self, screen):
        """
        Funcion dibujar: Muestra por pantalla el estado actual del texto animado.
        """
        self.actualizar()
        if self.activo and self.opacidad > 0:
            Texto.mostrar_texto_transparente(
                screen,
                f"+{self.texto}",
                self.x,
                self.y,
                self.opacidad,
                self.tamano,
                self.color,
            )
