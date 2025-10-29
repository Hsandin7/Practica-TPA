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

@registrar_efecto("matematico")
def efecto_matematico(mano,fichas,multi):
    return fichas,multi*2

@registrar_efecto("stonks")
def efecto_stonks(mano,dinero):
    return dinero*2

@registrar_efecto("calculadora")
def efecto_calculadora(mano,fichas, multi):
    carta_mayor=max(key=lambda c:c.valor)
    return fichas,multi+carta_mayor.valor

@registrar_efecto("loco")
def efecto_el_loco(mano, fichas, multi):
    multi_extra=random.choice([0,1,5,10,25,50])
    return fichas,multi+multi_extra

@registrar_efecto("doblete")
def efecto_doblete(mano, fichas,multi):
    fichas=0
    for m in mano:
        fichas+=m.valor*2
    return fichas,multi

@registrar_efecto("esteroides")
def efecto_esteroides(mano,fichas,multi):
    fichas=0
    for m in mano:
        fichas+=20
    return fichas,multi

@registrar_efecto("gloton")
def efecto_gloton(mano,fichas,multi):
    fichas=0
    for m in mano:
        fichas+=m.valor+20
        multi+=10
    return fichas,multi

@registrar_efecto("programador")
def efecto_programador(mano,fichas,multi,cartas_jugadas):
    bonus=cartas_jugadas//10
    return fichas,multi*(1+bonus)

# Ahora mismo esta igual que la clase carta
class Comodin(Boton):
    def __init__(self, nombre, x,y):
        super().__init__(f"Graficos/Comodines/{nombre}.png", x,y)
        self.nombre = str()
        self.descripcion = str()
        self.rareza = int() # "Comun", "Raro", "Epico"
        self.precio = int() # Precio de la carta
    
    def aplicar(self, mano, fichas, multi=1, dinero=0, cartas_jugadas=0,comodines=None):
        if self.nombre=="Clon" and comodines:
            i=comodines.i(self)
            if i>0:
                comodin_drch=comodines[i-1]
                return comodin_drch.aplicar(mano,fichas,multi,dinero,cartas_jugadas,comodines)
            else:
                return fichas, multi,dinero
        efecto=efectos_comodin.get(self.nombre)
        if efecto:
            resultado=efecto(mano,fichas,multi,dinero=dinero,cartas_jugadas=cartas_jugadas)
            if len(resultado)==2:
                fichas,multi=resultado
            else:
                fichas,multi,dinero=resultado
        return fichas,multi,dinero   
    
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