
import os, time, random, sys
from datetime import date

def limpar_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def limpar_ultima_linha():
    # Move o cursor 1 linha para cima
    sys.stdout.write('\x1b[1A')
    # Limpa a linha inteira
    sys.stdout.write('\x1b[2K')
    sys.stdout.flush()

def mostrar_animacao():
    #simbolos = [' ','.','.']
    simbolos = ['▁','▂','▃','▄','▅','▆','▇','█']
                
    for _ in range(5):
        print(f"Carregando {random.choice(simbolos)} {random.choice(simbolos)} {random.choice(simbolos)} ", end="\r")
        time.sleep(0.2)
    print(" " * 20, end="\r")

cardapio_base = [
    {"id" : 1,"nome" : "Guioza", 'preco':'19.99',"descricao" : "Pastéis recheados com carne ou legumes, cozidos no vapor ou fritos."},
    {"id" : 2,"nome" : "Edamame", 'preco':'11.99' ,"descricao" : "Vagem de soja cozida no vapor com flor de sal."},
    {"id" : 3,"nome" : "Harumaki", 'preco':'14.99' ,"descricao" : "Rolinhos primavera fritos com recheios variados (legumes, queijo, carne)."},
    {"id" : 4,"nome" : "Missoshiru", 'preco':'27.99' ,"descricao" : " Sopa de missô, feita com pasta de soja fermentada, dashi, tofu e cebolinha."}
    ]

total_a_pagar = 0.0
salao = []
'''Armazena [{'mesa' : 0,'id_func':0, 'id_pedido':0,'id_prato':0,'valor':0}]'''

lista_mesas = [
    {"id" : 1,'garcom' : 'Alan Turing', 'clientes':0,'recebiveis':0,'mesa_uso':[],'mesa_livre':[1,2,3,4,5,6,7,8,9,10]},
    {"id" : 2,'garcom' : 'Grace Hopper', 'clientes':0,'recebiveis':0,'mesa_uso':[],'mesa_livre':[11,12,13,14,15,16,17,18,19,20]},
    {"id" : 3,'garcom' : 'Linus Torvalds', 'clientes':0,'recebiveis':0,'mesa_uso':[],'mesa_livre':[21,22,23,24,25,26,27,28,29,30]},
    {"id" : 4,'garcom' : 'Mc Bob Esponja', 'clientes':0,'recebiveis':0,'mesa_uso':[],'mesa_livre':[31,32,33,34,35,36,37,38,39,40]}
    ]
'''Dicionario de mesas e funcionarios'''

def mostrar_cardapio(cardapio_base):
    print(f'| Cardapio online |'.center(100))
    print("--"*55)
    for i in range(len(cardapio_base)):
        print(f'[{cardapio_base[i]["id"]}] - R$ {cardapio_base[i]["preco"]} - {cardapio_base[i]["nome"]} - {cardapio_base[i]["descricao"]} ')
    print("--"*55,'\n')

def mostrar_funcionarios(id_funcionario):
    print(f'| Lista de funcionarios e lugares |'.center(100))
    print("--"*55)
    for i in range(len(lista_mesas)):
        #print(lista_mesas[i]["id"])
        if id_funcionario == "" and len(lista_mesas[i]["mesa_livre"]) > 0:
            print(f' [{lista_mesas[i]["id"]}] - Garçom: {lista_mesas[i]["garcom"]}')

        elif id_funcionario == lista_mesas[i]["id"]:
            print(f' [{lista_mesas[i]["id"]}] - Garçom: {lista_mesas[i]["garcom"]} - Mesas disponiveis: ', end="")
            for j in lista_mesas[i]["mesa_livre"]:
                print(f'[{j}]',end="")
            print()


    print("--"*55,'\n')

def tela_inicial():
    limpar_terminal()
    print(f'| MENU PRINCIPAL |'.center(100))
    print("--"*55)
    #return int(input(f'[0] - Encerrar programa \n[1] - Funcionarios \n[2] - Cliente\n--------------------------------------------------------------------------------------------------------------\n'))
    return int(input(f'[0] - Encerrar programa \n[1] - Cliente\n--------------------------------------------------------------------------------------------------------------\n'))

def tela_cliente():
    print(f'| Tela cliente |'.center(100))
    print("--"*55)
    escolha = int(input(f'[0] - Voltar\n[1] - Cardápio\n[2] - Novo Pedido \n[3] - Meus pedidos\n--------------------------------------------------------------------------------------------------------------\n'))
    
    match escolha:
        case 1: #Cardapio
            limpar_terminal()
            mostrar_cardapio(cardapio_base)
            tela_cliente()
        case 2: #Novo pedido
            mostrar_animacao()
            limpar_terminal()
            novo_pedido()
            limpar_terminal()
        case 3: #Meus pedidos
            limpar_terminal()
            mesa = int(input(f'Informe o numero da mesa\n'))
            resumo_pedidos(mesa, salao)
        case _: #Voltar
            limpar_terminal()
            mostrar_animacao()                    
            limpar_terminal()

