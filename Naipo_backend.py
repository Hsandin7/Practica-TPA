# import pygame
import random
import pygame


# cartas de cada tipo

class carta:
    def __init__(self, tipo):
        self._tipo = tipo


class carta_normal(carta):
    def __init__(self, tipo, palo, numero):
        tipo = "normal"
        super().__init__(tipo)
        self._palo = palo
        self._numero = numero


class comodin(carta):
    def __init__(self, tipo):
        tipo = "comodin"
        super().__init__(tipo)


# Clase de la baraja entera inicial
class Mazo:
    palos = ["♠", "♥", "♦", "♣"]
    def __init__(self):
        self.cartas = [f"{numero}{palo}" for palo in Mazo.palos for numero in range(1, 13)]
        self.barajar()

    def barajar(self):
        random.shuffle(self.cartas)

    def robar(self):
        if self.cartas:
            carta = self.cartas[-1]   # obtiene la última carta sin borrarla
            self.cartas.pop()         # la elimina del mazo
            return carta
        return None


# Mano hecha
class jugador:
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




class juego:
    def __init__(self, jugador: jugador):
        pass



# Diccionarios...:
# comodines = {
#     "Pereira": comodin(1)
#     "wasdwasd": comodin()

# }


hola = Mazo()
jug1 = jugador(0, 0)

print(hola.cartas)

jug1.nueva_mano(hola)

print("\nMano jugador:")
print(jug1._mano)

# print()
# print("Baraja actualizada:")
# print(hola.cartas)

print()                                         # Permite al usuario seleccionar las cartas
while len(jug1._cartas_seleccionadas) < 5:
    jug1.seleccionar_carta()

print("\nCartas seleccionadas:")                                        # Muestra las cartas seleccionadas
print(jug1._cartas_seleccionadas)


JugarODescartar = input("\nDescartar (D) o jugar cartas(J)?:").lower()  # Decide si jugar o descartar las cartas
if JugarODescartar == 'd':   
    jug1.descartar_cartas(hola)
elif JugarODescartar == 'j':
    jug1.jugar_cartas()
else:
    print("No se ha seleccionado nada")


print("\nBaraja actualizada:")
print(hola.cartas)

print("\nMano jugador actualizada:")
print(jug1._mano)

print("\nTus puntos son: ")
print(jug1._puntos)






# if __name__ == "__main__":
#     print(hola.cartas)



# 1 Selecciona                  HECHO
# 2 Descartar o jugar           



