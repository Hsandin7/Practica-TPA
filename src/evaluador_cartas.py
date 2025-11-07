# Cada comprobacion devuelve una lista con las cartas que cumplen las condiciones
# (Menos la de carta mas alta que devuelve una solo y despues se convierte en lista para un manejo mas sencillo)

# Toda la parte de evaluar ya esta acabada
# Cuando se usa evaluar() se obtiene un diccionario (self.resultado) con las "Cartas", "Valor" y "Multiplicador"
# correspondientes con la comprobacion que sea verdadera

# Decorador
def jugada(condicion, base, multiplicador):
    def decorador(func):
        def nueva_funcion(self):
            if not condicion(self):   # Comprobación del numero total de cartas jugadas (Es una funcion lambda)
                return None
            cartas = func(self)
            if cartas:
                self.resultado = {
                    "Cartas": cartas,
                    "Valor": base + sum(c.valor for c in cartas),
                    "Multiplicador": multiplicador
                    }
                return self.resultado
        return nueva_funcion
    return decorador


class Evaluador_Cartas:
    """Clase Evaluador_Cartas: Comprueba si las cartas jugadas tienen alguna puntuación.
    
        Inicializa los atributos:
        - cartas es la lista de las cartas jugadas.
        - resultado lo que se devulve al acabar la evaluacion.
        
    """

    def __init__(self):
        self.cartas = list()
        self.resultado = {"Cartas": [], "Valor": 0, "Multiplicador": 0}

    def evaluar(self, cartas_seleccionadas):
        """Funcion evaluar: Comprueba todas las posibles jugadas con un un orden de prioridad
            comprobando si las cartas jugadas corresponden a alguna jugada para sumar la puntucaion
            y devolver el resultado.
        """
        self.cartas = cartas_seleccionadas
        self.cartas.sort(key=lambda carta: carta.valor)
        
        comprobaciones = [
            self._Escalera_Color,
            self._Poker,
            self._Trio_y_Pareja,
            self._Color,
            self._Escalera,
            self._Trio,
            self._Doble_Pareja,
            self._Pareja,
            self._Carta_mas_alta
        ]

        for funcion in comprobaciones:
            if (resultado := funcion()):
                return resultado

    @jugada(condicion= lambda self: len(self.cartas) == 5, base=100, multiplicador=8)
    def _Escalera_Color(self):
        if self._Escalera() and self._Color():
            return self.cartas

    @jugada(condicion= lambda self: len(self.cartas) >= 4, base=60, multiplicador=7)
    def _Poker(self):
        for c1 in self.cartas:
            iguales = [c for c in self.cartas if c.valor == c1.valor]
            if len(iguales) == 4:
                return iguales

    @jugada(condicion= lambda self: len(self.cartas) == 5, base=40, multiplicador=4)
    def _Trio_y_Pareja(self):
        trio = self._Trio()
        if trio:
            restantes = [c for c in self.cartas if c not in trio]
            if restantes[0].valor == restantes[1].valor:
                return self.cartas
    
    @jugada(condicion= lambda self: len(self.cartas) == 5, base=50, multiplicador=6)
    def _Color(self):
        if all([c.palo == self.cartas[0].palo for c in self.cartas]):
            return self.cartas

    @jugada(condicion= lambda self: len(self.cartas) == 5, base=30, multiplicador=4)
    def _Escalera(self):
        lista = sorted(self.cartas, key=lambda carta: carta.valor)
        if all(lista[i+1].valor == lista[i].valor + 1 for i in range(len(lista)-1)):
            return lista

    @jugada(condicion= lambda self: len(self.cartas) >= 3, base=30, multiplicador=3)
    def _Trio(self):
        for c1 in self.cartas:
            iguales = [c for c in self.cartas if c.valor == c1.valor]
            if len(iguales) == 3:
                return iguales

    @jugada(condicion= lambda self: len(self.cartas) >= 4, base=20, multiplicador=2)
    def _Doble_Pareja(self):
        cartas_originales = self.cartas.copy()
        pareja1 = self._Pareja()
        if pareja1:
            self.cartas = [c for c in cartas_originales if c not in pareja1["Cartas"]]
            pareja2 = self._Pareja()
            self.cartas = cartas_originales
            if pareja2:
                return pareja1["Cartas"] + pareja2["Cartas"]

    @jugada(condicion= lambda self: len(self.cartas) >= 2, base=10, multiplicador=2)
    def _Pareja(self):
        for c1 in self.cartas:
            iguales = [c for c in self.cartas if c.valor == c1.valor and c is not c1]
            if iguales:
                return [c1, iguales[0]]

    @jugada(condicion= lambda self: True, base=5, multiplicador=1)
    def _Carta_mas_alta(self):
        return [max(self.cartas, key=lambda c: c.valor)]