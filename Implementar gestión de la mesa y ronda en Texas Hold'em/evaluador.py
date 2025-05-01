from collections import Counter
from jugador import Jugador 

# Función que evalúa el tipo de mano
def evaluar_mano(cartas):
    valores = [carta[:-1] for carta in cartas]  # Extraer valores de las cartas
    palos = [carta[-1] for carta in cartas]  # Extraer palos de las cartas

    # Contar las frecuencias de los valores
    valor_count = Counter(valores)
    palo_count = Counter(palos)

    # Escalera
    es_escalera = len(valor_count) == 5 and (max([valores.index(v) for v in valor_count]) - min([valores.index(v) for v in valor_count]) == 4)

    # Color
    es_color = len(palo_count) == 1

    # Combos
    pares = [valor for valor, count in valor_count.items() if count == 2]
    tres = [valor for valor, count in valor_count.items() if count == 3]
    cuatro = [valor for valor, count in valor_count.items() if count == 4]

    if len(pares) == 1 and len(tres) == 1: 
        return "Full House"
    elif es_escalera and es_color:
        return "Escalera Real" if "A" in valores else "Escalera de Color"
    elif len(pares) == 2:
        return "Doble Par"
    elif len(pares) == 1:
        return "Par"
    elif len(tres) == 1:
        return "Trío"
    elif len(cuatro) == 1:
        return "Poker"
    elif es_color:
        return "Color"
    elif es_escalera:
        return "Escalera"
    else:
        return "Carta Alta"

# Función para comparar las manos y determinar al ganador
def comparar_manos(jugadores, cartas_comunes):
    manos = {}
    
    # Evaluar la mano de cada jugador
    for jugador in jugadores:
        mano = jugador.obtener_cartas_completas(cartas_comunes)  # Obtener las cartas propias + comunes
        mano_evaluada = evaluar_mano(mano)  # Evaluar la mano del jugador
        manos[jugador.nombre] = mano_evaluada
    
    # Encontrar el jugador con la mejor mano
    ganador = max(manos, key=manos.get)
    return ganador

# Función para desempatar manos si es necesario
def desempate(jugadores, mano_comparada):
    jugadores_con_igual_mano = [j for j in jugadores if evaluar_mano(j.obtener_cartas_completas(j.cartas_comunes)) == mano_comparada]
    
    if len(jugadores_con_igual_mano) == 1:
        return jugadores_con_igual_mano[0].nombre

    # Si hay empate, comparamos por kicker (carta más alta)
    return max(jugadores_con_igual_mano, key=lambda j: max(j.obtener_cartas_completas(j.cartas_comunes), key=lambda c: c[:-1]))