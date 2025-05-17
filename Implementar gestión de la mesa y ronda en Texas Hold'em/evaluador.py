from collections import Counter

VALORES_CARTAS = {
    '2': 2, '3': 3, '4': 4, '5': 5, '6': 6,
    '7': 7, '8': 8, '9': 9, '10': 10,
    'J': 11, 'Q': 12, 'K': 13, 'A': 14
}

PALOS_VALIDOS = {'♠', '♥', '♦', '♣'}

NOMBRES_MANOS = {
    9: "Escalera Real",
    8: "Escalera de Color",
    7: "Póker",
    6: "Full House",
    5: "Color",
    4: "Escalera",
    3: "Trío",
    2: "Doble Par",
    1: "Par",
    0: "Carta Alta"
}

# Validación del formato de carta
def carta_valida(carta):
    if len(carta) < 2:
        return False
    valor = carta[:-1]
    palo = carta[-1]
    return valor in VALORES_CARTAS and palo in PALOS_VALIDOS

def evaluar_mano(cartas):
    if not all(carta_valida(c) for c in cartas):
        return "Formato inválido"

    valores = sorted([VALORES_CARTAS[c[:-1]] for c in cartas], reverse=True)
    palos = [c[-1] for c in cartas]
    valor_count = Counter(valores)
    palo_count = Counter(palos)

    es_color = len(palo_count) == 1
    es_escalera = False

    valores_unicos = sorted(set(valores))
    if len(valores_unicos) == 5:
        if valores_unicos[-1] - valores_unicos[0] == 4:
            es_escalera = True
        # Escalera baja A-2-3-4-5
        elif valores_unicos == [2, 3, 4, 5, 14]:
            es_escalera = True
            valores = [5, 4, 3, 2, 1]  # Ajustar orden para comparación

    pares = [v for v, c in valor_count.items() if c == 2]
    tres = [v for v, c in valor_count.items() if c == 3]
    cuatro = [v for v, c in valor_count.items() if c == 4]

    if es_escalera and es_color:
        return (9, max(valores)) if max(valores) == 14 else (8, max(valores))  # Escalera Real o de Color
    elif cuatro:
        return (7, cuatro[0])
    elif tres and pares:
        return (6, tres[0])  # Full House
    elif es_color:
        return (5, valores)
    elif es_escalera:
        return (4, max(valores))
    elif tres:
        return (3, tres[0])
    elif len(pares) == 2:
        return (2, sorted(pares, reverse=True))
    elif len(pares) == 1:
        return (1, pares[0])
    else:
        return (0, valores)

def comparar_manos(jugadores, cartas_comunes):
    mejores_manos = []
    for jugador in jugadores:
        mano = jugador.obtener_cartas_completas(cartas_comunes)
        evaluacion = evaluar_mano(mano)
        if evaluacion != "Formato inválido":
            mejores_manos.append((evaluacion, jugador.nombre))

    if not mejores_manos:
        return "Sin manos válidas"

    ganador = max(mejores_manos)
    tipo_mano = NOMBRES_MANOS[ganador[0][0]]
    return f"{ganador[1]} gana con {tipo_mano}"

def desempate(jugadores, mano_comparada):
    jugadores_con_igual_mano = [j for j in jugadores
                                if evaluar_mano(j.obtener_cartas_completas(j.cartas_comunes))[0] == mano_comparada[0]]

    mejores = []
    for jugador in jugadores_con_igual_mano:
        mano = jugador.obtener_cartas_completas(jugador.cartas_comunes)
        evaluacion = evaluar_mano(mano)
        mejores.append((evaluacion, jugador.nombre))

    if not mejores:
        return "Empate sin manos válidas"

    ganador = max(mejores)
    return ganador[1]
