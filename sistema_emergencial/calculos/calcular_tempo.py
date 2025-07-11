# Cálculo do tempo de entrega com base na distância
def calcular_tempo_chegada(distancia_km):
    velocidade_drone_kmh = 72
    tempo_horas = distancia_km / velocidade_drone_kmh
    tempo_minutos = tempo_horas     * 60
    return tempo_minutos