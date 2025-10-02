import random

# ---------------------------
# Clase Carta
# ---------------------------
class Carta:
    PALOS = ["♠", "♥", "♦", "♣"]
    VALORES = {1: "A", 11: "J", 12: "Q", 13: "K"}

    def __init__(self, palo, valor):
        self.palo = palo
        self.valor = valor

    def __str__(self):
        v = Carta.VALORES.get(self.valor, str(self.valor))
        return f"{v}{self.palo}"


# ---------------------------
# Clase Mazo
# ---------------------------
class Mazo:
    def __init__(self):
        self.cartas = [Carta(p, v) for p in Carta.PALOS for v in range(1, 14)]
        self.barajar()

    def barajar(self):
        random.shuffle(self.cartas)

    def robar(self):
        return self.cartas.pop() if self.cartas else None


# ---------------------------
# Clase Mano
# ---------------------------
class Mano:
    def __init__(self):
        self.cartas = []

    def agregar(self, carta):
        if carta:
            self.cartas.append(carta)

    def reemplazar(self, indices, mazo):
        for i in indices:
            if 0 <= i < len(self.cartas):
                self.cartas[i] = mazo.robar()

    def __str__(self):
        return " ".join(f"[{i}] {c}" for i, c in enumerate(self.cartas))

    def evaluar(self):
        # Versión simple: suma de valores
        return sum(c.valor for c in self.cartas)


# ---------------------------
# Clase Juego
# ---------------------------
class Juego:
    def __init__(self):
        self.mazo = Mazo()

    def jugar_mano(self):
        mano = Mano()
        # Repartir 5 cartas
        for _ in range(5):
            mano.agregar(self.mazo.robar())

        print("\n=== Nueva Mano ===")
        print(mano)

        # Preguntar qué descartar
        descartar = input("Elige las posiciones a descartar (ej: 0 2 4) o Enter para quedarte todo: ")
        if descartar.strip():
            try:
                indices = list(map(int, descartar.split()))
                mano.reemplazar(indices, self.mazo)
            except ValueError:
                print("Entrada inválida, no se descarta nada.")

        # Mostrar mano final
        print("Tu mano final:")
        print(mano)

        # Evaluar puntaje
        puntaje = mano.evaluar()
        print(f"Puntaje de la mano: {puntaje}")
        return puntaje


# ---------------------------
# Main
# ---------------------------
if __name__ == "__main__":
    juego = Juego()
    total = 0

    while True:
        total += juego.jugar_mano()
        print(f"Puntaje acumulado: {total}")

        seguir = input("¿Jugar otra mano? (s/n): ")
        if seguir.lower() != "s":
            print("Gracias por jugar. Puntaje final:", total)
            break
