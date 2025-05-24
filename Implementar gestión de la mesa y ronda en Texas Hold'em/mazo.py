import random

class Mazo:
    def __init__(self):
        self.cartas = []
        self.cartas_usadas = []
        self.crear_mazo()

    def crear_mazo(self):
        palos = ['♠', '♥', '♦', '♣']
        valores = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        
        self.cartas = []  # Reiniciar lista por si se llama varias veces
        for _ in range(3):
            for palo in palos:
                for valor in valores:
                    self.cartas.append(f"{valor}{palo}")

    def barajar(self):
        random.shuffle(self.cartas)

    def verificar_o_reiniciar_mazo(self, cartas_necesarias):
        if len(self.cartas) < cartas_necesarias:
            print("Mazo insuficiente, reiniciando mazo y barajando...")
            self.cartas += self.cartas_usadas
            self.cartas_usadas = []
            self.barajar()
            if len(self.cartas) < cartas_necesarias:
                raise ValueError("Mazo insuficiente incluso después de reiniciar y barajar.")

    def repartir_cartas_jugadores(self, jugadores):
        cartas_necesarias = 2 * len(jugadores)
        self.verificar_o_reiniciar_mazo(cartas_necesarias)
        if len(self.cartas) < cartas_necesarias:
            raise ValueError("No hay cartas suficientes para repartir a todos los jugadores.")
        for jugador in jugadores:
            jugador.cartas = [self.sacar_carta(), self.sacar_carta()]

    def repartir_cartas_comunes(self):
        cartas_necesarias = 5  # flop(3) + turn(1) + river(1)
        self.verificar_o_reiniciar_mazo(cartas_necesarias)
        flop = [self.sacar_carta() for _ in range(3)]
        turn = [self.sacar_carta()]
        river = [self.sacar_carta()]
        return flop, turn, river

    def sacar_carta(self):
        carta = self.cartas.pop()
        self.cartas_usadas.append(carta)
        return carta
