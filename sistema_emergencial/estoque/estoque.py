# Função para calcular média de kits disponíveis por pessoa
def estoque():
    estoque_kits_medicos= {
        "Kit para Ferimentos e Cortes": 15000,
        "Kit para Desidratação e Fadiga": 15000,
        "Kit para Infecções Graves": 15000,
        "Kit para Problemas Respiratórios": 8000,
        "Kit para Ansiedade e Estresse Agudo": 7000
    }

    estoque_kits_alimenticios = {
        "Kit Nutritivo Básico (Primeiras 24h)": 15000,
        "Kit de Reidratação e Energia Rápida": 12000,
        "Kit Infantil": 8000,
        "Kit para Idosos ou Pessoas Vulneráveis": 10000,
        "Kit Refeição Pronta": 15000,
    }

    qtd_pessoas_presenciaram_o_desastre = 60000
    qtd_total_kits_no_estoque = sum(estoque_kits_alimenticios.values()) + sum(estoque_kits_medicos.values())
    media_de_kit_por_pessoa = qtd_total_kits_no_estoque // qtd_pessoas_presenciaram_o_desastre
    return media_de_kit_por_pessoa
