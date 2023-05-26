Kwh = float(input('Quantos Kwh? '))
tipo = input('Qual o tipo de Intalação (R, C ou I): ')

if(tipo == 'R' ):
    if Kwh <= 500:
        soma = 0.4
    else:
        soma = 0.65

elif(tipo == 'C'):
    if Kwh <= 1000:
        soma = 0.55
    else:
        soma = 0.6

elif(tipo == 'I'):
    if Kwh <= 5000:
        soma = 0.55
    else:
        soma = 0.6

else:
    print('Instalação inválida')

print('Total a pagar: {}'.format(Kwh * soma))