def novo_pedido():
    print(f'| Novo pedido |'.center(100))
    print("=="*55,"\n")
    mostrar_funcionarios("")
    id_funcionario = int(input('Digite o numero do garçom:\n'))-1
    limpar_terminal()
    print(f'| Novo pedido |'.center(100))
    print("=="*55,"\n")
    mostrar_funcionarios(id_funcionario+1)
    mesa= int(input('Digite o numero da mesa\n'))
    limpar_terminal()
    print(f'| Novo pedido |'.center(100))
    print("=="*55,"\n")
    mostrar_cardapio(cardapio_base)
    print(f'[✓] Resumo: Garçom: {lista_mesas[id_funcionario]["garcom"]} - Mesa: {mesa}\n')
    prato = int(input('Digite um numero para escolher o prato:\n'))
    pedido = random.randint(1, 999)
    salao.append({'mesa' : mesa,'id_func': lista_mesas[id_funcionario]["id"], 'id_pedido':pedido,'id_prato':prato,'valor': float(cardapio_base[prato]["preco"])})
    limpar_terminal()
    organizar_mesas(id_funcionario,mesa)

    print(f'| [✓] Pedido concluido! |'.center(100))
    print("--"*55,"\n")
    #print(f'Nº do pedido: {pedido} - Garçom: {lista_mesas[id_funcionario]["garcom"]} - Mesa: {mesa}')
    print(f'Nº do pedido: {pedido} \nGarçom: {lista_mesas[id_funcionario]["garcom"]} \nMesa: {mesa}')
    print(f'Prato: {cardapio_base[prato]["nome"]} - {cardapio_base[prato]["descricao"]} \nTotal: {cardapio_base[prato]["preco"]}\n')
    mostrar_animacao()
    #print(salao)
    #input()
    tela_cliente()

def organizar_mesas(id_funcionario,mesa):
    lista_mesas[id_funcionario]["mesa_uso"].append(mesa)
    lista_mesas[id_funcionario]["mesa_livre"].remove(mesa)

def resumo_pedidos(mesa,salao):
    print(f'| Tela de pagamento |'.center(100))
    print("--"*55,"\n")
    total_a_pagar = 0.0
    print(f'Mesa: 1 - Garçom - Comanda nº {random.randint(999, 9999)} - {date.today()}\n'.center(100))
    print("--"*25)
    for i in range(len(salao)):
        if salao[i]["mesa"] == mesa:
            print(f'{i+1} - {cardapio_base[salao[i]["id_prato"]]["nome"]} - {cardapio_base[salao[i]["id_prato"]]["preco"]}')
            sub_total = salao[i]["valor"]
            total_a_pagar += sub_total
    print("--"*25,"\n")
    print(f'Total: R$ {total_a_pagar}\n')

    print("--"*55,"\n")
    escolha = int(input(f'[0] - Voltar\n[1] - Pagar\n'))
    
    match escolha:
        case 1: #Fechar pedidos
            print(salao)
            #salao = [item for item in salao if item["mesa"] != mesa]
            salao[:] = [item for item in salao if item["mesa"] != mesa]
            #input()
            #limpar_terminal()
            print(f'| Tela de pagamento |'.center(100))
            print("--"*55,"\n")
            print(f'| [✓] Pagamento realizado! |'.center(100))
            print("--"*55,"\n")
            print(salao)
            mostrar_animacao()
            input()
            return salao
        case _: #Voltar
            limpar_terminal()
            tela_cliente()
    return salao
# def fechar_pedidos(mesa,salao):
#     salao = [item for item in salao if item["mesa"] != mesa]
#     return salao

while True:

    escolha = tela_inicial()
    #print(escolha)
    limpar_terminal()
    match escolha:
        case 1:
            mostrar_animacao()
            tela_cliente()
        case _:
            #limpar_terminal()
            limpar_terminal()
            print('Programa finalizado!')
            break



























#resumo_pedidos(escolha := int(input(f'Qual o numero do pedido?\n')))
# def resumo_pedidos(id_pedido):
#     print(f'Em desenvolvimento')

# ====== codigo morto ================= RIP ========================












# def novo_pedido(mesa,pedido):
#     for i in range(len(salao)):
#         if salao[i]['mesa'] == mesa:


#tela_inicial()
#mostrar_cardapio()


# while True:

#     if input(f'0 para sair') == 0:
#         break
#     else:
#         salao.append({})



#salao = [{'mesa' : 0,'id_func':0, 'qtd_pedidos':0,'price':0}]
#historico_pedidos = [{'id_pedido': 0,'prato':0}]
# def pedidos():
#     mesa= int(input('Digite o numero da mesa\n'))
#     prato = int(input('Digite o numero do prato\n'))-1
#     pedido = 1
#     novo_pedido(mesa,prato,pedido)


#     preco = cardapio_base[pedido]["preco"]
#     salao.append({'mesa' : 0,'id_func':0, 'id_pedido':0,'prato':0})

# while True:
#     condicao = int(input(f'\n[0] - Para finalizar \n[1] - Para continuar\n'))== 0
#     if condicao:
#         print('Pedido finalizado!')
#         break
#     else:
#         novo_pedido()