from jugador import Jugador
from mesa import Mesa

def mostrar_estado_jugadores(jugadores):
    print("\n--- ESTADO ACTUAL DE LOS JUGADORES ---")
    for jugador in jugadores:
        estado = "Activo" if jugador.activo else "Eliminado"
        en_ronda = "En ronda" if jugador.en_ronda else "Fuera de ronda"
        print(f"{jugador.nombre}: Fichas={jugador.fichas}, Cartas={jugador.cartas}, Estado={estado}, {en_ronda}")

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
try:
    mesa.jugar_mano()
except ValueError as e:
    print(f"Error durante la partida: {e}")
    print("La partida ha sido detenida debido a error en el mazo.")

mostrar_estado_jugadores(jugadores)

print("\n--- 🧍 ESTADO FINAL DE JUGADORES ---")
for jugador in jugadores:
    print(f"{jugador.nombre}: Fichas = {jugador.fichas}, Cartas = {jugador.cartas}, Activo = {jugador.activo}, En ronda = {jugador.en_ronda}")
