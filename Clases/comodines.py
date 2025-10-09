import pygame
from Clases.boton import Boton
# Hay que pensar qué atributos tien y qué hace cada comodín

# Si tienen un funcionamiento muy diferente habría que
# evaluar hacer una clase diferente por cada uno y
# después agruparlos en una clase diferente o algo

# El mejor caso sería que compartieran atributos (multiplicador,
# nombre, etc.) pero no funcionamiento, para así poder hacer uso de
# herencia por cada comodín


# Ahora mismo está igual que la clase carta
class Comodin(Boton):
    def __init__(self, ruta_imagen, posicion, descripcion):
        super().__init__(ruta_imagen, posicion)
        self.descripcion = descripcion
    
    def dibujar(self):
        pass