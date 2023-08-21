import math

print('***** ÁREA DO TRIÂNGULO *****')
ang = float(input('Informe o valor do ângulo: '))

seno = float(math.sin(math.radians(ang)))
cos = float(math.cos(math.radians(ang)))
tang = float(math.tan(math.radians(ang)))

continua = 's'
while continua == 's':
    calc = str(input('Você quer saber o valor do "seno", "cosseno", ou "tangente"? '))
    match calc:
        case 'seno':
            print('O valor do seno é: ', seno)
            continua = input('Deseja calcular novamente? [s/n]')
        case 'cosseno':
            print('O valor do cosseno é: ', cos)
            continua = input('Deseja calcular novamente? [s/n]')
        case 'tangente':
            print('O valor da tangente é: ', tang)
            continua = input('Deseja calcular novamente? [s/n]')
        case _:
            print('Escreva uma opção válida!'.upper())
print('*** FIM ***')