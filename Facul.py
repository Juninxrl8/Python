dano = int(input('Quanto de Dano recebido (1 a 10) ? '))
esc = int(input('Quanto restou do seu escudo? (1 a 10) '))

if(dano == 10 and esc == 0):
    print('Seu escudo caiu')
    print('Você está morto!!')
else:
    print('')
    print('Conseguiu sobreviviver!!')
    print('Nobre Guerreiro')