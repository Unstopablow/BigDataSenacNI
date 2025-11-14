
import random
import time 
import os


def limpar_tela():
    os.system('cls')


def voltar_menu():
    while True:
        escolha = input("Digite 9 para voltar ao menu: ")
        if escolha == "9":
            limpar_tela()
            break
        else:
            print(" Comando inválido. Digite 9 para voltar.")



def mostrar_cardapio(cardapio):
    print("══════════════════ CARDÁPIO ══════════════════\n")

    print('Comidas:')
    for id_item, dados in cardapio.items():
        if dados['categoria'] == 'Comida':
            print(f'[{id_item}] {dados["nome"]:<25} R$ {dados["preco"]:.2f}')
    print()

    print('Bebidas:')
    for id_item, dados in cardapio.items():
        if dados['categoria'] == 'Bebida':
            print(f'[{id_item}] {dados["nome"]:<25} R$ {dados["preco"]:.2f}')
    print()

    print('Sobremesas:')
    for id_item, dados in cardapio.items():
        if dados['categoria'] == 'Sobremesa':
            print(f'[{id_item}] {dados["nome"]:<25} R$ {dados["preco"]:.2f}')
    print()

    print("══════════════════════════════════════════════")



def fazer_pedido(cardapio, comanda):

    pedido_temp = []

    while True:
        mostrar_cardapio(cardapio)

        print("\nDigite o ID do item (0 para finalizar): ")
        try:
            id_escolhido = int(input("> "))
        except ValueError:
            print("Opção inválida. Digite apenas números.")
            continue

        if id_escolhido == 0:
            break

        if id_escolhido not in cardapio:
            print("ID inválido.")
            continue

        try:
            quantidade = int(input("Quantidade: "))
            if quantidade <= 0:
                print("Quantidade inválida.")
                continue
        except ValueError:
            print("Digite apenas números.")
            continue

        pedido_temp.append({
            "id": id_escolhido,
            "quantidade": quantidade
        })

        print("Item adicionado!\n")
        time.sleep(1)
        limpar_tela()

    if not pedido_temp:
        print("Nenhum item foi adicionado.")
        return

    limpar_tela()
    print("══════ RESUMO DO PEDIDO ══════")
    total_pedido = 0

    for item in pedido_temp:
        info = cardapio[item["id"]]
        nome = info["nome"]
        preco = info["preco"]
        qtd = item["quantidade"]
        subtotal = preco * qtd
        total_pedido += subtotal

        print(f"{qtd}x {nome:<25} R$ {subtotal:.2f}")

    print(f"\nTOTAL: R$ {total_pedido:.2f}")
    print("══════════════════════════════")

    while True:
        resposta = input("Confirmar pedido? (S/N): ").strip().upper()
        letras = "".join(ch for ch in resposta if ch.isalpha())

        if letras:
            primeira = letras[0]
            if primeira in ("S", "N"):
                break

        print("Digite apenas S ou N.")

    if primeira == "S":
        novo_pedido = {
            'status' : 'pendente',
            'itens': pedido_temp
        }
        comanda["pedidos"].append(novo_pedido)
        comanda["total"] += total_pedido
        print("\nPedido confirmado e enviado para o garçom!\n")
    else:
        print("\nPedido cancelado.\n")

    time.sleep(1)
    limpar_tela()



def ver_comanda(comanda, cardapio):
    limpar_tela()
    print(f"════════ COMANDA DA MESA {comanda['mesa']} ════════\n")

    if not comanda["pedidos"]:
        print("Nenhum pedido realizado ainda.")
        print("══════════════════════════════════")
        return

    total_geral = 0

    for i, pedido in enumerate(comanda["pedidos"], start=1):
        status = pedido["status"].capitalize()  
        print(f"PEDIDO {i} - Status: {status}")

        for item in pedido["itens"]:
            info = cardapio[item["id"]]
            nome = info["nome"]
            preco = info["preco"]
            qtd = item["quantidade"]
            subtotal = preco * qtd
            total_geral += subtotal

            print(f" - {qtd}x {nome} → R$ {subtotal:.2f}")

        print()

    print(f"TOTAL PARCIAL: R$ {total_geral:.2f}")
    print("══════════════════════════════════")




def fazer_pagamento(comanda, cardapio):
    limpar_tela()

    if not comanda["pedidos"]:
        print("Nenhum pedido foi realizado ainda.")
        time.sleep(1)
        limpar_tela()
        return
    
    print(f"════ PAGAMENTO - MESA {comanda['mesa']} ════\n")

    total_pagar = 0

    # Mostrando itens entregues e pendentes
    for pedido in comanda["pedidos"]:
        for item in pedido["itens"]:
            info = cardapio[item["id"]]
            nome = info["nome"]
            preco = info["preco"]
            qtd = item["quantidade"]
            subtotal = preco * qtd
            total_pagar += subtotal
            print(f"{qtd}x {nome:<25} R$ {subtotal:.2f}")

    print("\nTOTAL A PAGAR: R$ {:.2f}".format(total_pagar))
    print("════════════════════════════════════\n")

    print("Formas de pagamento:")
    print("1 - Dinheiro")
    print("2 - Pix")
    print("3 - Débito")
    print("4 - Crédito")
    print("9 - Voltar ao menu (sem pagar)\n")

    while True:
        opc = input("Escolha a forma de pagamento: ")

        if opc == "9":
            print("\nVoltando ao menu principal...\n")
            time.sleep(1.5)
            limpar_tela()
            return

        if opc not in ("1", "2", "3", "4"):
            print("Opção inválida.")
            continue

        break

    if opc == "4":  # cartão de crédito → parcelas
        while True:
            try:
                parcelas = int(input("Quantidade de parcelas (1 a 12): "))
                if parcelas < 1 or parcelas > 12:
                    print("Digite um número entre 1 e 12.")
                    continue
                break
            except ValueError:
                print("Digite apenas números.")

        valor_parcela = total_pagar / parcelas
        print(f"\nPagamento confirmado em {parcelas}x de R$ {valor_parcela:.2f}")

    else:
        print("\nPagamento confirmado!")

    comanda["status"] = "fechado"
    print("\nMuito obrigado por visitar o Tanoshimi!")
    

    time.sleep(1)
    limpar_tela()



