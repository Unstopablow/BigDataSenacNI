contador = 1
limite = 3
senha = 1234
usuario = "Pablo"

while contador <= limite:
    try:        
        user = str(input(f'Digite o nome do usuario:'))
        password = int(input(f'Digite a senha:'))
        print("\n","="*60,"\n")
        if password != senha and user != usuario:
            print('Usuario ou senha invalidos')
            print(f'Tentativas restantes {limite - contador}')
            print("\n","="*60,"\n")
        elif password != senha or user != usuario:
            print('Usuario ou senha invalidos')
            print(f'Tentativas restantes {limite - contador}')
            print("\n","="*60,"\n")       
        elif password == senha:
            print('Senha correta')
            break
        contador += 1
    except ValueError:
        print("Entrada inválida. Tente novamente.")    
if contador == 0:        
    print("", "="*19)
    print("| Acabou a tentativa |")
    print("", "="*19)