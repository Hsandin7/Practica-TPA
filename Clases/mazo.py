import random
from Clases.carta import Carta

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
            carta = self.cartas[-1]   # obtiene la ultima carta sin borrarla
            self.cartas.pop()         # la elimina del mazo
            return carta              # devuelve el valor (clase Carta)
        return None
    
#     def __str__(self):      # Cabia como se muestra el mazo cuando se hace un print (Solo para debugging)
#         return ", ".join(str(carta) for carta in self.cartas)


# # # Testing
# # sep = Mazo()
# # print(sep)