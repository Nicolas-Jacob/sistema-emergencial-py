# Função para entrada da distância e localização
def distancia():
    while True:
        try:
            distancia_km = float(input("\nEstamos localizados no Vale do Taquari - interior do Rio Grande do Sul!\n" \
            "Digite a distância em Quilômetros que você está da nossa base! Utilize apenas números (ex: 12, 8.5): "))
            if distancia_km <= 0:
                print("\nA distância deve ser um número positivo!")
                continue
            if distancia_km > 31:
                print("\nNosso Drone não tem capacidade para percorrer toda essa distância!"
                "\nLevaremos o drone até o local mais próximo possível e o soltaremos para ele conseguir chegar!")
            break
        except ValueError:
            print("\nPor favor, digite apenas números!")

    # Entrada do endereço
    while True:
        endereco = input("\nDigite o nome da rua em que você está: ").strip()
        if endereco.replace(" ", "").isalpha():
            break
        print("\nPor favor digite apenas letras (exemplo: Rua Monteiro Lobato)")

    # Entrada do número da rua
    while True:
        try:
            numero_rua = int(input("\nDigite o número do local em que você está: "))
            break
        except ValueError:
            print("\nDigite apenas números (exemplo: 608)")
    return distancia_km, endereco, numero_rua
