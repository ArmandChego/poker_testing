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

        # Validar que las listas no estén vacías para evitar errores
        if not flop or not turn or not river:
            print("Error: No hay cartas suficientes para continuar la mano.")
            return

        self.cartas_comunes = flop + turn + river  # Almacena las cartas comunes

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
            flop, turn, river = self.mazo.repartir_cartas_comunes()
            # Validar que no estén vacíos antes de asignar
            if not flop or not turn or not river:
                print("No hay cartas suficientes para la fase flop.")
                return
            self.cartas_comunes = flop + turn + river
            print(f"Flop: {flop}")
            self.ronda_apuestas()
            self.fase = "turn"
        elif self.fase == "turn":
            if len(self.cartas_comunes) > 3:
                print(f"Turn: {self.cartas_comunes[3]}")
            else:
                print("No hay carta para Turn.")
            self.ronda_apuestas()
            self.fase = "river"
        elif self.fase == "river":
            if len(self.cartas_comunes) > 4:
                print(f"River: {self.cartas_comunes[4]}")
            else:
                print("No hay carta para River.")
            self.ronda_apuestas()
            self.fase = "final"