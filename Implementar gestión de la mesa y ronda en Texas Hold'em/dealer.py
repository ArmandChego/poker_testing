import random

class Dealer:
    def __init__(self, jugadores):
        self.jugadores = jugadores
        self.indice_boton = 0

    def rotar_boton(self):
        self.indice_boton = (self.indice_boton + 1) % len(self.jugadores)

    def asignar_ciegas(self, small_blind, big_blind):
        sb_index = (self.indice_boton + 1) % len(self.jugadores)
        bb_index = (self.indice_boton + 2) % len(self.jugadores)

        jugador_sb = self.jugadores[sb_index]
        jugador_bb = self.jugadores[bb_index]

        if jugador_sb.fichas < small_blind:
            print(f"{jugador_sb.nombre} no tiene suficientes fichas para la ciega pequeña.")
            apuesta_sb = jugador_sb.apostar(jugador_sb.fichas)  # Apuesta todo lo que tiene
        else:
            apuesta_sb = jugador_sb.apostar(small_blind)

        if jugador_bb.fichas < big_blind:
            print(f"{jugador_bb.nombre} no tiene suficientes fichas para la ciega grande.")
            apuesta_bb = jugador_bb.apostar(jugador_bb.fichas)  # Apuesta todo lo que tiene
        else:
            apuesta_bb = jugador_bb.apostar(big_blind)

        return {"small_blind": sb_index, "big_blind": bb_index}

    def repartir_cartas(self):
        for jugador in self.jugadores:
            jugador.cartas = [self._carta_aleatoria() for _ in range(2)]

    def _carta_aleatoria(self):
        palos = ['♠', '♥', '♦', '♣']
        valores = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        return random.choice(valores) + random.choice(palos)

    def gestionar_fases(self, fase):
        if fase == "preflop":
            self.repartir_cartas()
        elif fase == "flop":
            pass
        elif fase == "turn":
            pass
        elif fase == "river":
            pass
