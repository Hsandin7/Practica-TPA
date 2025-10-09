from Clases.carta import Carta

class Evaluador_Cartas:
    def __init__(self, cartas_seleccionadas):
        self.cartas = cartas_seleccionadas
        self.resultado = {"Valor": int(), "Multiplicador": int()}

    def evaluar(self):
        if self._Escalera_Color:
            return self.resultado
        elif self._Poker:
            return self.resultado
        elif self._Trio_y_Pareja:
            return self.resultado
        elif self._Color:
            return self.resultado
        elif self._Escalera:
            return self.resultado
        elif self._Trio:
            return self.resultado
        elif self._Doble_Pareja:
            return self.resultado
        elif self._Parejas:
            return self.resultado
        elif self._Carta_mas_alta:
            return self.resultado

    def _Escalera_Color(self):
        pass

    def _Poker(self):
        pass

    def _Trio_y_Pareja(self):
        pass

    def _Color(self):
        pass

    def _Escalera(self):
        pass

    def _Trio(self):
        pass

    def _Doble_Pareja(self):
        pass

    def _Parejas(self):
        for carta in self.cartas:
            pass

    def _Carta_mas_alta(self):
        resultado = 0
        for carta in self.cartas:
            if carta.valor > resultado:
                resultado = carta
        return resultado


# lista = [1,5,6,3,2]
# print(sum(lista))