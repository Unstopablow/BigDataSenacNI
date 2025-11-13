import random

# --- 1. NOSSOS "BANCOS DE DADOS" GLOBAIS ---
# (Ficam aqui em cima para que todas as funções possam usá-los)

# Cardápio de Comida
cardapio = [
    {
        "nome": "(ITEM Nº1) Combinado Salmão (16 Peças)",
        "descricao": "4 Sashimi, 4 Uramaki Filadélfia, 4 Hossomaki Salmão, 4 Nigiri Salmão.",
        "preco": 55.00
    },
    {
        "nome": "(ITEM Nº2) Temaki Filadélfia",
        "descricao": "Cone de alga recheado com arroz, salmão, cream cheese e cebolinha.",
        "preco": 28.50
    },
    {
        "nome": " (ITEM Nº3) Hot Filadélfia (8 Peças)",
        "descricao": "Roll frito de salmão e cream cheese, com tarê e cebolinha.",
        "preco": 32.00
    },
    {
        "nome": "(ITEM Nº4) Porção de Sashimi (10 Fatias)",
        "descricao": "10 fatias de salmão fresco. Acompanha wasabi e gengibre.",
        "preco": 38.00
    }
]

# Cardápio de Bebidas
cardapio_bebidas = [
    {"nome": "Coca-Cola (Lata)", "preco": 12.00},
    {"nome": "Fanta Laranja (Lata)", "preco": 10.00},
    {"nome": "Suco de Laranja (Natural 300ml)", "preco": 8.00}
]

# AQUI É A MÁGICA:
# Esta lista vai guardar TODAS as mesas que estão comendo agora.
mesas_abertas = [] 
# Exemplo de como ela vai ficar:
# mesas_abertas = [
#   { "numero_mesa": 5, "cliente": "Ana", "garcom": "Carlos", "carrinho": [], "total": 0.0 },
#   { "numero_mesa": 12, "cliente": "Marcos", "garcom": "Bruno", "carrinho": [...], "total": 55.0 }
# ]


# --- 2. FUNÇÕES AUXILIARES (Pequenas tarefas) ---

def encontrar_mesa(numero_mesa):
    """
    Função simples que procura uma mesa na lista 'mesas_abertas'.
    Retorna a mesa (dicionário) se achar, ou 'None' (nada) se não achar.
    """
    for mesa in mesas_abertas:
        if mesa["numero_mesa"] == numero_mesa:
            return mesa
    return None

def calcular_total_mesa(mesa):
    """Calcula o total de um carrinho e atualiza o 'total' da mesa."""
    total_novo = 0.0
    for item in mesa["carrinho"]:
        subtotal = item["prato"]["preco"] * item["quantidade"]
        total_novo += subtotal
    
    # Atualiza o total no dicionário da mesa
    mesa["total"] = total_novo


def obter_garcom(numero_mesa):
    """Descobre o garçom com base no número da mesa."""
    if 1 <= numero_mesa <= 8:
        return "Carlos (Garçom)"
    elif 9 <= numero_mesa <= 15:
        return "Bruno (Garçom )"
    elif 16 <= numero_mesa <= 24:
        return "Rafael (Garçom )"
    elif 25 <= numero_mesa <= 32:
        return "Lucas (Garçom )"
    elif 33 <= numero_mesa <= 40:
        return "Thiago (Garçom )"
    else:
        return "Garçom não definido" # Segurança


# --- 3. FUNÇÕES PRINCIPAIS (As 3 Ações do Menu) ---

def abrir_nova_mesa():
    """
    AÇÃO 1: Cliente chegou. Pede nome, mesa, e já faz o primeiro pedido.
    """
    print("\n--- [1] ABRIR NOVA MESA ---")
    nome_do_cliente = input("Qual o nome do cliente? ")

    # Loop para validar a mesa
    while True:
        try:
            numero_mesa_str = input(f"Qual o número da mesa (1-40) para {nome_do_cliente}? ")
            numero_mesa = int(numero_mesa_str)
            
            if not (1 <= numero_mesa <= 40):
                print("❌ Erro: Mesa inválida. Somente de 1 a 40.")
                continue # Pede o número de novo
            
            # VERIFICA SE A MESA JÁ ESTÁ ABERTA
            mesa_existente = encontrar_mesa(numero_mesa)
            if mesa_existente:
                print(f"❌ Erro: A Mesa {numero_mesa} já está aberta e sendo usada por {mesa_existente['cliente']}.")
                continue # Pede o número de novo
            
            # Se a mesa é válida e está livre:
            break

        except ValueError:
            print("❌ Por favor, digite apenas números.")

    # Temos um número de mesa válido e livre
    garcom_atendente = obter_garcom(numero_mesa)
    
    # Cria a "comanda" (o dicionário) da mesa
    nova_mesa = {
        "numero_mesa": numero_mesa,
        "cliente": nome_do_cliente,
        "garcom": garcom_atendente,
        "carrinho": [], # O carrinho começa vazio
        "total": 0.0
    }
    
    print(f"\n✅ Mesa {numero_mesa} aberta para {nome_do_cliente} (Garçom: {garcom_atendente})")
    print("Vamos adicionar os primeiros itens...")

    # Adiciona os primeiros itens (chama a Ação 2)
    adicionar_itens_a_mesa(nova_mesa)
    
    # Salva a nova mesa no nosso "banco de dados"
    mesas_abertas.append(nova_mesa)
    print(f"\n--- Comanda da Mesa {numero_mesa} salva no sistema. ---")


