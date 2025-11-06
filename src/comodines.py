import pygame
import random
from src.boton import Boton

efectos_comodin={}
def registrar_efecto(nombre):
    def decorator(func):
        efectos_comodin[nombre]=func
        return func
    return decorator

@registrar_efecto("gloton")
def efecto_gloton(mano, fichas, multi, dinero, cartas_jugadas):

    for _ in cartas_jugadas:
        fichas += 50
    multi += 10
    
    return fichas, multi, dinero

@registrar_efecto("stonks")
def efecto_stonks(mano, fichas, multi, dinero, cartas_jugadas):

    dinero = dinero*2

    return fichas, multi, dinero

@registrar_efecto("matematico")
def efecto_matematico(mano, fichas, multi, dinero, cartas_jugadas):

    multi =  multi*2

    return fichas, multi, dinero

@registrar_efecto("calculadora")
def efecto_calculadora(mano, fichas, multi, dinero, cartas_jugadas):

    carta_mayor=max(cartas_jugadas, key=lambda c:c.valor)
    multi = multi+carta_mayor.valor

    return fichas, multi, dinero


@registrar_efecto("loco")
def efecto_el_loco(mano, fichas, multi, dinero, cartas_jugadas):

    multi_extra=random.choice([0,1,5,10,25,50])
    multi = multi+multi_extra

    return fichas, multi, dinero

@registrar_efecto("doblete")
def efecto_doblete(mano, fichas, multi, dinero, cartas_jugadas):

    for m in cartas_jugadas:
        fichas+=m.valor
   
    return fichas, multi, dinero

@registrar_efecto("esteroides")
def efecto_esteroides(mano, fichas, multi, dinero, cartas_jugadas):
    
    for _ in cartas_jugadas:
        fichas+=20 

    return fichas,multi, dinero

@registrar_efecto("programador")
def efecto_programador(mano, fichas, multi, dinero, cartas_jugadas):
    
    multi_extra = 0
    for m in mano:
        if m.valor == 1:
            multi_extra += 1
    
    multi = multi + multi_extra

    return fichas,multi, dinero
    
class Comodin(Boton):
    _descripciones = {
        "matematico":   "Duplica el valor del multiplicador",
        "stonks":       "Gana el doble de dinero cada ronda",
        "calculadora":  "La carta mas alta jugada suma su valor como multiplicador en vez de puntos",
        "programador":  "Por cada as que tengas en la mano, aumenta el multiplicador en +1",
        "loco":         "Suma un multiplicador aleatorio   1/5/10/20/50",
        "doblete":      "Las cartas jugadas suman el doble",
        "esteroides":   "Todas las cartas suman 20 puntos",
        "gloton":       "Por cada carta jugada se suman 50 puntos y 10 de multi",
        "clon":         "Copia la accion del comodín que este colocado mas a la derecha"
    }
    
    def __init__(self, nombre):
        # Declaracion de los atributos
        super().__init__(f"Graficos/Comodines/{nombre}.png", 0,0)
        self.nombre = nombre
        self.descripcion = Comodin._descripciones[nombre]
        self.rareza = str() # "Comun", "Raro", "Epico"
        self.precio = int() # Precio de la carta
        # Declaracion de los estados de interacción
        self.seleccionada = False
        self.arrastrado=False
        self.offset_x=self.offset_y=0
        
        # Configuracion de rareza y precio del comodín en tienda según su rareza
        self._registrar_propiedades()

    # Metodo aplicar
    def aplicar(self, mano, fichas, multi, dinero, cartas_jugadas, comodines):
        if self.nombre == "clon":
            for d in reversed(comodines):
                if d is not self:
                    return d.aplicar(mano,fichas,multi,dinero,cartas_jugadas,comodines)
            return fichas, multi, dinero
        
        efecto = efectos_comodin.get(self.nombre)
        if efecto is None:
            return fichas, multi, dinero
        
        return efecto(mano,fichas,multi,dinero,cartas_jugadas or [])
    
    def _registrar_propiedades(self):
        # Asignar rareza y precio en base a la misma
        match self.nombre:
            case "matematico" | "stonks" | "calculadora" | "programador":
                self.rareza, self.precio = "comun", 3
            case "loco" | "doblete" | "esteroides":
                self.rareza, self.precio = "raro", 5
            case "gloton" | "clon":
                self.rareza, self.precio = "epico", 8
            case _:
                self.rareza, self.precio = "Desconocido", 1

    def detectar_seleccion(self, eventos):
        return self.detectar_click(eventos)
    
    def mover_comodines(self, eventos, lista_comodines, limite_rect=None):
        for e in eventos:
            if e.type == pygame.MOUSEBUTTONDOWN and e.button == 1 and self.rect.collidepoint(e.pos):
                self.arrastrado = True
                mouse_x, mouse_y = e.pos
                self.offset_x = self.rect.x - mouse_x
                self.offset_y = self.rect.y - mouse_y

            elif e.type == pygame.MOUSEBUTTONUP and e.button == 1:
                if self.arrastrado:
                    self.arrastrado = False
                    for o in lista_comodines:
                        if o is not self and self.rect.colliderect(o.rect):
                            i,j = lista_comodines.index(self),lista_comodines.index(o)
                            lista_comodines[i], lista_comodines[j] = lista_comodines[j], lista_comodines[i]
                            break

            elif e.type == pygame.MOUSEMOTION and self.arrastrado:
                mouse_x, mouse_y = e.pos
                self.rect.x = mouse_x + self.offset_x
                self.rect.y = mouse_y + self.offset_y
                self.x, self.y = self.rect.topleft
                if limite_rect:
                    self.rect.clamp_ip(limite_rect)
        

    def dibujar(self,screen):
        self.x, self.y = self.rect.topleft
        super().dibujar(screen)
