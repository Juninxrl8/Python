a = int(input('Digite o valor do primeiro lado do triânagulo: '))
b = int(input('Digite o valor do segundo lado do triânagulo: '))
c = int(input('Digite o valor do terceiro lado do triânagulo: '))

if(a > 0) and (b > 0) and (c > 0 ): # Só mais um jeito de fazer! termos idependentes conectados pelo operador and

    if(a + b > c) and (a + c > b) and (b + c > a):
        #se chegou até aqui significa que os números entregues configuram um triãngulo

        print('')
        if(a != b) and (a != c) and (b != c):
            print('Esse é um conjunto de lado que configuram um triângulo Escaleno')
        elif(a == b) and (a == c) and (b ==c):
            print('Esse é um conjunto de lado que configuram um triângulo Equilátero')
        else:
            print('Esse é um conjunto de lado que configuram um triângulo Isóceles')

    else:
        print('')
        print('Esses números não formam um triângulo ')

else:
    print("")
    print('Esses números não formam um triângulo ')