def adicionar_itens_a_mesa(mesa_para_adicionar=None):
    """
    AÇÃO 2: Garçom foi na mesa. Pergunta qual mesa e adiciona mais itens.
    Se 'mesa_para_adicionar' for fornecido (pela Ação 1), pula a pergunta.
    """
    if mesa_para_adicionar is None:
        print("\n--- [2] ADICIONAR ITENS A UMA MESA ---")
        try:
            numero_mesa_str = input("Qual o número da mesa que deseja adicionar itens? ")
            numero_mesa = int(numero_mesa_str)
            
            mesa_encontrada = encontrar_mesa(numero_mesa)
            
            if mesa_encontrada is None:
                print(f"❌ Erro: Mesa {numero_mesa} não encontrada ou não está aberta.")
                return # Volta ao menu principal
        except ValueError:
            print("❌ Por favor, digite apenas números.")
            return # Volta ao menu principal
    else:
        # Veio da Ação 1 (abrir_nova_mesa)
        mesa_encontrada = mesa_para_adicionar

    print(f"\n--- Adicionando itens para Mesa {mesa_encontrada['numero_mesa']} ---")

    # --- Loop de COMIDA ---
    while True:
        print("\nCardápio de COMIDAS:")
        for i, item in enumerate(cardapio):
            print(f"  [{i + 1}] {item['nome']} - R$ {item['preco']:.2f}")
        
        escolha_str = input("Digite o número do prato (ou 'N' para pular para bebidas): ").strip().upper()

        if escolha_str == 'N':
            break
        
        try:
            escolha_num = int(escolha_str)
            indice = escolha_num - 1
            
            if 0 <= indice < len(cardapio):
                prato_escolhido = cardapio[indice]
                
                # Pergunta a Quantidade
                while True:
                    try:
                        qtd_str = input(f"Quantas unidades de '{prato_escolhido['nome']}'? ")
                        quantidade = int(qtd_str)
                        if quantidade > 0:
                            break
                        else:
                            print("Digite pelo menos 1.")
                    except ValueError:
                        print("Digite um número.")
                
                # Adiciona no carrinho da mesa
                item_pedido = {"prato": prato_escolhido, "quantidade": quantidade}
                mesa_encontrada["carrinho"].append(item_pedido)
                print(f"✅ {quantidade}x {prato_escolhido['nome']} adicionado(s).")
                
                # Pergunta se quer mais comida
                continuar_comida = input("Adicionar mais COMIDA? (S/N): ").strip().upper()
                if continuar_comida == 'N':
                    break # Sai do loop de COMIDA
            else:
                print("❌ Opção inválida.")
        except ValueError:
            print("❌ Entrada inválida. Digite um número ou 'N'.")
            
    # --- Loop de BEBIDA ---
    # (Exatamente igual ao de comida)
    while True:
        print("\nCardápio de BEBIDAS:")
        for i, item in enumerate(cardapio_bebidas):
            print(f"  [{i + 1}] {item['nome']} - R$ {item['preco']:.2f}")
        
        escolha_str = input("Digite o número da bebida (ou 'N' para finalizar): ").strip().upper()

        if escolha_str == 'N':
            break
        
        try:
            escolha_num = int(escolha_str)
            indice = escolha_num - 1
            
            if 0 <= indice < len(cardapio_bebidas):
                prato_escolhido = cardapio_bebidas[indice]
                
                while True:
                    try:
                        qtd_str = input(f"Quantas unidades de '{prato_escolhido['nome']}'? ")
                        quantidade = int(qtd_str)
                        if quantidade > 0:
                            break
                        else:
                            print("Digite pelo menos 1.")
                    except ValueError:
                        print("Digite um número.")
                
                item_pedido = {"prato": prato_escolhido, "quantidade": quantidade}
                mesa_encontrada["carrinho"].append(item_pedido)
                print(f"✅ {quantidade}x {prato_escolhido['nome']} adicionado(s).")
                
                continuar_bebida = input("Adicionar mais BEBIDA? (S/N): ").strip().upper()
                if continuar_bebida == 'N':
                    break
            else:
                print("❌ Opção inválida.")
        except ValueError:
            print("❌ Entrada inválida. Digite um número ou 'N'.")

    # Atualiza o total da mesa
    calcular_total_mesa(mesa_encontrada)
    print(f"\nItens adicionados. Novo total da Mesa {mesa_encontrada['numero_mesa']}: R$ {mesa_encontrada['total']:.2f}")


