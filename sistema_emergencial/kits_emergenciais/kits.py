import time

def kits(media_de_kit_por_pessoa, pessoas):
    peso_total = 0
    kits_selecionados = []
    limite_kits = media_de_kit_por_pessoa * pessoas

    # Dicionário com os kits médicos e suas descrições
    kits_medicos = {
        1: ("Kit para Ferimentos e Cortes", "Para tratar cortes, arranhões, feridas abertas e prevenir infecções."),
        2: ("Kit para Desidratação e Fadiga", "Ideal para quem ficou sem água potável ou em esforço excessivo."),
        3: ("Kit para Infecções Graves", "Após exposição à água contaminada, esgoto ou ferimentos infectados."),
        4: ("Kit para Problemas Respiratórios", "Após inalação de fumaça, mofo, poeira ou por doenças respiratórias."),
        5: ("Kit para Ansiedade e Estresse Agudo", "Pessoas em choque, trauma psicológico ou crises emocionais.")
    }

    # Dicionário com os kits alimentícios e suas descrições
    kits_alimenticios = {
        1: ("Kit Nutritivo Básico (Primeiras 24h)", "Alimentos essenciais para as primeiras 24 horas de sobrevivência."),
        2: ("Kit de Reidratação e Energia Rápida", "Reidratantes, energéticos e suplementos de absorção rápida."),
        3: ("Kit Infantil", "Comida e suplementos adequados para crianças."),
        4: ("Kit para Idosos ou Pessoas Vulneráveis", "Fácil digestão e alta densidade nutricional."),
        5: ("Kit Refeição Pronta", "Refeições completas que podem ser consumidas sem preparo.")
    }

    # Loop principal de seleção dos kits
    while True:
        print("\n1.Kits Médicos"
        "\n2.Kits Alimentícios"
        "\n3.Remover Kit"
        "\n4.Finalizar pedido"
        f"\nKits selecionados até agora: {sum(qtd for _, _, qtd in kits_selecionados)}")

        try:
            escolha_kit = int(input("\nDigite a opção desejada: "))
            # Escolha de kits médicos
            if escolha_kit == 1:
                for num, (nome, desc) in kits_medicos.items():
                    print(f"{num}. {nome}. {desc}")
                tipo = int(input("\nDigite o número correspondente ao Kit que é da sua necessidade (1 a 5): "))
                if tipo not in kits_medicos:
                    print("\nOpção inválida! Digite um número de 1 a 5.")
                    continue
                qtd = int(input("Digite a quantidade necessária desse kit: "))
                if sum(qtd for _, _, qtd in kits_selecionados) + qtd > limite_kits:
                    print(f"\nErro! Esse pedido ultrapassaria o limite máximo de {limite_kits} kits.")
                    continue
                tipo_kit = "Kit Médico"
                nome_kit = kits_medicos[tipo][0]
                kits_selecionados.append((tipo_kit, nome_kit, qtd))
                peso_total += qtd * 2

            # Escolha de kits alimentícios
            elif escolha_kit == 2:
                for num, (nome, desc) in kits_alimenticios.items():
                    print(f"{num}. {nome}. {desc}")
                tipo = int(input("\nDigite o número do Kit que é da sua necessidade (1 a 5): "))
                if tipo not in kits_alimenticios:
                    print("\nOpção inválida! Digite um número de 1 a 5.")
                    continue
                qtd = int(input("\nDigite a quantidade necessária desse kit: "))
                if sum(qtd for _, _, qtd in kits_selecionados) + qtd > limite_kits:
                    print(f"\nErro! Esse pedido ultrapassaria o limite máximo de {limite_kits} kits.")
                    continue
                tipo_kit = "Kit Alimentício"
                nome_kit = kits_alimenticios[tipo][0]
                kits_selecionados.append((tipo_kit, nome_kit, qtd))
                peso_total += qtd * 5

            # Remoção de kits do pedido
            elif escolha_kit == 3:
                if not kits_selecionados:
                    print("\nNenhum Kit foi adicionado! Escolha outra opção.")
                    continue
                else:
                    print("\nKits adicionados:")
                    for idx, (tipo_kit, nome_kit, qtd) in enumerate(kits_selecionados, 1):
                        print(f"{idx}. {qtd}x {tipo_kit} | {nome_kit}")
                # Escolher qual kit remover
                while True:
                    try:
                        num_remover = int(input("\nDigite o número do kit que deseja remover: "))
                        if num_remover < 1 or num_remover > len(kits_selecionados):
                            print("\nOpção inválida! Escolha um número válido.")
                            continue
                        break
                    except ValueError:
                        print("\nPor favor, digite apenas números!")
                # Definir a quantidade a ser removida
                while True:
                    try:
                        qtd_remover = int(input("Digite a quantidade que deseja remover: "))
                        tipo_kit, nome_kit, qtd_atual = kits_selecionados[num_remover - 1]
                        if qtd_remover == 0:
                            print("\nNenhum kit removido.")
                            break
                        if qtd_remover > qtd_atual:
                            print("\nErro! Você não pode remover mais kits do que adicionou.")
                            continue
                        break
                    except ValueError:
                        print("\nPor favor, digite apenas números!")
                if qtd_remover == qtd_atual:
                    kits_selecionados.pop(num_remover - 1)
                    peso_total -= qtd_atual * (2 if tipo_kit == "Kit Médico" else 5)
                else:
                    kits_selecionados[num_remover - 1] = (tipo_kit, nome_kit, qtd_atual - qtd_remover)
                    peso_total -= qtd_remover * (2 if tipo_kit == "Kit Médico" else 5)
                print("\nKit removido com sucesso!")

            # Finalizar o pedido
            elif escolha_kit == 4:
                total_kits_selecionados = sum(qtd for _, _, qtd in kits_selecionados)
                if total_kits_selecionados > limite_kits:
                    print(f"\nErro! Você ultrapassou o limite permitido de {limite_kits} kits. "
                        "Por favor, remova alguns kits antes de finalizar o pedido.")
                    continue
                print("\nFinalizando pedido...", end="", flush=True)
                time.sleep(2.5)
                print("\nPedido finalizado com sucesso!")
                break
            else:
                print("\nDigite uma opção válida!")
        except ValueError:
            print("Por favor, digite apenas números!")
    return peso_total, kits_selecionados