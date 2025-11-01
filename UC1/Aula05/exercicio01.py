# for i in range(5):
#     try:
#         print(f"Número {i + 1} de 5:")
#         num = float(input("Digite um número: "))
#         dobro = num * 2
#         triplo = num * 3
#         quádruplo = num * 4
#         print(f" Resultado: Dobro={dobro}, Triplo={triplo}, Quádruplo={quádruplo}\n")
#     except ValueError:
#         print(f'Entrada inválida. Tente novamente.')


contador = 0 # Inicializamos o contador
limite = 5 # Definimos o limite
while contador < limite: # A condição de parada: Enquanto o contador for menor que 5
    try:
        print(f"Número {contador + 1} de {limite}:")
        num = float(input("Digite um número: "))
        
        dobro = num * 2
        triplo = num * 3
        quadruplo = num * 4
        
        print(f" Resultado: Dobro={dobro}, Triplo={triplo}, Quádruplo={quadruplo}\n")
        print(type(dobro),type(triplo), type(quadruplo))
        contador = contador + 1 # IMPORTANTÍSSIMO! Incrementa o contador para evitar loop infinito
        
    except ValueError:
        print("Entrada inválida. Tente novamente.")
        # Não incrementamos o contador para dar nova chance ao usuário
