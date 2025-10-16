from Clases.carta import Carta

# Cada comprobación devuelve una lista con las cartas que cumplen las condiciones
# (Menos la de carta más alta que devuelve una solo y después se convierte en lista para un manejo más sencillo)

# Toda la parte de evaluar ya está acabada
# Cuando se usa evaluar() se obtiene un diccionario (self.resultado) con las "Cartas", "Valor" y "Multiplicador"
# correspondientes con la comprobación que sea verdadera

class Evaluador_Cartas:
    def __init__(self, cartas_seleccionadas):
        self.cartas = cartas_seleccionadas
        self.resultado = {"Cartas": list(), "Valor": int(), "Multiplicador": int()}

    def evaluar(self):
        if len(self.cartas) == 5 and (cartas := self._Escalera_Color()) is not None:
            self.resultado["Cartas"] = cartas
            self.resultado["Valor"] = 100 + sum([c.valor for c in cartas])
            self.resultado["Multiplicador"] = 8
            print("Escalera Color")
            return self.resultado
        
        if len(self.cartas) >= 4 and (cartas := self._Poker()) is not None:
            self.resultado["Cartas"] = cartas
            self.resultado["Valor"] = 60 + sum([c.valor for c in cartas])
            self.resultado["Multiplicador"] = 7
            print("Poker")
            return self.resultado
        
        if len(self.cartas) == 5 and (cartas := self._Trio_y_Pareja()) is not None:
            self.resultado["Cartas"] = cartas
            self.resultado["Valor"] = 40 + sum([c.valor for c in cartas])
            self.resultado["Multiplicador"] = 4
            print("Trio y Pareja")
            return self.resultado
        
        if len(self.cartas) == 5 and (cartas := self._Color(self.cartas)) is not None:
            self.resultado["Cartas"] = cartas
            self.resultado["Valor"] = 50 + sum([c.valor for c in cartas])
            self.resultado["Multiplicador"] = 6
            print("Color")
            return self.resultado
        
        if len(self.cartas) == 5 and (cartas := self._Escalera()) is not None:
            self.resultado["Cartas"] = cartas
            self.resultado["Valor"] = 30 + sum([c.valor for c in cartas])
            self.resultado["Multiplicador"] = 4
            print("Escalera")
            return self.resultado
        
        if len(self.cartas) >= 3 and (cartas := self._Trio()) is not None:
            self.resultado["Cartas"] = cartas
            self.resultado["Valor"] = 30 + sum([c.valor for c in cartas])
            self.resultado["Multiplicador"] = 3
            print("Trio")
            return self.resultado
        
        if len(self.cartas) >= 4 and (cartas := self._Doble_Pareja()) is not None:
            self.resultado["Cartas"] = cartas
            self.resultado["Valor"] = 20 + sum([c.valor for c in cartas])
            self.resultado["Multiplicador"] = 2
            print("Doble Pareja")
            return self.resultado
        
        if len(self.cartas) >= 2 and (cartas := self._Parejas(self.cartas)) is not None:
            self.resultado["Cartas"] = cartas
            self.resultado["Valor"] = 10 + sum([c.valor for c in cartas])
            self.resultado["Multiplicador"] = 2
            print("Parejas")
            return self.resultado
        
        if (carta := self._Carta_mas_alta()) is not None:
            self.resultado["Cartas"] = [carta]
            self.resultado["Valor"] = 5 + carta.valor
            self.resultado["Multiplicador"] = 1
            print("Carta más alta")
            return self.resultado
        


    def _Escalera_Color(self):
        if self._Escalera() is not None and self._Color(self.cartas) is not None:
            return self.cartas
        return None

    def _Poker(self):
        for c1 in self.cartas:
            for c2 in self.cartas:
                for c3 in self.cartas:
                    for c4 in self.cartas:
                        if c1 != c2 and c1 != c3 and c1 != c4 and c2 != c3 and c2 != c4 and c3 != c4:
                            if c1.valor == c2.valor == c3.valor == c4.valor:
                                return [c1, c2, c3, c4]
        return None

    def _Trio_y_Pareja(self):
        lista_cartas = self.cartas.copy()
        trio = self._Trio()
        if trio is not None:
            lista_cartas.remove(trio[0])
            lista_cartas.remove(trio[1])
            lista_cartas.remove(trio[2])
            if len(lista_cartas) == 2  and lista_cartas[0].valor == lista_cartas[0].valor:
                return self.cartas
            else:
                return None
        else:
            return None

    def _Color(self, cartas):
        color = cartas[0].palo
        for carta in cartas:
            if carta.palo is not color:
                return None
        return cartas

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

    def _Trio(self):
        for c1 in self.cartas:
            for c2 in self.cartas:
                for c3 in self.cartas:
                    if c1 != c2 and c1 != c3 and c2 != c3:
                        if c1.valor == c2.valor == c3.valor:
                            return [c1, c2, c3]
        return None

    def _Doble_Pareja(self):
        lista_cartas = self.cartas.copy()
        pareja1 = self._Parejas(lista_cartas)
        if pareja1 is not None:
            lista_cartas.remove(pareja1[0])
            lista_cartas.remove(pareja1[1])
            pareja2 = self._Parejas(lista_cartas)
            if pareja2 is not None:
                return pareja2 + pareja1
            else:
                return None
        else:
            return None

    def _Parejas(self, cartas):
        for c1 in cartas:
            for c2 in cartas:
                if c1 is not c2 and c1.valor == c2.valor:
                    return [c1, c2]
        return None

    def _Carta_mas_alta(self):
        resultado = None
        for carta in self.cartas:
            if resultado is None or carta.valor > resultado.valor:
                resultado = carta
        return resultado
