import os
import time
import random
import sys
from datetime import date

# ==========================
# FUNÇÕES DE UTILIDADE
# ==========================
def limpar_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def limpar_ultima_linha():
    sys.stdout.write('\x1b[1A')
    sys.stdout.write('\x1b[2K')
    sys.stdout.flush()

def mostrar_animacao():
    simbolos = ['▁','▂','▃','▄','▅','▆','▇','█']
    print(f"Carregando {random.choice(simbolos)} {random.choice(simbolos)} {random.choice(simbolos)} ", end="\r")
    time.sleep(0.2)
    print(" " * 30, end="\r")

# ==========================
# CARDÁPIO E FUNCIONÁRIOS
# ==========================
cardapio_base = [
    {"id": 1, "nome": "Guioza", 'preco': 19.99, "descricao": "Pastéis recheados com carne ou legumes, cozidos no vapor ou fritos."},
    {"id": 2, "nome": "Edamame", 'preco': 11.99, "descricao": "Vagem de soja cozida no vapor com flor de sal."},
    {"id": 3, "nome": "Harumaki", 'preco': 14.99, "descricao": "Rolinhos primavera fritos com recheios variados (legumes, queijo, carne)."},
    {"id": 4, "nome": "Missoshiru", 'preco': 27.99, "descricao": "Sopa de missô, feita com pasta de soja fermentada, dashi, tofu e cebolinha."}
]

lista_mesas = [
    {"id": 1, 'garcom': 'Alan Turing', 'clientes': 0, 'recebiveis': 0, 'mesa_uso': [], 'mesa_livre': list(range(1, 11))},
    {"id": 2, 'garcom': 'Grace Hopper', 'clientes': 0, 'recebiveis': 0, 'mesa_uso': [], 'mesa_livre': list(range(11, 21))},
    {"id": 3, 'garcom': 'Linus Torvalds', 'clientes': 0, 'recebiveis': 0, 'mesa_uso': [], 'mesa_livre': list(range(21, 31))},
    {"id": 4, 'garcom': 'Mc Bob Esponja', 'clientes': 0, 'recebiveis': 0, 'mesa_uso': [], 'mesa_livre': list(range(31, 41))}
]

# Lista global de pedidos
salao = []

# ==========================
# FUNÇÕES DE EXIBIÇÃO
# ==========================
def mostrar_cardapio():
    print(f'| Cardápio Online |'.center(100))
    print("--"*55)
    for prato in cardapio_base:
        print(f'[{prato["id"]}] - R$ {prato["preco"]:.2f} - {prato["nome"]} - {prato["descricao"]}')
    print("--"*55, '\n')
def mostrar_funcionarios(id_funcionario=""):
    print(f'| Lista de Funcionários e Mesas |'.center(100))
    print("--"*55)
    for func in lista_mesas:
        if id_funcionario == "" and len(func["mesa_livre"]) > 0:
            print(f'[{func["id"]}] - Garçom: {func["garcom"]}')
        elif id_funcionario == func["id"]:
            mesas_disp = " ".join([f"[{m}]" for m in func["mesa_livre"]])
            print(f'[{func["id"]}] - Garçom: {func["garcom"]} - Mesas disponíveis: {mesas_disp}')
    print("--"*55, '\n')

# ==========================
# TELAS DO SISTEMA
# ==========================
def tela_inicial():
    limpar_terminal()
    print(f'| MENU PRINCIPAL |'.center(100))
    print("--"*55)
    return int(input('[0] - Encerrar programa \n[1] - Cliente\n' + "-"*100 + '\n'))

