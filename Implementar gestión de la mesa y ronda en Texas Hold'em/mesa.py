from dealer import Dealer
from ronda_apuestas import RondaApuestas

class Mesa:
    def __init__(self, jugadores, small_blind=10, big_blind=20):
        self.jugadores = jugadores
        self.dealer = Dealer(jugadores)
        self.small_blind = small_blind
        self.big_blind = big_blind

    def jugar_mano(self):
        self.dealer.rotar_boton()
        self.dealer.asignar_ciegas(self.small_blind, self.big_blind)
        self.dealer.repartir_cartas()
        ronda = RondaApuestas(self.jugadores)
        ronda.ejecutar_ronda()

        jugadores_en_pie = [j for j in self.jugadores if j.en_ronda and j.activo]
        if len(jugadores_en_pie) == 1:
            print(f"Ganador inmediato: {jugadores_en_pie[0].nombre}")
        else:
            print("Continuar con siguiente fase (flop, turn, river)")
