class Jugador:
    def __init__(self, nombre, fichas):
        self.nombre = nombre
        self.fichas = fichas
        self.cartas = []
        self.apuesta_actual = 0
        self.activo = True
        self.en_ronda = True

    def apostar(self, cantidad):
        cantidad = min(cantidad, self.fichas)
        self.fichas -= cantidad
        self.apuesta_actual += cantidad
        return cantidad

    def retirarse(self):
        self.en_ronda = False

    def reiniciar_ronda(self):
        self.apuesta_actual = 0
        self.cartas = []
        self.en_ronda = self.activo

    def obtener_cartas_completas(self, cartas_comunes):
        return self.cartas + cartas_comunes