def tela_cliente():
    while True:
        print(f'| Tela Cliente |'.center(100))
        print("--"*55)
        escolha = int(input('[0] - Voltar\n[1] - Cardápio\n[2] - Novo Pedido\n[3] - Meus Pedidos\n' + "-"*110 + '\n'))

        if escolha == 0:
            limpar_terminal()
            break
        elif escolha == 1:
            limpar_terminal()
            mostrar_cardapio()
            tela_cliente()
        elif escolha == 2:
            mostrar_animacao()
            limpar_terminal()
            novo_pedido()
            limpar_terminal()
        elif escolha == 3:
            limpar_terminal()
            mesa = int(input('Informe o número da mesa: '))
            resumo_pedidos(mesa)
        limpar_terminal()

# ==========================
# FUNÇÕES DE PEDIDOS
# ==========================
def novo_pedido():
    print(f'| Novo Pedido |'.center(100))
    print("=="*55, "\n")

    mostrar_funcionarios("")
    id_funcionario = int(input('Digite o número do garçom: ')) - 1

    limpar_terminal()
    print(f'| Novo Pedido |'.center(100))
    print("=="*55, "\n")
    mostrar_funcionarios(id_funcionario + 1)

    mesa = int(input('Digite o número da mesa: '))
    limpar_terminal()

    print(f'| Novo Pedido |'.center(100))
    print("=="*55, "\n")
    mostrar_cardapio()
    prato = int(input('Digite o número do prato: '))

    pedido_id = random.randint(1, 999)
    salao.append({
        'mesa': mesa,
        'id_func': lista_mesas[id_funcionario]["id"],
        'id_pedido': pedido_id,
        'id_prato': prato - 1,  # Corrigido índice
        'valor': cardapio_base[prato - 1]["preco"]
    })

    organizar_mesas(id_funcionario, mesa)

    print(f'| [✓] Pedido Concluído |'.center(100))
    print("--"*55, "\n")
    print(f'Nº do pedido: {pedido_id}\nGarçom: {lista_mesas[id_funcionario]["garcom"]}\nMesa: {mesa}')
    print(f'Prato: {cardapio_base[prato - 1]["nome"]} - {cardapio_base[prato - 1]["descricao"]}\nTotal: R$ {cardapio_base[prato - 1]["preco"]:.2f}\n')
    mostrar_animacao()
    input()

def organizar_mesas(id_funcionario, mesa):
    if mesa in lista_mesas[id_funcionario]["mesa_livre"]:
        lista_mesas[id_funcionario]["mesa_uso"].append(mesa)
        lista_mesas[id_funcionario]["mesa_livre"].remove(mesa)

def resumo_pedidos(mesa):
    print(f'| Tela de Pagamento |'.center(100))
    print("--"*55, "\n")

    total_a_pagar = 0.0
    pedidos_mesa = [item for item in salao if item["mesa"] == mesa]

    if not pedidos_mesa:
        print("Nenhum pedido encontrado para esta mesa.\n")
        input()
        return

    print(f'Mesa: {mesa} - Comanda nº {random.randint(999, 9999)} - {date.today()}\n'.center(100))
    print("--"*25)

    for i, item in enumerate(pedidos_mesa, start=1):
        prato = cardapio_base[item["id_prato"]]
        print(f'{i} - {prato["nome"]} - R$ {prato["preco"]:.2f}')
        total_a_pagar += item["valor"]

    print("--"*25)
    print(f'Total: R$ {total_a_pagar:.2f}\n')
    print("--"*55, "\n")

    escolha = int(input('[0] - Voltar\n[1] - Pagar\n'))

    if escolha == 1:
        # REMOÇÃO CORRIGIDA (modifica a lista original)
        salao[:] = [item for item in salao if item["mesa"] != mesa]
        print(f'| [✓] Pagamento Realizado! |'.center(100))
        print("--"*55, "\n")
        mostrar_animacao()
        input()

# ==========================
# LOOP PRINCIPAL
# ==========================
def main():
    while True:
        escolha = tela_inicial()
        limpar_terminal()
        if escolha == 1:
            mostrar_animacao()
            tela_cliente()
        else:
            limpar_terminal()
            print('Programa finalizado!'.center(100))
            break

if __name__ == "__main__":
    main()
