import pygame
import random
from Clases.boton import Boton
# Hay que pensar que atributos tien y que hace cada comodin

efectos_comodin={}
def registrar_efecto(nombre):
    def decorator(func):
        efectos_comodin[nombre]=func
        return func
    return decorator

#Definicion de efectos para cada comodin


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
    # for m in cartas_jugadas:
    #     fichas = fichas - m.valor
        
    return fichas,multi, dinero

@registrar_efecto("programador")
def efecto_programador(mano, fichas, multi, dinero, cartas_jugadas):
    
    multi_extra = 0
    for m in mano:
        if m.valor == 1:
            multi_extra += 1
    
    multi = multi + multi_extra

    return fichas,multi, dinero
    

# Ahora mismo esta igual que la clase carta
class Comodin(Boton):
    def __init__(self, nombre):
        super().__init__(f"Graficos/Comodines/{nombre}.png", 0,0)
        self.nombre = nombre
        self.descripcion = str()
        self.rareza = int() # "Comun", "Raro", "Epico"
        self.precio = int() # Precio de la carta

        self.arrastrado=False
        self.offset_x=0
        self.offset_y=0

    def aplicar(self, mano, fichas, multi, dinero, cartas_jugadas, comodines):
        print(self.nombre)
        print(f"Operacion antes: {fichas} + {multi}")
        if cartas_jugadas is None:
            cartas_jugadas = []
        
        if self.nombre == "clon":
            for d in reversed(comodines):
                if d is not self:
                    return d.aplicar(mano,fichas,multi,dinero,cartas_jugadas,comodines)
            return fichas, multi, dinero
        efecto = efectos_comodin.get(self.nombre)
        if efecto is None:
            return fichas, multi, dinero
        
        resultado = efecto(mano=mano, fichas=+fichas, multi=multi, dinero=dinero, cartas_jugadas=cartas_jugadas)
        return resultado
    
    def registrar_precio(self):
        match self.rareza:
            case "Comun":
                self.precio=3
            case "Raro":
                self.precio=5
            case "Epico":
                self.precio=8
        pass

    def mover_comodines(self, eventos, lista_comodines, limite_rect=None):
        for e in eventos:
            if e.type == pygame.MOUSEBUTTONDOWN and e.button == 1:
                if self.rect.collidepoint(e.pos):
                    self.arrastrado = True
                    mouse_x, mouse_y = e.pos
                    self.offset_x = self.rect.x - mouse_x
                    self.offset_y = self.rect.y - mouse_y

            elif e.type == pygame.MOUSEBUTTONUP and e.button == 1:
                if self.arrastrado:
                    self.arrastrado = False
                    for o in lista_comodines:
                        if o is not self and self.rect.colliderect(o.rect):
                            i = lista_comodines.index(self)
                            j = lista_comodines.index(o)
                            lista_comodines[i], lista_comodines[j] = lista_comodines[j], lista_comodines[i]
                            break

            elif e.type == pygame.MOUSEMOTION and self.arrastrado:
                mouse_x, mouse_y = e.pos
                self.rect.x = mouse_x + self.offset_x
                self.rect.y = mouse_y + self.offset_y
                self.x, self.y = self.rect.topleft
                if limite_rect:
                    self.rect.clamp_ip(limite_rect)
        base_x=257 - float((len(lista_comodines)-1) / 2) * 100
        for i,c in enumerate(lista_comodines):
            if not c.arrastrado:
                c.rect.topleft=(base_x+i*80,530)
                c.x,c.y=c.rect.topleft

    def dibujar(self,screen):
        self.x, self.y = self.rect.topleft
        super().dibujar(screen)
