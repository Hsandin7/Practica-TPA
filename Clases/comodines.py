import pygame

# Hay que pensar qué atributos tien y qué hace cada comodín

# Si tienen un funcionamiento muy diferente habría que
# evaluar hacer una clase diferente por cada uno y
# después agruparlos en una clase diferente o algo

# El mejor caso sería que compartieran atributos (multiplicador,
# nombre, etc.) pero no funcionamiento, para así poder hacer uso de
# herencia por cada comodín


# Ahora mismo está igual que la clase carta
class Comodin:
    PALOS = ["♠", "♥", "♦", "♣"]    # Cambiar por: Oros(o), Copas(c), Espadas(e), Bastos(b)
    VALORES = list(range(1,13))

    def __init__(self, palo, valor):
        self.palo = palo
        self.valor = valor
        # self.imagen = pygame.image.load(f"{self.valor}{self.palo}")    # Imagen correspondiente cargada
        self.x = int()
        self.y = int()

    def __str__(self):              # Cabia como se muestra la carta cuando se hace un print (Solo para debugging)
        return f"{self.valor}{self.palo}"
    
    def asignar_posicion(self, posx, posy):     # Asigna la posición de la imagen
        self.x = posx
        self.y = posy

    def mostrar(self):              # Función para mostrar la carta
        
        pass


# # Testing
# sep = Carta("♠", 4)
# print(sep)