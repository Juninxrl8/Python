# função da dimensão do objeto
def dimensoesObjeto():
    print('-' * 15, 'MENU 1 de 3 DIMENSÃO do OBJETO', '-' * 15)  # printo uma mensagem de abertura do menu

    while True:  # laço de repetição infinito (até que se torne false)
        try:  # aqui eu digo pra ele tentar executar sem erro
            alt = float(input('Qual a altura do objeto? (Em cm) '))  # variavel tipo float que pede altura
            comp = float(input('Qual a comprimento do objeto? (Em cm) '))  # variavel tipo float que pede o comprimento
            larg = float(input('Qual a largura do objeto? (Em cm) '))  # variavel tipo float que pede largura
            volume = alt * comp * larg  # variável que vai multiplicar as anteriores e guardar o valor do volume

            global valor  # aqui eu indico que uma variável do escopo global vai ser alterada

            if (volume < 1000):  # inicio uma condição
                valor = 10  # caso os ifs sejam executados, o valor da variável 'valor' (do escopo global) será alterado
                return volume  # Peço para retornar o valor da variavel volume para o escopo global
            elif (volume >= 1000 and volume < 10000):
                valor = 20
                return volume
            elif (volume >= 10000 and volume < 30000):
                valor = 30
                return volume
            elif (volume >= 30000 and volume < 100000):
                valor = 50
                return volume
            else:  # caso não caia em nenhum dos ifs
                print('O volume do objeto é (em cm³): {}.' .format(volume))
                print('Desculpe! Não trabalhamos com objetos de dimensões tão grandes.')  # vai printar essa mensagem
                print('Por favor, entre com as dimensões desejadas novamente.') # pedir para que indique um novo valor
                continue  # e voltar para o início do while

        except ValueError:  # caso o try n seja bem sucedido
            print('Você digitou alguma dimensão de valor não numérico')  # vai cair na exceção e printar essas mensagens
            print('Por favor, entre com as dimensões desejadas novamente')


# fim da função dimensão


# início da função pesoObjeto
def pesoObjeto():
    print('-' * 15, 'MENU 2 de 3 PESO do OBJETO', '-' * 15)  # printo uma mensagem de abertura do menu
    while True:  # um laço de repetição
        try:  # tentar executar sem erro
            peso = float(input('Qual o peso do objeto? (Em Kg) '))  # peço o peso em Kg

            global mult  # declaro q a variável global 'mult' vai ser alterada

            if (peso <= 0.1):  # abro condições
                mult = 1  # que se forem executadas vão alterar o valor da variavel mult
                break  # encerrando com um break
            elif 0.1 < peso < 1:  # (peso > 0.1) and (peso < 1):
                mult = 1.5
                break
            elif 1 <= peso < 10:  # (peso >= 1) and (peso < 10):
                mult = 2
                break
            elif 10 <= peso < 30:  # (peso >= 10) and (peso < 30):
                mult = 3
                break
            else:  # caso nenhum dos ifs sejas bem sucedidos, vai cair no else
                print('Desculpe! Não aceitamos objetos tão pesados.')  # que vai printar essa mensagem
                continue  # e voltar para o início do laço
        except ValueError:  # caso o try encontre uma exceção do tipo ValueError
            print(
                'Você digitou o peso do objeto com um valor não numérico.')  # ele vai printar essa mensagens e voltar ao início do loop
            print('Por favor, entre com o valor correto.')


# fim da função pesoObjeto


# início da função rotaObjeto
def rotaObjeto():
    print('-' * 15, 'MENU 3 de 3 ROTA do OBJETO', '-' * 15)  # printo uma mensagem de abertura do menu
    while True:  # laço de repetição
        rota = input('Selecione uma rota:\n' +
                     'BR - De Brasília para Rio de Janeiro'
                     '\nBS - De Brasília para São Paulo'  # crio uma variavel que chama um input e já entrega as rotas
                     '\nRB - De Rio de Janeiro para Brasília'  # disponiveis, para que o usuário possa escolher
                     '\nSR - De São Paulo para Rio de Janeiro\n'
                     '>>')
        global multi  # declaro que a variavel do escopo global multi poderá ser alterada

        rota = rota.upper().strip()  # peço para que qualquer letra digitada na variavel seja reconhecida como maiúscula
        # e que qualquer espaço vasio (no início ou no final) seja anulado
        if rota == 'BR':  # abertura de condições
            multi = 1.5  # caso sejam executadas o valor da variavel será mudado
            break  # finalizo com um break
        if rota == 'BS':
            multi = 1.2
            break
        if rota == 'RB':
            multi = 1.5
            break
        if rota == 'SR':
            multi = 1
            break
        else:  # caso todos os ifs sejam ignorados
            print('Você digitou uma rota que não existe.')  # o else será executado exibindo essas mensagens
            print('Por favor, insira a rota desejada novamente.')
            continue  # logo em seguida voltando para o início do laço


# fim da função rotaObjeto


# Programa Principal
print('BEM-VINDO A COMPANHIA DE LOGÍSTICA MAURICIO da SILVA SOUSA JUNIOR')  # Identificador

valor = 0
mult = 0  # variáveis que terão seus valores modificados nas funções
multi = 0

volume = dimensoesObjeto()  # invoco a função
print('O volume do objeto é (em cm³): {}'.format(volume))  # peço que print a variável 'volume' retornada da função dimensoesObjeto()

peso = pesoObjeto()  # invoco a função pesoObjeto()

rota = rotaObjeto()  # invoco a função rotaObjeto()

total = valor * mult * multi  # multiplico o valor das variáveis para me voltar o valor final
print('Total a pagar (R$): {} (dimensões: {} * peso: {} * rota: {})'.format(total, valor, mult,
                                                                            multi))  # exibo o total a pagar e a fórmula usada