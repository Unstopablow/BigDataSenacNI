print("\n")
texto1 = "# Exercicio (2º) - Cadastro de Candidatos. #"
print(texto1.upper())
print("\n")
from datetime import datetime


candidatos_validos = []
historico_canditados = {}

for i in range(3):
    try:
        anonascimento = int(input(f'Digite o ano de nascimento: \n'))
        ano_atual = datetime.now().year
        idade = ano_atual - anonascimento
        #print(idade)
        if idade <18:
            print(f'Candidato menor, não poderá participar')
            continue
        elif idade >= 18:
            telefone = str(input(f'Digite um telefone: \n'))
            email = str(input(f'Digite um email: \n')) 
            print("="*60,"\n")
            print(f'{"-_"*10} Detalhes canditato {i+1} {"-_"*9}\n')
            print(f'Idade do {i+1}º candidato: {idade}')
            print(f'Telefone do {i+1}º candidato: {telefone}')
            print(f'Email do {i+1}º candidato: {email}')
            print("\n","="*60)
            print("================= Cadastro do novo candidato ===============")
            print("="*60,"\n")
            candidatos_validos.append(f' Candidato: {i+1} - Idade: {idade} - Telefone: {telefone} - Email: {email}') 
            print(candidatos_validos) 
            
            #candidatos_validos.append["Candidato": i,"Idade": idade,"Telefone" : telefone,"Email" : email]   
    except ValueError:
        print("Entrada inválida. Tente novamente.")    