import pygame

class Carta:
    PALOS = ["♠", "♥", "♦", "♣"]    # Cambiar por: Oros(o), Copas(c), Espadas(e), Bastos(b)
    VALORES = list(range(1,13))

    def __init__(self, palo, valor):
        self.palo = palo
        self.valor = valor
        # self.imagen = pygame.image.load(f"{self.valor}{self.palo}")    # Imagen correspondiente cargada (faltan las imágenes)
        self.x = int()      # Pos de la imagen
        self.y = int()

    def __str__(self):              # Cabia como se muestra la carta cuando se hace un print (Solo para debugging)
        return f"{self.valor}{self.palo}"
    
    def asignar_posicion(self, posx, posy):     # Asigna la posición de la imagen
        self.x = posx
        self.y = posy

    def mostrar(self, screen):              # Función para mostrar la carta
        screen.blit(self.imagen, (0,0))
        pass


# # Testing
# sep = Carta("♠", 4)
# print(sep)