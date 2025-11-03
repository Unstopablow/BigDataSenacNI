contador = 1
limite = 3
senha = 1234
str(input(f'Digite o nome do usuario:'))

while contador <= limite:
    try:        
        tentativa = int(input(f'Digite a senha:'))
        if tentativa != senha:
            print('Senha incorreta')
            print(f'Tentativas restantes {limite - contador}')
            
        elif tentativa == senha:
            print('Senha correta')
            break
        contador += 1
    except ValueError:
        print("Entrada inválida. Tente novamente.")    
