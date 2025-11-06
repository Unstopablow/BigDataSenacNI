import random

def origem_produtos():
    print("\n")
    texto1 = "# Exercicio (4º) - Código de Origem do Produto. #"
    print(texto1.upper())
    print("\n")

    # Escreva um programa que leia o código de origem de um produto e imprima na tela a região
    # de sua procedência, conforme a tabela abaixo:
    # Observação: caso o código não seja nenhum dos especificados, o produto deve ser

    # encarado como “Importado”.
    print(f' -----------------------------------------------------')
    print(f'|Código 1 = Sul             |  Código 2 = Norte       |')
    print(f'|Código 3 = Leste           |  Código 4 = Oeste       |')
    print(f'|Código 5,6 = Nordeste      |  Código 7,8,9= Sudeste  |')
    print(f'|Código 10 = Centro-Oeste   |  Código 11 = Noroeste   |')
    print(f'|Código ? = Importado                                 |')
    print(f' -----------------------------------------------------\n')



    while True:
        try:
            Codigo_Regiao = int(input("Digite um número: "))
            match Codigo_Regiao:
                case 1:
                    print(f'Região sul')
                    break
                case 2:
                    print(f'Região norte')
                    break
                case 3:
                    print(f'Região leste')
                    break
                case 4:
                    print(f'Região Oeste')
                    break 
                case 5|6:
                    print(f'Nordeste')
                    break 
                case 7|8|9:
                    print(f'Sudeste')
                    break 
                case 10:
                    print(f'Centro-Oeste')
                    break 
                case 11:
                    print(f'Noroeste')
                    break 
                case _:
                    print(f'Importado')
                    break 
        except ValueError:
            print(f'Insira um numero') 
origem_produtos()