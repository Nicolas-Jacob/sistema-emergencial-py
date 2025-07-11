# Função para perguntar a quantidade de pessoas no abrigo
def quantidade_pessoas(media_de_kit_por_pessoa):
    while True:
        try:
            pessoas = int(input("\nDigite a quantidade de pessoas que estão em seu abrigo (exemplo: 4, 12): "))
            if pessoas <= 0:
                print("\nA quantidade deve ser um número positivo!")
                continue
            break
        except ValueError:
            print("\nPor favor, digite apenas números!")
    limite_kits = media_de_kit_por_pessoa * pessoas              
    print(f"\nCada pessoa terá direito à {media_de_kit_por_pessoa:.0f} kits totalizando {limite_kits} kits, isso devido a capacidade do nosso estoque e a quantidade de pessoas necessitadas!")
    return pessoas
