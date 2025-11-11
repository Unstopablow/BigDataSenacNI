# 1. Controle de Pesca
# Crie um programa que ajude um pescador a controlar sua produtividade. Toda vez que ele
# traz um peso de peixes maior que o estabelecido pelo regulamento (100 quilos), ele deve
# pagar uma multa de R$ 4,00 por quilo excedente.
# ● O programa deve ler o peso de peixes (em quilos) pescado no dia.
# ● Você deve criar uma função (ex: calcular_multa(peso_total)) que recebe o peso e
# retorna o valor da multa (que pode ser 0.0 se estiver dentro do limite).
# ● Se o valor da multa retornado for maior que zero, mostre a multa.
# ● Caso contrário, mostre a mensagem "Peso dentro do limite. Nenhuma multa a
# pagar."
# ● Pergunte o peso de várias pescarias feitas ao longo da semana. O loop para quando
# o usuário digitar 0. Ao final, mostre o total de multa acumulado no dia.

multa_acumulada = 0
def calcular_multa(peso_total):
    limite = 100
    multa = 4

    if peso_total > limite:
        excesso = peso_total - limite
        return multa * excesso      
    
    elif peso_total<=0:
        return 0
        
    else:
        return 0

while True:
    try:
        if escolher := int(input(f'Cancelar digite (0) | Continuar (1) \n'.center(50))) == 0:
            print(f'Programa encerrado')
            break
        else:
            multa_atual = calcular_multa(float(input(f'Digite o peso do peixe: \n'.center(50))))
            multa_acumulada += multa_atual 
            print(f'Você foi multado em: {multa_atual}'.center(50))
    except ValueError:
        print()



print(f'Total de multa acumulada'.center(50),multa_acumulada)