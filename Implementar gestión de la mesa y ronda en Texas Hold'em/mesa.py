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

    def jugar_mano(self):
        # Rotar el botón y asignar las ciegas
        self.dealer.rotar_boton()
        self.dealer.asignar_ciegas(self.small_blind, self.big_blind)
        
        # Barajar el mazo antes de repartir las cartas
        self.mazo.barajar()

        # Repartir las cartas a los jugadores
        self.mazo.repartir_cartas_jugadores(self.jugadores)
        
        # Repartir las cartas comunes (flop, turn, river)
        flop, turn, river = self.mazo.repartir_cartas_comunes()

        # Mostrar las cartas comunes en cada fase
        print(f"Flop: {flop}")
        print(f"Turn: {turn}")
        print(f"River: {river}")
        
        # Ejecutar la ronda de apuestas
        ronda = RondaApuestas(self.jugadores)
        ronda.ejecutar_ronda()

        # Evaluar las manos de los jugadores y determinar el ganador
        ganador = comparar_manos(self.jugadores)
        print(f"El ganador de la mano es: {ganador}")

        # Verificar cuantos jugadores estan activos para ver si el juego termina
        jugadores_en_pie = [j for j in self.jugadores if j.en_ronda and j.activo]
        if len(jugadores_en_pie) == 1:
            print(f"Ganador inmediato: {jugadores_en_pie[0].nombre}")
        else:
            print("Continuar con siguiente fase (flop, turn, river)")
