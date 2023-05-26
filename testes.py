print('|Sacolão de frutas! - - - - - - - - |Faça a sua escolha|')

print('1 - Maçã')
print('2 - Banana')
print('3 - Kiwi')
print('4 - Salada')

print('')
escolha = int(input('O que vai levar hoje ? '))
qtd = int(input('Quantas unidades ? '))

if(escolha == 1):
    soma = qtd * 2.30
    print('')
    print('Você comprou {} maçã(s).' .format(qtd))
    print('Valor final, {:.2f}$ reais.' .format(soma))
elif(escolha == 2):
    som = qtd * 1.30
    print('')
    print('Você comprou {} banana(s).' .format(qtd))
    print('Valor final, {:.2f}$ reais.' .format(som))
elif(escolha == 3):
    so = qtd * 3.30
    print('')
    print('Você comprou {} Kiwi(s).' .format(qtd))
    print(f'Valor final, {so:.2f}$ reais.')
elif(escolha == 4):
    somar = qtd * 5
    print('')
    print('Você comprou {} salada(s).' .format(qtd))
    print(f'Valor final: {somar:.2f}$ reais.' )
else:
    print('Esse código de produto não está adicionado no cardápio')
    print('Por favor, atenção!! ')