def ano_bissexto(ano):
    div4 = ano % 4 == 0
    div100 = ano % 100 == 0
    div400 = ano % 400 == 0
    if div4 & div100 & div400:
        print(f'{ano} é bissexto')
    else:
        print(f'{ano} não é bissexto') 

while True:
    try:
        if escolher := int(input(f'Cancelar digite (0) | Continuar (1)\n')) == 0:
            print(f'Programa encerrado')
            break
        else:
            ano_bissexto(ano := int(input(f'Fala um ano ai\n')))
    except ValueError:
        print()