import pygame

class Texto:
    """Clase Texto: Contiene las funcionalidades de la fuente."""

    _fuentes = {}

    # Se hace cache de cada uno de los tamanos de fuente y se cargan a traves de esta funcion
    @classmethod
    def cargar_fuente(cls, tamano):
        if tamano not in cls._fuentes:
            cls._fuentes[tamano] = pygame.font.Font("./tipografia_naipo.ttf", tamano)
        return cls._fuentes[tamano]

    @classmethod
    def mostrar_texto(
        cls, screen, texto: str, posx: int, posy: int, tamano=30, color=(255, 255, 255)
    ):
        fuente = cls.cargar_fuente(tamano)

        texto_renderizado = fuente.render(texto, True, color)
        screen.blit(texto_renderizado, (posx, posy))

    @classmethod
    def mostrar_texto_centrado(
        cls,
        screen,
        texto: str,
        posx_centrada: int,
        posy: int,
        tamano=30,
        color=(255, 255, 255),
    ):
        fuente = cls.cargar_fuente(tamano)

        texto_renderizado = fuente.render(texto, True, color)
        posx = posx_centrada - texto_renderizado.get_width() // 2
        screen.blit(texto_renderizado, (posx, posy))

    @classmethod
    def mostrar_texto_transparente(
        cls,
        screen,
        texto: str,
        posx: int,
        posy: int,
        opacidad: int,
        tamano=30,
        color=(255, 255, 255),
    ):
        fuente = cls.cargar_fuente(tamano)

        texto_renderizado = fuente.render(texto, True, color)
        superficie = pygame.Surface(texto_renderizado.get_size(), pygame.SRCALPHA)
        superficie.blit(texto_renderizado, (0, 0))
        superficie.set_alpha(opacidad)
        screen.blit(superficie, (posx, posy))

    @classmethod
    def mostrar_texto_multilinea(
        cls,
        screen,
        texto: str,
        posx: int,
        posy: int,
        tamano=20,
        color=(255, 255, 255),
        ancho_max=300,
    ):
        fuente = cls.cargar_fuente(tamano)
        palabras = texto.split(" ")
        lineas = []
        linea_actual = ""

        for palabra in palabras:
            prueba = linea_actual + palabra + " "
            if fuente.size(prueba)[0] > ancho_max:
                lineas.append(linea_actual)
                linea_actual = palabra + " "
            else:
                linea_actual = prueba
        lineas.append(linea_actual)

        for i, linea in enumerate(lineas):
            texto_renderizado = fuente.render(linea.strip(), True, color)
            screen.blit(texto_renderizado, (posx, posy + i * (tamano + 4)))