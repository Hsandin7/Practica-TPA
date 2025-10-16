from Clases.boton import Boton

class Carta(Boton):
    PALOS = ["o", "c", "e", "b"]    # Oros(o), Copas(c), Espadas(e), Bastos(b)
    VALORES = list(range(1,13))

    def __init__(self, valor, palo):
        super().__init__(f"Graficos/cartas/{valor}{palo}.png", 1200, 600, "Sonidos/Sonido_Seleccionar_Cartas.mp3")
        self._valor = valor
        self._palo = palo
        self.x_final = self.x
        self.y_final = self.y
        self.velocidad = 0.2
        self.seleccionada = False

    @property
    def valor(self):
        return self._valor

    @property
    def palo(self):
        return self._palo
    
    def mover_hacia_destino(self):
        x = self.x
        y = self.y
        x += (self.x_final - self.x) * self.velocidad
        y += (self.y_final - self.y) * self.velocidad
        super().asignar_posicion(x, y)

    def dibujar(self, screen):
        self.mover_hacia_destino()
        super().dibujar(screen)
    
    def detectar_seleccion(self, eventos):
        if self.detectar_click(eventos):
            self.seleccionada = not self.seleccionada