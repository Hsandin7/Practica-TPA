from Clases.carta import Carta

# Cada comprobación devuelve una lista con las cartas que cumplen las condiciones
# (Menos la de carta más alta que devuelve una solo y después se convierte en lista para un manejo más sencillo)

# Toda la parte de evaluar ya está acabada
# Cuando se usa evaluar() se obtiene un diccionario (self.resultado) con las "Cartas", "Valor" y "Multiplicador"
# Correspondientes con la comprobación que sea verdadera

class Evaluador_Cartas:
    def __init__(self, cartas_seleccionadas):
        self.cartas = cartas_seleccionadas
        self.resultado = {"Cartas": list(), "Valor": int(), "Multiplicador": int()}

    def evaluar(self):
        if (cartas := self._Escalera_Color()) is not None:
            self.resultado["Cartas"] = cartas
            self.resultado["Valor"] = 100 + sum([c.valor for c in cartas])
            self.resultado["Multiplicador"] = 8
            return self.resultado
        
        if (cartas := self._Poker()) is not None:
            self.resultado["Cartas"] = cartas
            self.resultado["Valor"] = 60 + sum([c.valor for c in cartas])
            self.resultado["Multiplicador"] = 7
            return self.resultado
        
        if (cartas := self._Trio_y_Pareja()) is not None:
            self.resultado["Cartas"] = cartas
            self.resultado["Valor"] = 40 + sum([c.valor for c in cartas])
            self.resultado["Multiplicador"] = 4
            return self.resultado
        
        if (cartas := self._Color()) is not None:
            self.resultado["Cartas"] = cartas
            self.resultado["Valor"] = 50 + sum([c.valor for c in cartas])
            self.resultado["Multiplicador"] = 6
            return self.resultado
        
        if (cartas := self._Escalera()) is not None:
            self.resultado["Cartas"] = cartas
            self.resultado["Valor"] = 40 + sum([c.valor for c in cartas])
            self.resultado["Multiplicador"] = 4
            return self.resultado
        
        if (cartas := self._Trio()) is not None:
            self.resultado["Cartas"] = cartas
            self.resultado["Valor"] = 30 + sum([c.valor for c in cartas])
            self.resultado["Multiplicador"] = 3
            return self.resultado
        
        if (cartas := self._Doble_Pareja()) is not None:
            self.resultado["Cartas"] = cartas
            self.resultado["Valor"] = 20 + sum([c.valor for c in cartas])
            self.resultado["Multiplicador"] = 2
            return self.resultado
        
        if (cartas := self._Parejas()) is not None:
            self.resultado["Cartas"] = cartas
            self.resultado["Valor"] = 10 + sum([c.valor for c in cartas])
            self.resultado["Multiplicador"] = 2
            return self.resultado
        
        if (carta := self._Carta_mas_alta()) is not None:
            self.resultado["Cartas"] = [carta]
            self.resultado["Valor"] = 5 + carta.valor
            self.resultado["Multiplicador"] = 1
            return self.resultado
        


    def _Escalera_Color(self):
        resultado = None
        # Código
        return resultado

    def _Poker(self):
        resultado = None
        # Código
        return resultado

    def _Trio_y_Pareja(self):
        resultado = None
        # Código
        return resultado

    def _Color(self):
        resultado = None
        # Código
        return resultado

    def _Escalera(self):
        resultado = None
        # Código
        return resultado

    def _Trio(self):
        resultado = None
        # Código
        return resultado

    def _Doble_Pareja(self):
        resultado = None
        # Código
        return resultado

    def _Parejas(self):
        resultado = None
        for c1 in self.cartas:
            for c2 in self.cartas:
                if c1 is not c2 and c1.valor == c2.valor:
                    resultado = [c1, c2]
        return resultado

    def _Carta_mas_alta(self):
        resultado = None
        for carta in self.cartas:
            if resultado is None or carta.valor > resultado.valor:
                resultado = carta
        return resultado
