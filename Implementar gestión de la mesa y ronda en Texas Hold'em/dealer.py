import random

class Dealer:
    def __init__(self, jugadores):
        self.jugadores = jugadores
        self.indice_boton = 0

    def rotar_boton(self):
        self.indice_boton = (self.indice_boton + 1) % len(self.jugadores)

    def asignar_ciegas(self, small_blind, big_blind):
        sb = (self.indice_boton + 1) % len(self.jugadores)
        bb = (self.indice_boton + 2) % len(self.jugadores)
        apuesta_sb = self.jugadores[sb].apostar(small_blind)
        apuesta_bb = self.jugadores[bb].apostar(big_blind)
        return { "small_blind": sb, "big_blind": bb }

    def repartir_cartas(self):
        for jugador in self.jugadores:
            jugador.cartas = [self._carta_aleatoria() for _ in range(2)]

    def _carta_aleatoria(self):
        palos = ['♠', '♥', '♦', '♣']
        valores = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        return random.choice(valores) + random.choice(palos)

    def gestionar_fases(self, fase):
        if fase == "preflop":
            self.repartir_cartas()  # Reparte las cartas a los jugadores
        elif fase == "flop":
            # Reparte las cartas comunes (flop)
            pass
        elif fase == "turn":
            # Reparte la carta común del turn
            pass
        elif fase == "river":
            # Reparte la carta común del river
            pass
