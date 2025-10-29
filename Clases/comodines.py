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

    for m in cartas_jugadas:
        fichas += m.valor + 50
    for m in cartas_jugadas:
        fichas = fichas - m.valor
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
        fichas+=m.valor*2
    for m in cartas_jugadas:
        fichas = fichas - m.valor

    return fichas, multi, dinero

@registrar_efecto("esteroides")
def efecto_esteroides(mano, fichas, multi, dinero, cartas_jugadas):
    
    for m in cartas_jugadas:
        fichas+=20
    for m in cartas_jugadas:
        fichas = fichas - m.valor

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
    
    def aplicar(self, mano, fichas, multi, dinero, cartas_jugadas, comodines):
        print(self.nombre)
        print(f"Operacion antes: {fichas} + {multi}")
        if cartas_jugadas is None:
            cartas_jugadas = []
        
        if self.nombre == "clon":
            if comodines: 
                i = comodines.index(self)
                if i>=0 and i < len(comodines)-1:
                    comodin_clonado = comodines[i+1]

                    return comodin_clonado.aplicar(mano, fichas, multi, dinero, cartas_jugadas, comodines)
                
                else:
                    return fichas, multi, dinero 
            
            else: 
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

    def dibujar(self,screen):
        super().dibujar(screen)
