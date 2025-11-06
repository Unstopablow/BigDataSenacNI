resultados = []

for i in range(5):
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
              print(f'\n',"="*40)
              if  media <3:
                     print(f'Aluno: reprovado - média: {media}')
                     situacao_aluno = "Reprovado"
              elif media >= 3 and media <6:
                     print(f'Aluno: recuperação - média: {media}')
                     situacao_aluno = "Recuperação"
              elif media >= 6:
                     print(f'Aluno: aprovado - média: {media}')
                     situacao_aluno = "Aprovado"
              # match media:
              #     case 0| 1| 2:
              #         print(f'Reprovado: média: {media}')
              #     case 3| 4| 5:
              #         print(f'Recuperação: média: {media}')
              #     case 6| 8| 9 | 10:
              #         print(f'Aprovado: média: {media}')
              #     case _:
              #         print(f'Trat excc')
              print("="*40,"\n")
              resultados.append(f'Aluno {i+1} - {situacao_aluno} - média: {media}')
       except:
              print("Entrada inválida. Por favor, tente novamente.")

print(" ","="*(len(resultados)*36))
print(f' | {resultados} |')
print(" ","="*(len(resultados)*36))

