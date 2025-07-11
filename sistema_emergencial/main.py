from calculos.calcular_drones import *
from calculos.calcular_tempo import *
from calculos.distancia import *
from calculos.quantidade_pessoas import *
from estoque.estoque import *
from exibicao_dados_pedido.exibicao_pedido import *
from kits_emergenciais.kits import *

# Mensagem de boas-vindas ao sistema
print("\nSeja bem-vindo(a) ao Sistema de Emergência Nacional. \
\nAqui você encontrará os melhores Kits Médicos e Alimentícios em caso de emergência. \
\nDigite as informações pedidas a seguir para que seu pedido seja feito da melhor forma possível!")

# Função principal que organiza a sequência das etapas
def main():
    distancia_km, endereco, numero_rua = distancia()
    media_de_kit_por_pessoa = estoque()
    pessoas = quantidade_pessoas(media_de_kit_por_pessoa)
    peso_total, lista_kits = kits(media_de_kit_por_pessoa, pessoas)
    exibir_dados_pedido(distancia_km, peso_total, lista_kits, endereco, numero_rua, pessoas)

# Executa o programa
if __name__ == "__main__":
    main()