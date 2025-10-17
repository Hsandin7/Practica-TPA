import pygame

class Transicion:
    def __init__(self):
        self.grosor = 0
        self.fase = ""      # expandir , contraer
        self.paginas = [None, None]
        self.num_destino = 0
        self.angulo = 0
        self.velocidad_expandir = 0.3
        self.velocidad_contraer = 0.2
    
    def iniciar(self, pagina_actual, pagina_destino, num_destino):
        self.paginas = [pagina_actual, pagina_destino]
        self.num_destino = num_destino
        self.grosor = 0
        self.fase = "expandir"
    
    def actualizar(self, screen):
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
                return self.num_destino

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