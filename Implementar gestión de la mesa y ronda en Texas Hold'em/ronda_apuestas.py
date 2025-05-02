class RondaApuestas:
    def __init__(self, jugadores):
        self.jugadores = jugadores
        self.apuesta_maxima = 0

    def ejecutar_ronda(self):
        jugadores_activos = [j for j in self.jugadores if j.en_ronda and j.activo]
        while True:
            cambios = False
            for jugador in jugadores_activos:
                if jugador.apuesta_actual < self.apuesta_maxima:
                    accion = self.obtener_accion(jugador)  # Este es el punto donde la IA o jugador toman decisiones
                    if accion == "call":
                        diferencia = self.apuesta_maxima - jugador.apuesta_actual
                        jugador.apostar(diferencia)
                        cambios = True
                    elif accion == "raise":
                        incremento = 20  # Ejemplo fijo
                        total = (self.apuesta_maxima - jugador.apuesta_actual) + incremento
                        jugador.apostar(total)
                        self.apuesta_maxima += incremento
                        cambios = True
                    elif accion == "fold":
                        jugador.retirarse()
            if not cambios:
                break

    def obtener_accion(self, jugador):
        # Aquí puedes reemplazar por entrada de usuario o IA
        return "call"  # Por ahora simple para pruebas
