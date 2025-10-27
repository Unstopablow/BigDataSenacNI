import random

num1= int(random.uniform(1, 10))
num2= int(random.uniform(1, 10))
num3= int(random.uniform(1, 10))
num4= int(random.uniform(1, 10))

#num1 = 3
#num2=5
#num3=1
print(num1,num2,num3,num4,'\n')

media = (num1+num2+num3+num4)/4
print(media,'\n')
if media > 7:
    print('Aprovado')
elif media >= 5 and media <= 7:
    print('Recuperação')
elif media < 5:
    print('Reprovado')





