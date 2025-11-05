import random

class Niveles:
    """Clase Niveles: Hace toda la funcionalidad de los niveles y los niveles que son un boss.
    
        Inicializa los atributos: 
            - nivel_actual a 1 ya que se empieza en el nivel 1
            - puntos a 0 porque en cada nivel empieza con 0 puntos 
            - puntos_nivel que son los puntos objetivo a lo que hay que llegar
            - multiplicador este multiplicador es lo que aumenta cada nivel.

    """
    def __init__(self):
        self.nivel_actual = 1
        self.puntos_nivel = 100
        self.multiplicador = 2.5
        self.color_pantalla = (0,0,0)
        self.colores_boss = [
            (100, 0, 0),     # rojo
            (0, 0, 72),     # azul
            (85, 0, 72),    # morado
            (0, 60, 0),     # verde
            (97, 0, 48),    # rosa
            (127, 52, 0),    # naranja
        ]
        self.es_boss = False
        self.carta_invalida = int()

    def siguente_nivel(self):
        """Funcion siguente_nivel: pasa de nivel sumando 1 al nivel_actual, 
            multiplicando los puntos objetivo por el multiplicador y pone los puntos del jugador a 0."""
        
        print(f"NNivel: {self.nivel_actual}, es bos: {self.es_boss}")
        self.nivel_actual += 1
        self.puntos_nivel = int(self.puntos_nivel * self.multiplicador)

        self.check_boss()

    def check_boss(self):
        if (self.nivel_actual -1)%3 == 0:
            self.es_boss = True
            self.color_pantalla = random.choice(self.colores_boss)
            self.carta_invalida = random.randint(1, 12)
            print (f"BOSS: {self.color_pantalla}")
        else:
            self.es_boss = False
            self.color_pantalla = (0,0,0)
            self.carta_invalida = None