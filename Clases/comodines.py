import pygame
from Clases.boton import Boton
# Hay que pensar que atributos tien y que hace cada comodin

# Si tienen un funcionamiento muy diferente habria que
# evaluar hacer una clase diferente por cada uno y
# despues agruparlos en una clase diferente o algo

# El mejor caso seria que compartieran atributos (multiplicador,
# nombre, etc.) pero no funcionamiento, para asi poder hacer uso de
# herencia por cada comodin


# Ahora mismo esta igual que la clase carta
class Comodin(Boton):
    def __init__(self, ruta_imagen, posicion):
        super().__init__(ruta_imagen, posicion)
        self.nombre = str()
        self.descripcion = str()
        self.rareza = int() # "Comun", "Raro", "Epico"
        self.precio = int() # Precio de la carta
    
    def dibujar(self):
        pass