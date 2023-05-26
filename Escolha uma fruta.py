print('Escolha o que desejar')

print('1 - Maçã')
print('2 - Banana')
print('3 - laranja')

produto = int(input('Qual fruta você escolhe ? '))

qtd = int(input('Quantas unidades ? '))

if(produto == 1):
    pagar = qtd * 2.3
    print('Você comprou %i Maçã(s). Valor final: %.2f' %(qtd, pagar))
else:
    if(produto == 2):
        paga = qtd * 3.6
        print('Você comprou %i Banana(s). Valor final: %.2f' %(qtd, paga))
    else:
        if(produto == 3):
            pag = qtd * 1.85
            print('Você comprou %i Laranja(s). Valor final: %.2f' %(qtd, pag))
        else:
            print('Produto inexistente')

#todo aninhamento tem que ter um recuo.