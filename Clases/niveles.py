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
        self.puntos = 0
        self.puntos_nivel = 100
        self.multiplicador = 1.5
        # self.boss = {
            
        # }

    def siguente_nivel(self):
        """Funcion siguente_nivel: pasa de nivel sumando 1 al nivel_actual, 
            multiplicando los puntos objetivo por el multiplicador y pone los puntos del jugador a 0."""
        
        self.nivel_actual += 1
        self.puntos = 0
        self.puntos_nivel = int(self.puntos_nivel * self.multiplicador)
    
    def nivel_perdido(self):
        """Funcion nivel_perdido: cuando no logras llegar a los puntos 
            objetivo se reinician todos los valores a los del inicio."""
        self.nivel_actual = 1
        self.puntos = 0
        self.puntos_nivel = 100

    def verificar_nivel(self, puntos):
        """Funcion verificar_nivel: comprueba si se ha alcanzado el objetivo de puntos y 
            si es así devuelve verdadero."""
        if puntos >= self.puntos_nivel:
            self.siguente_nivel()
            print("siguente nivel")
            return True
            