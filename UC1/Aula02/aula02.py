import random

'''
nota1 = int(input('Digite a primeira nota: '))
nota2 = int(input('Digite a segunda nota: '))

media = (nota1 + nota2) /2
print("A média é: ", media)

nota1 = int(input('Digite a primeira nota:\n'))
nota2 = int(input('Digite a segunda nota:\n'))

print('Resultado da soma:\n', nota1+nota2)
print('Resultado da subtração:\n', nota1-nota2)
print('Resultado da multiplicação:\n', nota1*nota2)
print('Resultado da divisão:\n', nota1/nota2)
print('Resultado do resto da divisão:\n', nota1 ,'/', nota2,'=', nota1%nota2)

#-#-#-#-#-#--#-#-#-#-#----

moto = True
preco = 18.40

if preco > 10:
    print('Aguardar...')
elif preco < 20:
    print('Pedir, mesmo assim')
else:
    print('Não a caminho')

'''

num1= int(random.uniform(1, 10))
num2= int(random.uniform(1, 10))
num3= int(random.uniform(1, 10))

#num1 = 3
#num2=5
#num3=1
print(num1,num2,num3,'\n')

if num1 >= num2 and num1 >= num3:
    if num2 > num3:
        print(num3,num2,num1)
    else:
        print(num2,num3,num1)
elif num2 >= num1 and num2 >= num3:
    if num1 > num3:
        print(num3,num1,num2)
    else:
        print(num1,num3,num2)
elif num3 >= num1 and num3 >= num2:
    if num1 > num2:
        print(num2,num1,num3)
    else:
        print(num1,num2,num3)
