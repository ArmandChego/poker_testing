import random

class Mazo:
    def __init__(self):
        self.cartas = []
        self.cartas_usadas = []
        self.crear_mazo()

    def crear_mazo(self):
        # 3 barajas de 52 cartas (156 cartas en total)
        palos = ['♠', '♥', '♦', '♣']
        valores = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        
        # Crear las tres barajas
        for _ in range(3):
            for palo in palos:
                for valor in valores:
                    self.cartas.append(f"{valor}{palo}")

    def barajar(self):
        # Mezcla aleatoriamente las cartas del mazo
        random.shuffle(self.cartas)

    def repartir_cartas_jugadores(self, jugadores):
        # Reparte 2 cartas a cada jugador
        for jugador in jugadores:
            jugador.cartas = [self.sacar_carta(), self.sacar_carta()]

    def repartir_cartas_comunes(self):
        # Reparte las cartas comunes (flop, turn, river)
        flop = [self.sacar_carta() for _ in range(3)]  # 3 cartas para el flop
        turn = self.sacar_carta()  # 1 carta para el turn
        river = self.sacar_carta()  # 1 carta para el river
        
        return flop, turn, river

    def sacar_carta(self):
        #Saca una carta del mazo y la marca como usada
        carta = self.cartas.pop()
        self.cartas_usadas.append(carta)
        return carta
