class Niveles:
    def __init__(self):
        self.nivel_actual = 1
        self.puntos = 0
        self.puntos_nivel = 100
        self.multiplicador = 1.5
        # self.boss = {
            
        # }

    def siguente_nivel(self):
        self.nivel_actual += 1
        self.puntos = 0
        self.puntos_nivel = self.puntos_nivel * self.multiplicador
    
    def nivel_perdido(self):
        self.nivel_actual = 1
        self.puntos = 0
        self.puntos_nivel = 100

    def verificar_nivel(self, puntos):
        if puntos >= self.puntos_nivel:
            self.siguente_nivel()
            print("siguente nivel")
            return True
            