def login_garcom():
    senha_correta = "1234"
    senha = input("Digite a senha do garçom: ")

    if senha == senha_correta:
        limpar_tela()
        return True
    else:
        print("Senha incorreta! Voltando ao menu...")
        time.sleep(1)
        limpar_tela()
        return False 


def gerenciar_entregas(comanda, cardapio):
    while True:
        limpar_tela()

        pendentes = [
            (index, pedido)
            for index, pedido in enumerate(comanda["pedidos"])
            if pedido["status"] == "pendente"
        ]

        print("=== PEDIDOS PENDENTES ===\n")

        if not pendentes:
            print("Nenhum pedido pendente no momento.")
            print("\nDigite 9 para voltar ao menu.")
            escolha = input("> ")
            if escolha == "9":
                limpar_tela()
                return
            else:
                continue

        mesa_atual = comanda["mesa"]

        for index_real, pedido in pendentes:
            print(f"Pedido {index_real + 1} — Mesa {mesa_atual}")
            for item in pedido["itens"]:
                nome = cardapio[item["id"]]["nome"]
                qtd = item["quantidade"]
                print(f" - {qtd}x {nome}")
            print()

        print("Digite o número do pedido entregue.")
        print("(Ou digite 9 para voltar ao menu)")

        escolha = input("> ")

        if escolha == "9":
            limpar_tela()
            return

        if not escolha.isdigit():
            print("Entrada inválida!")
            time.sleep(1)
            continue

        escolha = int(escolha)

        if 1 <= escolha <= len(comanda["pedidos"]):
            if comanda["pedidos"][escolha - 1]["status"] == "pendente":
                comanda["pedidos"][escolha - 1]["status"] = "entregue"
                print(f"\n✔ Pedido {escolha} marcado como entregue!\n")
            else:
                print("\nEste pedido já foi entregue!\n")
        else:
            print("\nPedido inexistente!\n")

        time.sleep(1)


def area_garcom(comanda, cardapio):
    if not login_garcom():
        return  

    while True:
        gerenciar_entregas(comanda, cardapio)
        return 



cardapio = {
    1: {"nome": "Sushi (10 peças)", "preco": 31.90, "categoria": "Comida"},
    2: {"nome": "Temaki", "preco": 27.90, "categoria": "Comida"},
    3: {"nome": "Sashimi (10 peças)", "preco": 31.90, "categoria": "Comida"},
    4: {"nome": "Yakisoba", "preco": 36.90, "categoria": "Comida"},
    5: {"nome": "Hot Roll (10 peças)", "preco": 31.90, "categoria": "Comida"},
    
    6: {"nome": "Água", "preco": 4.90, "categoria": "Bebida"},
    7: {"nome": "Refrigerante", "preco": 7.90, "categoria": "Bebida"},
    8: {"nome": "Suco", "preco": 8.90, "categoria": "Bebida"},
    
    9: {"nome": "Morango Fenômeno (8 un.)", "preco": 27.90, "categoria": "Sobremesa"},
    10: {"nome": "Harumaki M&M", "preco": 24.90, "categoria": "Sobremesa"},
    11: {"nome": "Brownie com sorvete", "preco": 29.90, "categoria": "Sobremesa"},
}




garcons= ['bruno', ' rafael', 'ana', 'lucas', 'marina', 'joao']

mesa= random.randint(1, 30)
garcom= random.choice(garcons)


print('='*50)
print('bem-vindo ao restaurante Tanoshimi'.center(50))
print('='*(50))
print(f'mesa: {mesa}')
print(f'garçom responsável: {garcom}')
print('='*50)

time.sleep(1)
limpar_tela()

comanda= {
    'mesa':mesa,
    'garcom':garcom,
    'pedidos':[],
    'status' : 'aberto',
    'total': 0.0
    
}

while True:
    print('='*50)
    print(' MENU PRINCIPAL'.center(40))
    print('='*50)
    print('1 - Ver cardapio e fazer pedido')
    print('2 - Ver status do pedido')
    print('3 - Fazer o pagamento')
    print('4 - Acesso do garçom')
    print('0 - sair')

    opcao = input('escolha uma opção:')

    limpar_tela()

    match opcao:

        case '1':
            print('>>> Entrando no cardapio...\n')
            time.sleep(1)
            limpar_tela()
            fazer_pedido(cardapio,comanda)

            voltar_menu()

        case '2':
            print('>>> Status do pedido...\n')
            time.sleep(1)
            limpar_tela()
            ver_comanda(comanda,cardapio)

            voltar_menu()

        case '3':
            print('>>> Iniciando pagamento...\n')
            time.sleep(1)
            limpar_tela()
            fazer_pagamento(comanda,cardapio)
        
            voltar_menu()

        case '4':
            print('>>> Acesso do garçon...')
            time.sleep(1)
            limpar_tela()
            area_garcom(comanda,cardapio)

            voltar_menu()

        case '0':
            if comanda["pedidos"] and comanda["status"] == "aberto":
                    print(" Você precisa realizar o pagamento antes de sair!")
                    time.sleep(2)
                    limpar_tela()
                    continue
            
            print('=' * 50)
            print(' Muito obrigado por visitar o Tanoshimi '.center(50))
            print(' Volte sempre! '.center(50))
            print('=' * 50)
            break
        