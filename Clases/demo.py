from Clases.juego import Juego
from Clases.animaciones import Transicion




class Demo:
    def __init__(self):
        self.activa = False
        self.contador = 0
        self.funcionar = True
    
    def checkear_inicio(self, pag_actual):
        if pag_actual == 0:
            self.contador += 1
        else:
            self.contador = 0
        
        if self.contador > 3*60:   # 30s x 60fps para esperar en total 30s
            self.activa = True
            self.contador = 0

    def ejecutar_demo(self, juego: Juego, transicion: Transicion):
        if self.contador < 200*60:
            if self.funcionar:
                self.funcionar = False
                juego.mostrar_fondo = True
                Juego.num_transicion = 1        # Transicion 1
                Juego.paginas_transicion = [juego.paginas[0], juego.paginas[1], 1]
                
                transicion.iniciar( Juego.paginas_transicion[0],
                                    Juego.paginas_transicion[1],
                                    Juego.paginas_transicion[2],
                                    Juego.num_transicion)