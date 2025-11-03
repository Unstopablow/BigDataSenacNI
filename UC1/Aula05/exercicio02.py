print("\n")
texto1 = "# Exercicio (2º) - Cadastro de Candidatos. #"
print(texto1.upper())
print("\n")

# for i in range(3):
#     try:
#         anonascimento = int(input(f'Digite o ano de nascimento: \n'))
#         idade = 2025 - anonascimento
#         #print(idade)
#         if idade <18:
#             print(f'Não poderá participar')
#             break
#         elif idade >= 18:
#             telefone = str(input(f'Digite um telefone: \n'))
#             email = str(input(f'Digite um email: \n')) 
#             print("="*60,"\n")
#             print(f'{"-_"*10} Detalhes canditato {i+1} {"-_"*9}\n')
#             print(f'Idade do {i+1}º candidato: {idade}')
#             print(f'Telefone do {i+1}º candidato: {telefone}')
#             print(f'Email do {i+1}º candidato: {email}')
#             print("\n","="*60,"\n")
#             print("                Cadastro do novo candidato:")
                    
#     except ValueError:
#         print("Entrada inválida. Tente novamente.")    

for i in range(5):
    try:
        anonascimento = int(input(f'Digite o ano de nascimento: \n'))
        idade = 2025 - anonascimento
        #print(idade)
        if idade <18:
            #print(f'Não poderá participar')
            print(i)
            i = i -1
            print(i)
        elif idade >= 18:
            #telefone = str(input(f'Digite um telefone: \n'))
           # email = str(input(f'Digite um email: \n')) 
           # print("="*60,"\n")
           # print(f'{"-_"*10} Detalhes canditato {i+1} {"-_"*9}\n')
           # print(f'Idade do {i+1}º candidato: {idade}')
           # print(f'Telefone do {i+1}º candidato: {telefone}')
           # print(f'Email do {i+1}º candidato: {email}')
           # print("\n","="*60,"\n")
           # print("                Cadastro do novo candidato:")
            print(i+1)
    except ValueError:
        print("Entrada inválida. Tente novamente.")    