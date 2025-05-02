from jugador import Jugador
from mesa import Mesa

jugadores = [
    Jugador("Tokki", 500),
    Jugador("Cometa", 500),
    Jugador("Frost", 500),
    Jugador("Oumeg", 500),
    Jugador("Ari", 500),
    Jugador("Eduard", 500)
]

mesa = Mesa(jugadores)

print("\n--- 🃏 INICIANDO MANO ---\n")
mesa.jugar_mano()

print("\n--- 🧍 ESTADO FINAL DE JUGADORES ---")
for jugador in jugadores:
    print(f"{jugador.nombre}: Fichas = {jugador.fichas}, Cartas = {jugador.cartas}, Activo = {jugador.activo}, En ronda = {jugador.en_ronda}")
