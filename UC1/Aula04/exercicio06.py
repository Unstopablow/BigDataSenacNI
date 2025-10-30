import random

try:
    n1 = int(random.uniform(-100, 100))

    if n1 >= 0:  
        print(f'O valor {n1} é positivo.')
    elif n1 < 0:
        print(f'O valor {n1} é negativo.')

except:
    print("Entrada inválida. Por favor, digite um número inteiro.")
