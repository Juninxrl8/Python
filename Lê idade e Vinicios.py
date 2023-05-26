nome = input('Digite seu nome: ')
idade = int(input('Digite a sua idade: '))

if(nome == 'Vinicius' ):
    print('Olá, Vinicius!')
elif(idade < 18):
    print('%s, você é menor de Idade' %(nome))
elif(idade >= 100):
    print('Possivelmente essa pessoa, %s, é fictícia' %(nome))
else:
    print('Olá, %s, você é maior de idade' %(nome))