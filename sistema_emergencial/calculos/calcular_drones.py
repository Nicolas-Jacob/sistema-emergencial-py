import math

# Cálculo de quantos drones serão necessários para transportar os kits
def calcular_qtd_drones_necessarios(peso_total):
    capacidade_drone_kg = 30
    qtd_drones = math.ceil(peso_total / capacidade_drone_kg)
    return int(qtd_drones)