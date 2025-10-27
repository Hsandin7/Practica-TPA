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

@registrar_efecto("Pereira")
def efecto_matematico(mano,fichas,multi):
    return fichas,multi*2

@registrar_efecto("Stonks")
def efecto_stonks(mano,dinero):
    return dinero*2

@registrar_efecto("Calculadora")
def efecto_calculadora(mano,fichas, multi):
    carta_mayor=max(key=lambda c:c.valor)
    return fichas,multi+carta_mayor.valor

@registrar_efecto("El loco")
def efecto_el_loco(mano, fichas, multi):
    multi_extra=random.choice([0,1,5,10,25,50])
    return fichas,multi+multi_extra

@registrar_efecto("Doblete")
def efecto_doblete(mano, fichas,multi):
    fichas=0
    for m in mano:
        fichas+=m.valor*2
    return fichas,multi

@registrar_efecto("Esteroides")
def efecto_esteroides(mano,fichas,multi):
    fichas=0
    for m in mano:
        fichas+=20
    return fichas,multi

@registrar_efecto("Gloton")
def efecto_gloton(mano,fichas,multi):
    fichas=0
    for m in mano:
        fichas+=m.valor+20
        multi+=10
    return fichas,multi

@registrar_efecto("Programador")
def efecto_programador(mano,fichas,multi,cartas_jugadas):
    bonus=cartas_jugadas//10
    return fichas,multi*(1+bonus)

# Ahora mismo esta igual que la clase carta
class Comodin(Boton):
    def __init__(self, ruta_imagen, posicion,efecto):
        super().__init__(ruta_imagen, posicion)
        self.nombre = str()
        self.descripcion = str()
        self.rareza = int() # "Comun", "Raro", "Epico"
        self.precio = int() # Precio de la carta
        self.efecto=efecto
    
    def aplicar(self, mano, fichas, multi=1, dinero=0, cartas_jugadas=0,comodines=None):
        if self.efecto=="Clon" and comodines:
            i=comodines.i(self)
            if i>0:
                comodin_drch=comodines[i-1]
                return comodin_drch.aplicar(mano,fichas,multi,dinero,cartas_jugadas,comodines)
            else:
                return fichas, multi,dinero
        efecto=efectos_comodin.get(self.efecto)
        if efecto:
            resultado=efecto(mano,fichas,multi,dinero=dinero,cartas_jugadas=cartas_jugadas)
            if len(resultado)==2:
                fichas,multi=resultado
            else:
                fichas,multi,dinero=resultado
        return fichas,multi,dinero   
    def dibujar(self):
        pass