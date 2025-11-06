import random
import pygame
from src.jugador import Jugador
from src.comodines import Comodin
from src._utilidades import mostrar_texto, mostrar_texto_centrado

class Tienda:
    """Clase Tienda: Hace toda la funcionalidad de la tienda.
            Inicializa los atributos:
            - Los comodines disponibles en la tienda, ademas de que los muestra.
            - Esta la funcion de cambiar de comodines y comprar.
            - Se resta del dinero el precio del comodin.
    """
    def __init__(self, jugador: Jugador):
        self.jugador = jugador
        self.comodines_disponibles = [
            "gloton", "stonks", "matematico", "calculadora", "loco",
            "doblete", "esteroides", "programador", "clon"
        ]
        self.coste_cambiar = 2
        self.tienda_comodines = [None, None]
        self.comodin_seleccionado = None
        self.poblar()

def poblar_tienda(self):
    
    """
        La funcion poblar tienda sirve para mostrar los comodines que puede comprar en la tienda,
        y que con el random hace que no se puedan repetir un mismo comodin en la tienda.
    """
        pos_slot_1 = (690, 250)
        pos_slot_2 = (840, 250)
        
        #Determinar cuántos comodines quedan y elegirlos de forma única
        num_a_elegir = min(2, len(self.comodines_disponibles))
        
        if num_a_elegir == 0:
            self.tienda_comodines[0] = None
            self.tienda_comodines[1] = None
            self.comodin_seleccionado = None
            return

        # Elige los nombres únicos (1 o 2)
        nombres = random.sample(self.comodines_disponibles, num_a_elegir)

        # Elimina los nombres elegidos de la lista de disponibles
        for nombre in nombres:
            self.comodines_disponibles.remove(nombre)
            
        nombre1 = nombres[0]
        nombre2 = nombres[1] if len(nombres) == 2 else None

        # Crear objetos Comodin y asignarles posición
        
        #Comodin 1
        self.tienda_comodines[0] = Comodin(nombre1)
        self.tienda_comodines[0].asignar_posicion(pos_slot_1[0], pos_slot_1[1])
        self.tienda_comodines[0].seleccionada = False
        
        #Comodin 2
        self.tienda_comodines[1] = Comodin(nombre2) if nombre2 else None
        if self.tienda_comodines[1]: 
            self.tienda_comodines[1].asignar_posicion(pos_slot_2[0], pos_slot_2[1])
            self.tienda_comodines[1].seleccionada = False

        # Finalizar
        self.comodin_seleccionado = None

    def mostrar(self, screen):
        """
            La funcion mostrar, muestra la informacion del precio de los comodines y el dinero del juegador.
        """
        mostrar_texto_centrado(screen, f"{self.jugador.dinero}$", 900, 150, 40)     # Mostrar dinero actual del jugador
        
        color_coste = (255, 255, 0) if self.jugador.dinero >= self.coste_cambiar else (255, 0, 0)   # Amarillo si se puede pagar Rojo si no
        mostrar_texto(screen, f"{self.coste_cambiar}$", 525, 400 , 30, color_coste)

        for comodin in self.tienda_comodines:
            if comodin:
                comodin.dibujar(screen)
                color_precio = (255, 255, 0) if self.jugador.dinero >= comodin.precio else (255, 0, 0)      # Amarillo si se puede pagar Rojo si no
                mostrar_texto_centrado(screen, f"{comodin.precio}$", comodin.rect.midbottom[0], comodin.rect.bottom + 3, 20, color_precio)
                if comodin.seleccionada:
                    screen.blit(comodin.imagen_hover, (comodin.x, comodin.y))

    def actualizar(self, eventos):
        """
            Devuelve si un comodin esta seleccionado o no.
        """
        # Selección de comodines
        for comodin in self.tienda_comodines:
            if comodin and comodin.detectar_seleccion(eventos):
                if comodin.seleccionada:
                    comodin.seleccionada = False
                    self.comodin_seleccionado = None
                else:
                    for c in self.tienda_comodines:
                        if c: c.seleccionada = False
                    comodin.seleccionada = True
                    self.comodin_seleccionado = comodin

    def cambiar(self):
        """
            Funcion del boton cambiar.
        """
        # Botón "Cambiar"
        if self.jugador.dinero >= self.coste_cambiar:
            self.jugador.dinero -= self.coste_cambiar
            self.coste_cambiar += 2
            self.poblar()

    def comprar(self):
        """
            Funcion del boton comprar.
        """
        # Botón "Comprar"
        if self.comodin_seleccionado and self.jugador.dinero >= self.comodin_seleccionado.precio and len(self.jugador.comodines_mano) < 5:
            self.jugador.dinero -= self.comodin_seleccionado.precio
            self.jugador.comodines_mano.append(self.comodin_seleccionado)
            idx = self.tienda_comodines.index(self.comodin_seleccionado)
            self.tienda_comodines[idx] = None
            self.comodin_seleccionado = None