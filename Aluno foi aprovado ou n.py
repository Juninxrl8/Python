Nome = input('Digite o nome do aluno: ')
N1 = float(input('Digite a primeira nota: '))
N2 = float(input('Digite a segunda nota: '))
N3 = float(input('Digite a terceira nota: '))

if(N1 >= 7 and N2 >= 7 and N3 >= 7):
    print('O aluno, %s, Passou de ano' %(Nome))

else:
    print('O aluno, %s, foi reprovado.....' %(Nome))
    print('Estude mais....')