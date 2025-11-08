import random

def dado(numero_de_lados):
    face = random.randint(1,numero_de_lados)
    return face

print("="*40)
print("SIMULADOR DE BATALHA")
print("="*40)

input('Pressione qualquer tecla (enter) para rodar o ataque')
d20 = dado(20)
print(f'Valor:',d20)
input('Pressione qualquer tecla (enter)para rodar o dano')
d8 = dado(8)
print(f'Valor:',d8)
print(f'\n')

print(f'Primeiro valor:', d20)
print(f'Segundo valor:', d20)