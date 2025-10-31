print("\n")
texto1 = "# Exercicio (3º) - Rendimento do Taxista. #"
print(texto1.upper())
print("\n")

# Um motorista de táxi deseja calcular o rendimento de seu carro na praça. Sabendo-se que o
# preço do combustível é de R$ 6,15, escreva um programa para ler: a marcação do
# odômetro (km) no início do dia, a marcação (km) no final do dia, o número de litros de
# combustível gasto e o valor total (R$) recebido dos passageiros. Calcular e escrever: a
# média do consumo em km/L e o lucro (líquido) do dia.

odometro_inicial = int(input("Digite o Km inicial: "))
odometro_final = int(input("Digite o Km final: "))
autonomia = int(input("Digite o consumo médio do veiculo: "))
credito = int(input("Digite o valor total recebido: "))

km_rodado = odometro_final - odometro_inicial
gas_gasto = float(km_rodado/autonomia)
custo_gas = int(gas_gasto * 6.15)
lucro = credito-custo_gas

print('')
print(f'Km rodados {km_rodado}')
print(f'Combustível utilizado {gas_gasto:.2f} ')
print(f'Valor gasto com combustível: R$ {custo_gas}')
print(f'Lucro do dia: R$ {lucro}')