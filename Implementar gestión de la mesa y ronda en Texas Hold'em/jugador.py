class Jugador:
    def __init__(self, nombre, fichas):
        self.nombre = nombre
        self.fichas = fichas
        self.cartas = []
        self.apuesta_actual = 0
        self.activo = True
        self.en_ronda = True

    def apostar(self, cantidad):
        if not isinstance(cantidad, (int, float)) or cantidad <= 0 or cantidad == float('inf'):
            print(f"{self.nombre}: cantidad inválida para apostar: {cantidad}")
            return 0
        
        if self.fichas <= 0:
            print(f"{self.nombre}: no tiene fichas para apostar.")
            return 0
        
        cantidad_a_apostar = min(cantidad, self.fichas)
        self.fichas -= cantidad_a_apostar
        self.apuesta_actual += cantidad_a_apostar
        return cantidad_a_apostar

    def retirarse(self):
        self.en_ronda = False

    def reiniciar_ronda(self):
        self.apuesta_actual = 0
        self.cartas = []
        self.en_ronda = self.activo

    def obtener_cartas_completas(self, cartas_comunes):
        return self.cartas + cartas_comunes
