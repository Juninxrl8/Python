
print('1 = Adição')
print('2 = Subtração')
print('3 = Multiplicação')
print('4 = Divisão')
print('5 = potenciação')
print('')
print('>: Digite qualquer outro Número para SAIR')
print('')

esco = int(input('| Escolha uma operação matemática acima |> '))
#Ou eu poderia criar apenas duas variáveis para servir a todos os 'if', seria até mais recomendado!

if(esco == 1):
    print('')
    x = int(input('Digite o Primeiro Número: '))
    y = int(input('Digite o Segundo Número: '))

    soma = x + y
    print(f'{x:} mais {y:} é igual a: {soma:}')

elif(esco == 2):
    print('')
    r = int(input('Digite o Primeiro Número: '))
    t = int(input('Digite o Segundo Número: '))

    sub = r - t
    print(f'{r:} menos {t:} é igual a: {sub:}')

elif(esco == 3):
    print('')
    u = int(input('Digite o Primeiro Número: '))
    i = int(input('Digite o Segundo Número: '))

    mult = u * i
    print(f'{u:} vezes {i:} é igual a: {mult:}')

elif(esco == 4):
    print('')
    d = int(input('Digite o Primeiro Número: '))
    s = int(input('Digite o Segundo Número: '))

    divi = d / s
    print(f'{d:} dividido {s:} é igual a: {divi:}')

elif(esco == 5):
    print('')
    p = int(input('Digite o Primeiro Número: '))
    o = int(input('Digite o Segundo Número: '))

    poten = p ** o
    print(f'{p:} elevado à {o:}° potência é igual a: {poten:}')

else:
    print('')
    print('Fim da Operação. Você escolheu sair')
    print('------------------------------------')