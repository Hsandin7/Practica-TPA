import pygame
from Clases._utilidades import mostrar_texto_transparente

class Transicion:
    def __init__(self):
        self.grosor = 0
        self.fase = ""      # expandir , contraer
        self.paginas = [None, None]
        self.num_pagina_destino = 0
        self.angulo = 0
        self.velocidad_expandir = 0.3
        self.velocidad_contraer = 0.2
    
    def iniciar(self, pagina_actual, pagina_destino, num_pagina_destino):
        self.paginas = [pagina_actual, pagina_destino]
        self.num_pagina_destino = num_pagina_destino
        self.grosor = 0
        self.fase = "expandir"
    
    def actualizar(self, screen, num_transicion):
        num = None
        match num_transicion:
            case 1:
                self.animacion_1(screen)
            case 2:
                self.animacion_2(screen)
            case _:
                pass
        
        return num

    def animacion_1(self, screen):
        ancho = screen.get_width()
        alto = screen.get_height()
        
        if self.fase == "expandir":
            screen.blit(self.paginas[0], (0, 0))
            self.grosor += (ancho - self.grosor + 1) * self.velocidad_expandir
            if self.grosor >= ancho:
                self.grosor = ancho
                self.fase = "contraer"
        elif self.fase == "contraer":
            screen.blit(self.paginas[1], (0, 0))
            self.grosor -= (ancho - self.grosor + 1) * self.velocidad_contraer
            if self.grosor <= 0:
                self.fase = ""
                return self.num_pagina_destino

        posx = ancho/2 - self.grosor/2
        posy = 0
        pygame.draw.rect(screen, (0,0,0), [posx, posy, self.grosor, alto])
        
        return None
    
    def animacion_2(self, screen):
        ancho = screen.get_width()
        alto = screen.get_height()
        
        if self.fase == "expandir":
            screen.blit(self.paginas[0], (0, 0))
            self.grosor += (ancho - self.grosor + 1) * self.velocidad_expandir
            if self.grosor >= ancho:
                self.grosor = ancho
                self.fase = "contraer"
        elif self.fase == "contraer":
            screen.blit(self.paginas[1], (0, 0))
            self.grosor -= (ancho - self.grosor + 1) * self.velocidad_contraer
            if self.grosor <= 0:
                self.fase = ""
                return self.num_pagina_destino

        posx = ancho/2 - self.grosor/2
        posy = 0
        pygame.draw.rect(screen, (0,0,0), [posx, posy, self.grosor, alto])
        
        return None
    
    
    # intento segunda animacion:

    # cont = 0
    # def actualizar2(self, screen):
    #     ancho = screen.get_width()
    #     alto = screen.get_height()
    #     self.angulo += 5
    #     if self.angulo >= 365: self.angulo - 365
    #     self.velocidad_contraer = 0.1
    #     self.velocidad_expandir = 0.1
    #     if self.fase == "expandir":
    #         screen.blit(self.paginas[0], (0, 0))
    #         self.grosor += (ancho - self.grosor + 300) * self.velocidad_expandir
    #         if self.grosor >= ancho and self.angulo >= 360 and self.angulo <= 5:
    #             self.grosor = ancho
    #             self.fase = "pausa"
    #     elif self.fase == "pausa":
    #         cont += 1
    #         self.angulo = 0
    #         self.grosor = ancho
    #         if cont > 100:
    #             self.fase = "contraer"
    #     elif self.fase == "contraer":
    #         screen.blit(self.paginas[1], (0, 0))
    #         self.grosor -= (ancho - self.grosor + 100) * self.velocidad_contraer
    #         if self.grosor <= 0:
    #             self.grosor = 0
    #             self.angulo = 0
    #             self.fase = ""
    #             return self.num_destino

    #     cuadrado = pygame.Surface((self.grosor,self.grosor), pygame.SRCALPHA)
    #     cuadrado.fill((0,0,0))
    #     cuadrado_rotado = pygame.transform.rotate(cuadrado, self.angulo)
    #     cuadrado_pos = cuadrado_rotado.get_rect(center=(ancho/2, alto/2))
    #     screen.blit(cuadrado_rotado, cuadrado_pos)
    #     return None


class Animador_Texto:
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

    def iniciar(self, texto, x, y, x_final = None, y_final = None, color=(255,255,255), tamano=40):
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
        self.actualizar()
        if self.activo and self.opacidad > 0:
            mostrar_texto_transparente(screen, f"+{self.texto}", self.x, self.y, self.opacidad, self.tamano, self.color)