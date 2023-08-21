import math

inicio = input ('Vamos descobrir o valor da Hipotenusa? sim/não ')

if inicio=='sim':
    print('Vamos lá então!')
    n1=int(input ('Digite o valor do cateto oposto: '))
    n2=int(input ('Digite o valor do cateto adjacente: '))
    soma = int( math.sqrt(math.pow(n1, 2) + math.pow(n2, 2)))
    print ('A Hipotenusa vale: ', soma)
elif inicio=='não':
    print('** FIM **')