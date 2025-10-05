from mazo import Mazo

class Jugador:
    def __init__(self, puntos, comodines):
        self._puntos = puntos
        self._mano = []
        self._cartas_seleccionadas = [] # No puede tener mas de 5
        self._comodines = comodines
    
    def seleccionar_carta(self):
        if len(self._cartas_seleccionadas) <= 5:
            carta_seleccionada = self._mano[int(input("Seleccione la " + str(len(self._cartas_seleccionadas) + 1) + " carta: "))]
            
            if carta_seleccionada in self._cartas_seleccionadas:
                self._cartas_seleccionadas.remove(carta_seleccionada)
            else:
                self._cartas_seleccionadas.append(carta_seleccionada)

    def descartar_cartas(self, mazo: Mazo):
        for carta_seleccionada in self._cartas_seleccionadas:
            self._mano.remove(carta_seleccionada)
            self._mano.append(mazo.robar())
        self._cartas_seleccionadas.clear()

    def jugar_cartas(self):
        # Codigo para sumar puntuaciones usando "self._cartas_seleccionadas"
        
        
        num = [c.strip("♠♥♦♣") for c in self._cartas_seleccionadas]
        palo = [c.strip("0123456789") for c in self._cartas_seleccionadas]

        # --- HAY UNA PAREJA (mismo num) ---
        for i in range(len(num)):
           for j in range(i + 1, len(num)): 
               if num[i] == num[j]:
                   self._puntos = self._puntos + 2
                   return
               
        # --- HAY UN TRIO (mismo num) ---
        
        self._cartas_seleccionadas.clear()
    
    def nueva_mano(self, mazo: Mazo):
        for i in range(8):
            self._mano.append(mazo.robar())