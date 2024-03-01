#Algorítmo para o processo seletivo da Encora Brasil: Infinite Coins.

#Atribuição do número de moedas fornecidas pelo usuário a uma variável
total_centavos = int(input("Digite a quantidade de moedas possuídas: "))

def fazerTroco(total_centavos):
    # Criação do conjunto para armazenar as possibilidades
    conjunto_resultado = set()

    # Loop para iterar sobre as diferentes quantidades de moedas de 25 centavos (quarters)
    for moeda_de_25 in range(total_centavos + 1):
        # Loop para iterar sobre as diferentes quantidades de moedas de 10 centavos (dimes)
        for moeda_de_10 in range(total_centavos // 10 + 1):
            # Loop para iterar sobre as diferentes quantidades de moedas de 5 centavos(nickles)
            for moeda_de_5 in range(total_centavos // 5 + 1):
                # Calcular a quantidade de moedas de 1 centavo (Pennies)
                moeda_de_1 = total_centavos - (moeda_de_25 * 25 + moeda_de_10 * 10 + moeda_de_5 * 5)

                # Verifição para saber se a quantidade de moedas de 1 centavo é ou não negativa
                if moeda_de_1 >= 0:
                    # Adicionar ao conjunto de resultados possíveis
                    conjunto_resultado.add((moeda_de_25, moeda_de_10, moeda_de_5, moeda_de_1))

    return conjunto_resultado

# Chamar a função e armazenar o resultado
resultado = fazerTroco(total_centavos)

# Imprimir no terminal o resultado de possíveis combinações
print(resultado)
