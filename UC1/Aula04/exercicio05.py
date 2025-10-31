import random

print("\n")
texto1 = "# Exercicio (5º) - Média do Aluno com Optativa. #"
print(texto1.upper())
print("\n")
# Escreva um programa que leia as notas das duas avaliações normais e a nota da avaliação
# optativa dos estudantes de uma turma. Caso o estudante não tenha feito a optativa, deve
# ser fornecido o valor -1. Calcular a média do semestre considerando que a prova optativa
# substitui a nota mais baixa entre as duas primeiras avaliações. Escrever a média e
# mensagens que indiquem se o estudante foi aprovado, reprovado ou se está em
# recuperação, de acordo com as informações abaixo:
# Aprovado: média >= 6.0
# Reprovado: média < 3.0
# Recuperação: média >= 3.0 e < 6.0
# Observação: nota optativa - o estudante decide fazer uma prova extra para melhorar o
# resultado final.

# print(f'Colocar casa decimal :.2f)

try:
    nota_optativa = float(-1)
    primeira_nota = float(input(f'Digite a primeira nota do aluno: \n'))
    segunda_nota = float(input(f'Digite a segunda nota do aluno: \n'))

    pergunta = str(input(f'O aluno realizou a optativa? (Sim/Não) \n')).upper()

    if pergunta == "SIM":
        nota_optativa = float(input(f'Digite a nota da optativa: \n'))
        if segunda_nota >= primeira_nota: #and nota_optativa <= segunda_nota:
            #print(f'substituir av1, {primeira_nota}, {segunda_nota}')
            primeira_nota = nota_optativa
            #print(f'substituir av1, {primeira_nota}, {segunda_nota}')
        elif primeira_nota >= segunda_nota: #and nota_optativa <= primeira_nota:
            #print(f'substituir av2, {primeira_nota}, {segunda_nota}')
            segunda_nota = nota_optativa
            #print(f'substituir av2, {primeira_nota}, {segunda_nota}')
        else:
            print("ERROR1")
    elif pergunta == "NÃO":
        nota_optativa = -1
    else:
        pergunta = "ERROR2"
    media = float((primeira_nota + segunda_nota)/2)
        
    #media = float(random.uniform(1, 10))

    #print(f'Média do aluno é: \n {media}')

    if  media <3:
        print(f'Reprovado: média: {media}')
    elif media >= 3 and media <6:
        print(f'Recuperação: média: {media}')
    elif media >= 6:
        print(f'Aprovado: média: {media}')
    # match media:
    #     case 0| 1| 2:
    #         print(f'Reprovado: média: {media}')
    #     case 3| 4| 5:
    #         print(f'Recuperação: média: {media}')
    #     case 6| 8| 9 | 10:
    #         print(f'Aprovado: média: {media}')
    #     case _:
    #         print(f'Trat excc')
except:
    print("Entrada inválida. Por favor, tente novamente.")


# Aprovado: média >= 6.0
# Reprovado: média < 3.0
# Recuperação: média >= 3.0 e < 6.0


