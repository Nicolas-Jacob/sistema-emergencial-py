import os
import math
from calculos.calcular_tempo import calcular_tempo_chegada
from calculos.calcular_drones import calcular_qtd_drones_necessarios

# Exibe todos os dados finais do pedido
def exibir_dados_pedido(distancia_km, peso_total, lista_kits, endereco, numero_rua, pessoas):
    os.system('cls' if os.name == 'nt' else 'clear')
    if not lista_kits:
        print("Nenhum Kit foi adicionado ao pedido. "
            "\nObrigado por usar nosso sistema de emergência!")
        return

    print("\nResumo do pedido:" \
    f"Pedido para {pessoas} pessoas registrado com sucesso!"
    f"Local de entrega: {endereco}, nº{numero_rua}!")
    for tipo_kit, nome_kit, qtd in lista_kits:
        print(f"- {qtd}x {tipo_kit} | {nome_kit}")

    tempo_minutos = calcular_tempo_chegada(distancia_km)
    qtd_drones = calcular_qtd_drones_necessarios(peso_total)

    print(f"\nTempo estimado de entrega: {math.ceil(tempo_minutos)} minutos!"
    f"\nSerão necessários {int(qtd_drones)} drone(s) para entregar os kits!" \
    "\nObrigado por usar nosso sistema de emergência. Os drones já estão a caminho!")
