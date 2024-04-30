
def imprimir_informacoes(nome, idade, cidade):
    print("Nome:", nome, sep=" ", end=", ")
    print("Idade:", idade, sep=" ", end=", ")
    print("Cidade:", cidade, sep=" ", end="\n")
    # Exemplo de uso da função
nome = "João"
idade = 30
cidade = "São Paulo"
imprimir_informacoes(nome, idade, cidade)

#def calcular_operacao():
    # Solicita ao usuário os dois números e a operação desejada
#   num1 = float(input("Digite o primeiro número: "))
 #   num2 = float(input("Digite o segundo número: "))
  #  operacao = input("Digite a operação desejada (+, -, *, /): ")

    # Verifica a operação e calcula o resultado
#    if operacao == '+':
 #       resultado = num1 + num2
  #  elif operacao == '-':
   #     resultado = num1 - num2
    #elif operacao == '*':
     #   resultado = num1 * num2
   # elif operacao == '/':
        # Verifica se o segundo número não é zero para evitar divisão por zero
    #    if num2 != 0:
     #       resultado = num1 / num2
      #  else:
       #     print("Erro: divisão por zero.")
        #    return

    # Imprime o resultado da operação
    #print("O resultado de {} {} {} é: {}".format(num1, operacao, num2, resultado))

# Exemplo de uso da função
#calcular_operacao()

#def lista_de_compras():
    # Solicita ao usuário os itens da lista de compras
 #   entrada = input("Digite os itens da lista de compras, separados por vírgula: ")

    # Divide a entrada em uma lista de itens
  #  itens = entrada.split(',')

    # Imprime os itens em linhas separadas usando um laço
   # for i, item in enumerate(itens, 1):
    #    print("Item {}: {}".format(i, item.strip()))

# Exemplo de uso da função
#lista_de_compras()

#def converter_para_fahrenheit():
    # Solicita ao usuário a temperatura em graus Celsius
 #   celsius = float(input("Digite a temperatura em graus Celsius: "))

    # Converte a temperatura de Celsius para Fahrenheit usando a fórmula
  #  fahrenheit = (celsius * 9/5) + 32

    # Imprime o resultado
   # print("A temperatura em Fahrenheit é:", fahrenheit)

# Exemplo de uso da função
#converter_para_fahrenheit()

def obter_nomes():
    nomes = []  # Lista para armazenar os nomes

    # Loop infinito até que 'sair' seja digitado
    while True:
        nome = input("Digite um nome ou 'sair' para encerrar: ")
        if nome.lower() == 'sair':
            break  # Sai do loop se 'sair' for digitado
        nomes.append(nome)  # Adiciona o nome à lista

    # Imprime todos os nomes digitados
    for nome in nomes:
        print(nome)

# Exemplo de uso da função
obter_nomes()

