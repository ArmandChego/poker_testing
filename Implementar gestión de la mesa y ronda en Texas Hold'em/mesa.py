from mazo import Mazo
from dealer import Dealer
from ronda_apuestas import RondaApuestas
from evaluador import comparar_manos

class Mesa:
    def __init__(self, jugadores, small_blind=10, big_blind=20):
        self.jugadores = jugadores
        self.dealer = Dealer(jugadores)
        self.small_blind = small_blind
        self.big_blind = big_blind
        self.mazo = Mazo()
        self.fase = "preflop"
        self.cartas_comunes = []  # Lista para almacenar las cartas comunes

    def jugar_mano(self):
        self.dealer.rotar_boton()
        self.dealer.asignar_ciegas(self.small_blind, self.big_blind)
        self.mazo.barajar()
        self.mazo.repartir_cartas_jugadores(self.jugadores)

        print(f"Cartas de los jugadores: {[j.cartas for j in self.jugadores]}")
        ronda = RondaApuestas(self.jugadores)
        ronda.ejecutar_ronda()

        # Repartir las cartas comunes (flop, turn, river)
        flop, turn, river = self.mazo.repartir_cartas_comunes()

        # Aseguramos que sean listas antes de concatenarlas
        if isinstance(flop, list) and isinstance(turn, list) and isinstance(river, list):
            self.cartas_comunes = flop + turn + river  # Almacena las cartas comunes
        else:
            print("Error: Las cartas comunes no son listas.")
            return  # Salir del juego si ocurre un error

        print(f"Flop: {flop}")
        ronda.ejecutar_ronda()

        print(f"Turn: {turn}")
        ronda.ejecutar_ronda()

        print(f"River: {river}")
        ronda.ejecutar_ronda()

        # Determinar al ganador de la mano
        ganador = comparar_manos(self.jugadores, self.cartas_comunes)
        print(f"El ganador de la mano es: {ganador}")

        # Verificar si sólo queda un jugador activo
        jugadores_en_pie = [j for j in self.jugadores if j.en_ronda and j.activo]
        if len(jugadores_en_pie) == 1:
            print(f"Ganador inmediato: {jugadores_en_pie[0].nombre}")
        else:
            print("Continuar con siguiente fase (flop, turn, river)")

    def jugar_fase(self):
        if self.fase == "preflop":
            self.dealer.repartir_cartas()
            self.ronda_apuestas()
            self.fase = "flop"
        elif self.fase == "flop":
            flop, turn, river = self.mazo.repartir_cartas_comunes()  # Repartir cartas comunes (flop, turn, river)
            self.cartas_comunes = flop + turn + river
            print(f"Flop: {flop}")
            self.ronda_apuestas()
            self.fase = "turn"
        elif self.fase == "turn":
            # Ya no se reparten cartas, solo se debe manejar la fase
            print(f"Turn: {self.cartas_comunes[3]}")
            self.ronda_apuestas()
            self.fase = "river"
        elif self.fase == "river":
            # Ya no se reparten cartas, solo se debe manejar la fase
            print(f"River: {self.cartas_comunes[4]}")
            self.ronda_apuestas()
            self.fase = "final"
