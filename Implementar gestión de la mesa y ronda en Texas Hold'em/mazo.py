import random

class Mazo:
    def __init__(self):
        self.cartas = []
        self.cartas_usadas = []
        self.crear_mazo()

    def crear_mazo(self):
        palos = ['♠', '♥', '♦', '♣']
        valores = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        
        for _ in range(3):
            for palo in palos:
                for valor in valores:
                    self.cartas.append(f"{valor}{palo}")

    def barajar(self):
        random.shuffle(self.cartas)

    def repartir_cartas_jugadores(self, jugadores):
        for jugador in jugadores:
            jugador.cartas = [self.sacar_carta(), self.sacar_carta()]

    def repartir_cartas_comunes(self):
        # Reparte las cartas comunes (flop, turn, river)
        if len(self.cartas) >= 5:  # Verificar que haya suficientes cartas
            flop = [self.sacar_carta() for _ in range(3)]  # Reparte el flop (3 cartas)
            turn = [self.sacar_carta()]  # Reparte la carta del turn
            river = [self.sacar_carta()]  # Reparte la carta del river
            return flop, turn, river
        else:
            return [], [], []  # Si no hay cartas suficientes, devuelve listas vacías

    def sacar_carta(self):
        carta = self.cartas.pop()
        self.cartas_usadas.append(carta)
        return carta