def fechar_conta():
    """
    AÇÃO 3: Cliente foi ao caixa. Pede o número da mesa, mostra o total,
    registra o pagamento e remove a mesa da lista 'mesas_abertas'.
    """
    print("\n--- [3] FECHAR CONTA (Pagamento) ---")
    try:
        numero_mesa_str = input("Qual o número da mesa que deseja fechar a conta? ")
        numero_mesa = int(numero_mesa_str)
        
        mesa_para_fechar = encontrar_mesa(numero_mesa)
        
        if mesa_para_fechar is None:
            print(f"❌ Erro: Mesa {numero_mesa} não encontrada ou não está aberta.")
            return # Volta ao menu principal
    except ValueError:
        print("❌ Por favor, digite apenas números.")
        return # Volta ao menu principal

    # Se encontrou a mesa, mostra a conta
    print(f"\n--- FECHAMENTO DA MESA {numero_mesa} ---")
    print(f"Cliente: {mesa_para_fechar['cliente']}")
    print(f"Garçom: {mesa_para_fechar['garcom']}")
    print("---------------------------------")
    print("Itens Consumidos:")
    
    if not mesa_para_fechar["carrinho"]:
        print(" (Nenhum item consumido)")
    
    for item in mesa_para_fechar["carrinho"]:
        prato = item["prato"]
        qtd = item["quantidade"]
        subtotal = prato["preco"] * qtd
        print(f"   - {qtd}x {prato['nome']} - R$ {subtotal:.2f}")
    
    print("---------------------------------")
    print(f"   VALOR TOTAL: R$ {mesa_para_fechar['total']:.2f}")
    
    # Lógica de Pagamento
    print("\nForma de Pagamento:")
    print("[1] Pix")
    print("[2] Cartão de Crédito")
    print("[3] Cartão de Débito")
    
    forma_pagamento_nome = ""
    while True:
        escolha_pagamento = input("Escolha a forma de pagamento (1, 2 ou 3): ")
        if escolha_pagamento == "1":
            forma_pagamento_nome = "Pix"
            break
        elif escolha_pagamento == "2":
            forma_pagamento_nome = "Cartão de Crédito"
            break
        elif escolha_pagamento == "3":
            forma_pagamento_nome = "Cartão de Débito"
            break
        else:
            print("❌ Opção inválida. Digite 1, 2 ou 3.")

    # Geração do Número do Pedido
    numero_aleatorio = random.randint(100, 999) 
    numero_pedido_str = f"TAN-{numero_aleatorio}-12"
    
    print("\n-------------------------------------------")
    print("✅ Pagamento registrado!")
    print(f"O número do pedido é: **{numero_pedido_str}**")
    print(f"Forma de Pagamento: {forma_pagamento_nome}")
    print("Obrigado, voltem sempre!")
    
    # A ETAPA MAIS IMPORTANTE:
    # Remove a mesa da lista de mesas abertas
    mesas_abertas.remove(mesa_para_fechar)


# --- 4. O LOOP PRINCIPAL DO PROGRAMA ---
# (É o menu que fica rodando o tempo todo)

def main():
    print("===========================================")
    print("🍣 BEM-VINDO AO SISTEMA TANOSHIMI 🍣")
    print("===========================================")
    
    while True:
        print("\n--- MENU PRINCIPAL ---")
        print(f"(Mesas abertas agora: {len(mesas_abertas)})")
        print("[1] Abrir Nova Mesa (Cliente chegou)")
        print("[2] Adicionar Itens a uma Mesa (Garçom anotou)")
        print("[3] Fechar Conta (Cliente no caixa)")
        print("[4] Sair do Sistema (Encerrar dia)")
        print("------------------------")
        
        escolha = input("O que deseja fazer? (1, 2, 3 ou 4): ")
        
        if escolha == "1":
            abrir_nova_mesa()
        elif escolha == "2":
            adicionar_itens_a_mesa()
        elif escolha == "3":
            fechar_conta()
        elif escolha == "4":
            if len(mesas_abertas) > 0:
                print(f"ATENÇÃO: Existem {len(mesas_abertas)} mesas que não foram fechadas!")
            #break # Quebra o loop 'while True' e encerra o programa
            else:
                print("\nEncerrando o sistema...")
        else:
            print("❌ Opção inválida. Por favor, escolha 1, 2, 3 ou 4.")

# --- INICIA O PROGRAMA ---
main()