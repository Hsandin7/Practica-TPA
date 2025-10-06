import random
from carta import Carta

class Mazo:
    def __init__(self):
        self.cartas = [Carta(valor, palo) for palo in Carta.PALOS for valor in Carta.VALORES]
        self.barajar()

    def barajar(self):
        random.shuffle(self.cartas)

    def robar(self):
        if self.cartas:
            carta = self.cartas[-1]   # obtiene la última carta sin borrarla
            self.cartas.pop()         # la elimina del mazo
            return carta              # devuelve el valor
        return None
    
    def __str__(self):      # Cabia como se muestra el mazo cuando se hace un print (Solo para debugging)
        return ", ".join(str(carta) for carta in self.cartas)


# Testing
sep = Mazo()
print(sep)