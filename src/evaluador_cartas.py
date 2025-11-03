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
    """Clase Evaluador_Cartas: Comprueba si las cartas jugadas tienen alguna puntuación
    
        Inicializa los atributos:
        - cartas es la lista de las cartas jugadas
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
        if self._Escalera() and self._Color(self.cartas.copy()):
            return self.cartas

    @jugada(condicion= lambda self: len(self.cartas) >= 4, base=60, multiplicador=7)
    def _Poker(self):
        for c1 in self.cartas:
            for c2 in self.cartas:
                for c3 in self.cartas:
                    for c4 in self.cartas:
                        if c1 != c2 and c1 != c3 and c1 != c4 and c2 != c3 and c2 != c4 and c3 != c4:
                            if c1.valor == c2.valor == c3.valor == c4.valor:
                                return [c1, c2, c3, c4]

    @jugada(condicion= lambda self: len(self.cartas) == 5, base=40, multiplicador=4)
    def _Trio_y_Pareja(self):
        lista_cartas = self.cartas.copy()
        trio = self._Trio()
        if trio:
            lista_cartas.remove(trio[0])
            lista_cartas.remove(trio[1])
            lista_cartas.remove(trio[2])
            if lista_cartas[0].valor == lista_cartas[1].valor:
                return self.cartas
    
    @jugada(condicion= lambda self: len(self.cartas) == 5, base=50, multiplicador=6)
    def _Color(self, cartas=None):
        cartas = cartas or self.cartas
        color = cartas[0].palo
        for carta in cartas:
            if carta.palo is not color:
                return None
        return cartas

    @jugada(condicion= lambda self: len(self.cartas) == 5, base=30, multiplicador=4)
    def _Escalera(self):
        lista = sorted(self.cartas, key=lambda carta: carta.valor)
        c_anterior = lista[0]
        lista_actualizada = lista.copy()
        lista_actualizada.remove(c_anterior)
        for c_actual in lista_actualizada:
            if c_anterior.valor + 1 == c_actual.valor:
                c_anterior = c_actual
            else:
                return None
        return lista

    @jugada(condicion= lambda self: len(self.cartas) >= 3, base=30, multiplicador=3)
    def _Trio(self):
        for c1 in self.cartas:
            for c2 in self.cartas:
                for c3 in self.cartas:
                    if c1 != c2 and c1 != c3 and c2 != c3:
                        if c1.valor == c2.valor == c3.valor:
                            return [c1, c2, c3]

    @jugada(condicion= lambda self: len(self.cartas) >= 4, base=20, multiplicador=2)
    def _Doble_Pareja(self):
        lista_cartas = self.cartas.copy()
        pareja1 = self._Pareja(lista_cartas)
        if pareja1 is not None:
            lista_cartas.remove(pareja1[0])
            lista_cartas.remove(pareja1[1])
            pareja2 = self._Pareja(lista_cartas)
            if pareja2 is not None:
                return pareja2 + pareja1

    @jugada(condicion= lambda self: len(self.cartas) >= 2, base=10, multiplicador=2)
    def _Pareja(self, cartas=None):
        cartas = cartas or self.cartas
        for c1 in cartas:
            for c2 in cartas:
                if c1 is not c2 and c1.valor == c2.valor:
                    return [c1, c2]

    @jugada(condicion= lambda self: True, base=5, multiplicador=1)
    def _Carta_mas_alta(self):
        return [max(self.cartas, key=lambda c: c.valor)]
