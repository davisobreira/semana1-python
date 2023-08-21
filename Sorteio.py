import random

num = random.randint(1,10)
print ('Hey! Vou pensar em um número de 1 até 10. Quero ver se voce acerta qual é este.')
n = input('Escolha um número entre 1 e 10: ')
if n==num:
    print('Boa! Acertou. Pensei no número: ' , num)
else :
    print('Errou! Pensei no número: ', num)