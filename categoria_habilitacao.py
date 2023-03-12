# Desenvolva um código na linguagem Python, que utilize as seguintes características de um veículo:
# - Quantidade de rodas;
# - Peso bruto em quilogramas;
# - Quantidade de pessoas no veículo.

# Com essas informações, o programa mostrará qual é a melhor categoria de habilitação para o veículo informado a partir das condições:

# A: Veículos com duas ou três rodas;
# B: Veículos com quatro rodas, que acomodam até oito pessoas e seu peso é de até 3500 kg;
# C: Veículos com quatro rodas ou mais e com peso entre 3500 e 6000 kg;
# D: Veículos com quatro rodas ou mais e que acomodam mais de oito pessoas; E: Veículos com quatro rodas ou mais e com mais de 6000 kg. 

def categoria_habilitacao(qtd_rodas, peso, qtd_pessoas):
    if qtd_rodas == 2 or qtd_rodas == 3:
        return "Categoria A"
    elif qtd_rodas == 4 and qtd_pessoas <= 8 and peso <= 3500:
        return "Categoria B"
    elif qtd_rodas >= 4 and peso > 3500 and peso <= 6000:
        return "Categoria C"
    elif qtd_rodas >= 4 and qtd_pessoas > 8:
        return "Categoria D"
    elif qtd_rodas >= 4 and peso > 6000:
        return "Categoria E"
    else:
        return "Veículo não classificado"

qtd_rodas = int(input("Informe a quantidade de rodas: "))
peso = float(input("Informe o peso bruto em quilogramas: "))
qtd_pessoas = int(input("Informe a quantidade de pessoas no veículo: "))

categoria = categoria_habilitacao(qtd_rodas, peso, qtd_pessoas)

print(f"A categoria de habilitação para o veículo informado é: {categoria}")

