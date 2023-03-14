# Faça uma função calculadora que os números e as operações serão feitas pelo  usuário. O código deve ficar rodando infinitamente até que o usuário escolha a # opção de sair. No início, o programa mostrará a seguinte lista de operações:

# 1: Soma
# 2: Subtração
# 3: Multiplicação
# 4: Divisão
# 0: Sair

# Digite o número para a operação correspondente e caso o usuário introduza # qualquer outro, o sistema deve mostrar a mensagem “Essa opção não existe” e # voltar ao menu de opções.

# Após a seleção, o sistema deve pedir para o usuário inserir o primeiro e # segundo valor, um de cada. Depois precisa executar a operação e mostrar o # resultado na tela. Quando o usuário escolher a opção “Sair”, o sistema irá # parar.

# É necessário que o sistema mostre as opções sempre que finalizar uma operação e mostrar o resultado. 

## Para atender a solicitação, você pode criar uma função calculadora que exibe o  menu de opções, lê a entrada do usuário e executa a operação escolhida,   repetindo o processo até que o usuário selecione a opção de sair. Veja o código abaixo: ##

def calculadora():
    while True:
        print("Escolha a operação que deseja realizar:")
        print("1: Soma")
        print("2: Subtração")
        print("3: Multiplicação")
        print("4: Divisão")
        print("0: Sair")

        # Lê a entrada do usuário
        opcao = int(input())

        # Verifica a opção escolhida
        if opcao == 0:
            # Sai do loop
            print("Encerrando a calculadora...")
            break
        elif opcao == 1:
            # Soma
            num1 = float(input("Digite o primeiro valor: "))
            num2 = float(input("Digite o segundo valor: "))
            resultado = num1 + num2
            print(f"Resultado: {resultado}")
        elif opcao == 2:
            # Subtração
            num1 = float(input("Digite o primeiro valor: "))
            num2 = float(input("Digite o segundo valor: "))
            resultado = num1 - num2
            print(f"Resultado: {resultado}")
        elif opcao == 3:
            # Multiplicação
            num1 = float(input("Digite o primeiro valor: "))
            num2 = float(input("Digite o segundo valor: "))
            resultado = num1 * num2
            print(f"Resultado: {resultado}")
        elif opcao == 4:
            # Divisão
            num1 = float(input("Digite o primeiro valor: "))
            num2 = float(input("Digite o segundo valor: "))
            if num2 == 0:
                print("Erro: divisão por zero!")
            else:
                resultado = num1 / num2
                print(f"Resultado: {resultado}")
        else:
            # Opção inválida
            print("Essa opção não existe. Tente novamente.")

        print(" ")  # Pula uma linha para separar a saída das operações

        # chame a função 'calculadora()' para rodar o código. #

        

