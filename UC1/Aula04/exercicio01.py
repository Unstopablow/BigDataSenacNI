#import random


try:
    watts_lampada = int(input(f'Digite a potência da lampada em Watts: \n'))
    largura = float(input(f'Digite a largura do cômodo: \n'))
    comprimento = float(input(f'Digite o comprimento do cômodo: \n'))
    metroquadrado = largura * comprimento
    qtd_lampada = int(metroquadrado/watts_lampada)

    if qtd_lampada < 1:
        qtd_lampada = 1
    
    print(f'O metro quadrado do cômodo é: {metroquadrado}m²')
    print(f'A quantidade de lampada no cômodo é: {qtd_lampada}')

except:
    print("Entrada inválida. Por favor, digite um número inteiro.")
