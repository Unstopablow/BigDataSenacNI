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

def mostrar_animacao():
    simbolos = ['▁','▂','▃','▄','▅','▆','▇','█']
    print(f"Carregando {random.choice(simbolos)} {random.choice(simbolos)} {random.choice(simbolos)} ", end="\r")
    time.sleep(0.2)
    print(" " * 30, end="\r")

def input_int(mensagem, min_val=None, max_val=None):
    """Solicita um número inteiro com tratamento de erros e limites opcionais."""
    while True:
        try:
            valor = int(input(mensagem))
            if min_val is not None and valor < min_val:
                print(f"Digite um número maior ou igual a {min_val}.")
                continue
            if max_val is not None and valor > max_val:
                print(f"Digite um número menor ou igual a {max_val}.")
                continue
            return valor
        except ValueError:
            print("Entrada inválida! Digite apenas números inteiros.")

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
    {"id": 1, 'garcom': 'Alan Turing', 'clientes': 0, 'recebiveis': 0, 'mesa_uso': [], 'mesa_livre': list(range(1, 10 + 1))},
    {"id": 2, 'garcom': 'Grace Hopper', 'clientes': 0, 'recebiveis': 0, 'mesa_uso': [], 'mesa_livre': list(range(11, 20 + 1))},
    {"id": 3, 'garcom': 'Linus Torvalds', 'clientes': 0, 'recebiveis': 0, 'mesa_uso': [], 'mesa_livre': list(range(21, 30 + 1))},
    {"id": 4, 'garcom': 'Mc Bob Esponja', 'clientes': 0, 'recebiveis': 0, 'mesa_uso': [], 'mesa_livre': list(range(31, 40 + 1))}
]

# Lista global de pedidos
salao = []

# ==========================
# EXIBIÇÃO
# ==========================
def mostrar_cardapio():
    print(f'| Cardápio Online |'.center(100))
    print("--" * 55)
    for prato in cardapio_base:
        print(f'[{prato["id"]}] - R$ {prato["preco"]:.2f} - {prato["nome"]} - {prato["descricao"]}')
    print("--" * 55, '\n')

def mostrar_funcionarios(id_escolhido=None):
    print(f'| Funcionários e Mesas |'.center(100))
    print("--" * 55)

    for func in lista_mesas:
        if id_escolhido is None:
            print(f'[{func["id"]}] - {func["garcom"]}')
        elif func["id"] == id_escolhido:
            mesas = " ".join(f"[{m}]" for m in func["mesa_livre"])
            print(f'{func["garcom"]} - Mesas disponíveis: {mesas}')

    print("--" * 55)

# ==========================
# TELAS
# ==========================
def tela_inicial():
    limpar_terminal()
    print(f'| MENU PRINCIPAL |'.center(100))
    print("--" * 55)
    return input_int("[0] - Sair\n[1] - Cliente\n", 0, 1)

def tela_cliente():
    while True:
        print(f'| MENU DO CLIENTE |'.center(100))
        print("--" * 55)

        escolha = input_int(
            "[0] - Voltar\n[1] - Cardápio\n[2] - Novo Pedido\n[3] - Meus Pedidos\n",
            0, 3
        )

        if escolha == 0:
            limpar_terminal()
            return

        if escolha == 1:
            limpar_terminal()
            mostrar_cardapio()

        if escolha == 2:
            limpar_terminal()
            novo_pedido()

        if escolha == 3:
            limpar_terminal()
            mesa = input_int("Informe o número da mesa: ")
            resumo_pedidos(mesa)

        input("\nPressione Enter para continuar...")
        limpar_terminal()

# ==========================
# PEDIDOS
# ==========================
def escolher_garcom():
    mostrar_funcionarios()
    while True:

        num = input_int("[0] - Retornar | informe o número do garçom: ", 0, len(lista_mesas))
        if num == 0:
            limpar_terminal()
            tela_cliente()
            break
        else:
            return num - 1

def escolher_mesa(id_func):
    func = lista_mesas[id_func]

    if not func["mesa_livre"]:
        print("⚠ Este garçom não tem mesas livres!")
        return None

    print("\nMesas disponíveis:")
    print(" ".join(f"[{m}]" for m in func["mesa_livre"]))

    while True:
        m = input_int("[0] - Retornar | Escolha uma mesa: ")
        if m == 0:
            limpar_terminal()
            escolher_garcom()
            

        if m in func["mesa_livre"]:
            return m
        else:
            print("Mesa inválida ou já ocupada!")

def escolher_prato():
    mostrar_cardapio()
    return input_int("Escolha um prato: ", 1, len(cardapio_base)) - 1

def novo_pedido():
    print(f'| NOVO PEDIDO |'.center(100))
    print("--" * 55)

    id_func = escolher_garcom()

    limpar_terminal()
    mostrar_funcionarios(id_func + 1)

    mesa = escolher_mesa(id_func)
    if mesa is None:
        return

    prato = escolher_prato()

    pedido_id = random.randint(1000, 9999)

    salao.append({
        "mesa": mesa,
        "id_func": lista_mesas[id_func]["id"],
        "id_pedido": pedido_id,
        "id_prato": prato,
        "valor": cardapio_base[prato]["preco"]
    })

    organizar_mesas(id_func, mesa)

    print("\n✓ Pedido registrado com sucesso!")
    print(f"Pedido nº: {pedido_id}")
    print(f"Prato: {cardapio_base[prato]['nome']}")
    print(f"Mesa: {mesa}")

def organizar_mesas(id_func, mesa):
    lf = lista_mesas[id_func]["mesa_livre"]
    if mesa in lf:
        lf.remove(mesa)
        lista_mesas[id_func]["mesa_uso"].append(mesa)

def resumo_pedidos(mesa):
    pedidos = [p for p in salao if p["mesa"] == mesa]

    if not pedidos:
        print("Nenhum pedido encontrado para esta mesa.")
        return

    print(f'| PAGAMENTO | Mesa {mesa} |'.center(100))
    print("--" * 55)

    total = 0
    for i, p in enumerate(pedidos, 1):
        prato = cardapio_base[p["id_prato"]]
        print(f"{i} - {prato['nome']} - R$ {prato['preco']:.2f}")
        total += prato['preco']

    print("--" * 55)
    print(f"TOTAL: R$ {total:.2f}")

    pagar = input_int("\n[0] - Voltar\n[1] - Pagar\n", 0, 1)

    if pagar == 1:
        salao[:] = [p for p in salao if p["mesa"] != mesa]
        print("\n✓ Pagamento efetuado! Mesa liberada.")

# ==========================
# LOOP PRINCIPAL
# ==========================
def main():
    while True:
        escolha = tela_inicial()
        limpar_terminal()

        if escolha == 1:
            tela_cliente()
        else:
            print("Programa encerrado.")
            break

if __name__ == "__main__":
    main()
