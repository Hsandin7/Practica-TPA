import random
from src.carta import Carta

class Mazo:
    """Clase Mazo: Crea el mazo con todas las cartas y su funcionalidad
       
        Inicializa los atributos:
        - cartas: lista de las cartas del mazo.

        """
    
    def __init__(self):
        self.cartas = [Carta(valor, palo) for palo in Carta.PALOS for valor in Carta.VALORES]
        self.barajar()

    def barajar(self):
        """Funcion barajar: ordena las cartas de manera random."""
        random.shuffle(self.cartas)

    def robar(self):
        """Funcion robar: devuelve la ultima carta del mazo y la elimina de el 
            para que no vuelva a aparecer. """
        if self.cartas:
            carta = self.cartas[0]      # obtiene la primera carta sin borrarla
            self.cartas.pop(0)          # la elimina del mazo
            return carta                # devuelve el valor (clase Carta)
        return None