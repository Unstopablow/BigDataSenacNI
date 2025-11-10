texto_base = input(f'Digite uma palavra:\n').lower()
letra_procurada = input(f'Escolha uma letra:\n').lower()
contador = 0

for i in texto_base:
    if i == letra_procurada:
        contador += 1

print(f'A letra {letra_procurada} aparece ',contador,'x na palavra',texto_base)