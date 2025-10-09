from Clases.boton import Boton

class Carta(Boton):
    PALOS = ["o", "c", "e", "b"]    # Oros(o), Copas(c), Espadas(e), Bastos(b)
    VALORES = list(range(1,13))

    def __init__(self, valor, palo):
        super().__init__(f"Graficos/cartas/{valor}{palo}.png", (0,0), "Sonidos/Sonido_Seleccionar_Cartas.mp3")
        self._valor = valor
        self._palo = palo
        self.seleccionada = False

    @property
    def valor(self):
        return self._valor

    @property
    def palo(self):
        return self._palo
    
    def detectar_seleccion(self, eventos):
        if self.detectar_click(eventos):
            self.seleccionada = not self.seleccionada

    def detectar_seleccion2(self, eventos, contador): # Límite de selección de cartas
        if self.detectar_click(eventos):
            if self.seleccionada and contador >= 5:
                self.seleccionada = not self.seleccionada
            elif contador < 5:
                self.seleccionada = not self.seleccionada