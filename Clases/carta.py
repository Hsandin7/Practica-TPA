import pygame

class Carta:
    PALOS = ["o", "c", "e", "b"]    # Oros(o), Copas(c), Espadas(e), Bastos(b)
    VALORES = list(range(1,13))

    def __init__(self, valor, palo):
        self._valor = valor
        self._palo = palo
        self._imagen = pygame.image.load(f"Graficos/cartas/{self.valor}{self.palo}.png")    # Imagen correspondiente cargada
        self._x = int()      # Pos de la imagen
        self._y = int()

    @property
    def valor(self):
        return self._valor

    @property
    def palo(self):
        return self._palo

    def asignar_posicion(self, posx, posy):     # Asigna la posición de la imagen
        self._x = posx
        self._y = posy

    def mostrar(self, screen):                  # Función para mostrar la carta
        screen.blit(self._imagen, (self._x,self._y))
        pass

    def __str__(self):              # Cabia como se muestra la carta cuando se hace un print (Solo para debugging)
            return f"{self._valor}{self._palo}"
    

# # Testing
# sep = Carta(4, "o")
# print(sep)