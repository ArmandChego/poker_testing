from jugador import Jugador
from mesa import Mesa

# Crear jugadores
jugadores = [
    Jugador("Tokki", 500),
    Jugador("Cometa", 500),
    Jugador("Frost", 500),
    Jugador("Oumeg", 500),
    Jugador("Ari", 500),
    Jugador("Eduard", 500)
]

# Crear la mesa
mesa = Mesa(jugadores)

# Jugar una mano (Parte 1 completa)
print("\n--- 🃏 INICIANDO MANO ---\n")
mesa.jugar_mano()

# Mostrar estado final de cada jugador
print("\n--- 🧍 ESTADO FINAL DE JUGADORES ---")
for j in jugadores:
    print(f"{j.nombre}: Fichas = {j.fichas}, Cartas = {j.cartas}, Activo = {j.activo}, En ronda = {j.en_ronda}")
