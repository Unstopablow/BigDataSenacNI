
import os
import time
import random

def limpar_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def mostrar_animacao():
    simbolos = [' ','.','.']
                
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

#salao = [{'mesa' : 0,'id_func':0, 'id_pedido':0,'prato':0}] GABARITO
salao =[]
matricula_funcionario = 123

def mostrar_cardapio(cardapio_base):
    print(f'| Cardapio online |'.center(100))
    print("--"*55)
    for i in range(len(cardapio_base)):
        print(f'[{cardapio_base[i]["id"]}] - R$ {cardapio_base[i]["preco"]} - {cardapio_base[i]["nome"]} - {cardapio_base[i]["descricao"]} ')
    print("--"*55,'\n')

def novo_pedido():
    mesa= int(input('Digite o numero da mesa\n'))
    prato = int(input('Digite o numero do prato\n'))-1
    pedido = 1
    salao.append({'mesa' : mesa,'id_func':matricula_funcionario, 'id_pedido':pedido,'id_prato':prato})
    print(salao)

def tela_inicial():
    limpar_terminal()
    print(f'| MENU PRINCIPAL |'.center(100))
    print("--"*55)
    return int(input(f'[0] - Cancelar \n[1] - Funcionarios \n[2] - Cliente\n--------------------------------------------------------------------------------------------------------------\n'))
    

def tela_cliente():
    print(f'| Tela cliente |'.center(100))
    print("--"*55)
    escolha = int(input(f'[0] - Voltar\n[1] - Cardápio\n[2] - Meus Pedidos \n[3] - Pagar\n--------------------------------------------------------------------------------------------------------------\n'))
    
    match escolha:
        case 1:
            limpar_terminal()
            mostrar_cardapio(cardapio_base)
            tela_cliente()
        case 2:
            resumo_pedidos(escolha := int(input(f'Qual o numero do pedido?\n')))
            mostrar_animacao()
            limpar_terminal()
        case 3:
            #resumo_pedidos(escolha := int(input(f'Qual o numero do pedido?\n')))
            novo_pedido()
            a = input()
            #mostrar_animacao()
            #limpar_terminal()
        case _:
            limpar_terminal()
            mostrar_animacao()                    
            limpar_terminal()
            
def resumo_pedidos(id_pedido):
    print(f'Em desenvolvimento')

def finalizar_pedidos(id_pedido):
    print(f'Em desenvolvimento')


#tela_inicial()
while True:
    escolha = tela_inicial()
    #print(escolha)
    limpar_terminal()
    match escolha:
        case 1:
            #limpar_terminal()
            novo_pedido()
        case 2:
            mostrar_animacao()
            tela_cliente()
            #limpar_terminal()
            #mostrar_cardapio(cardapio_base)
        case _:
            #limpar_terminal()
            limpar_terminal()
            print('Programa finalizado!')
            break














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