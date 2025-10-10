# Encapsula todo lo relacionado con la mano, el mazo y las acciones del jugador

from Clases.mazo import Mazo
from Clases.evaluador_cartas import Evaluador_Cartas

class Jugador:
    def __init__(self):
        self.puntos = int()
        self.mazo = Mazo()
        self._mano = [self.mazo.robar() for i in range(0,8)]

    
    def mostrar_puntos(self, screen):
        pass

    def mostrar_mano(self, screen):      
        pos_x = 535
        for carta in self._mano:
            carta.x_final = pos_x
            if carta.seleccionada:
                carta.y_final = 450
                #carta.asignar_posicion(pos_x, 450)
            else:
                carta.y_final = 500
                #carta.asignar_posicion(pos_x, 500)
            carta.dibujar(screen)
            
            pos_x += 75
    
    def actualizar(self, eventos):
        for carta in self._mano:
            carta.detectar_seleccion(eventos)
    
    def actualizar2(self, eventos): # Con límite de selección de cartas
        contador = 0
        for carta in self._mano:
            if carta.seleccionada:
                contador += 1
        
        for carta in self._mano:
            carta.detectar_seleccion(eventos, contador)

    def jugar_cartas(self):
        cartas_jugadas = [carta for carta in self._mano if carta.seleccionada]
        if cartas_jugadas is not []:        # Comprueba que haya cartas seleccionadas
            evaluador = Evaluador_Cartas(cartas_jugadas)
            print(evaluador.evaluar())      # Para debugging pero se tendrá que reemplazar con algo que use el resultado
            self.descartar_cartas()         # Una vez jugadas se descartan

    def descartar_cartas(self):
        seleccionadas = []
        for carta in self._mano:
            if carta.seleccionada:
                seleccionadas.append(carta)
        for carta in seleccionadas:
            self._mano.remove(carta)
        while len(self._mano) is not 8:
            self._mano.append(self.mazo.robar())
                




class Jugadorrrrr:
    def __init__(self):
        self._puntos = int()
        self._mano = []
        self._cartas_seleccionadas = [] # No puede tener mas de 5
        self._comodines = []
    
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





def comprobaciones():
    pass