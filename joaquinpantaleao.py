import random

jogar = True

while jogar:
    print('Jogo de adivinhação com quatro chutes')
    numeroSecreto = random.randint(1, 10)
    acertou = False
    chances = 0
    print('Descubra o número secreto de 1 a 10\n')
    while not acertou and chances < 4:
        chances += 1
        print('\nVocê tem {} chances'.format(5-chances))
        chute = int(input("Digite seu chute: "))

        if chute == numeroSecreto:
            print('Acertou!!')
            acertou = True
            print('Parabéns!')
        elif chute > numeroSecreto:
            print("Chute foi MAIOR que o numero secreto!")
        elif chute < numeroSecreto:
            print("Chute foi MENOR que o numero secreto!")

        if chances == 4 and not acertou:
            print('\nAcabaram suas chances')
        else:
            print('tente novamente')

    print('Quer jogar novamente? s ou n ')
    decisao = str(input())
    if decisao == 's':
        jogar = True
        print("\n" * 20)
    else:
        print("\n" * 20)
        print('Au Revoir')
        jogar = False
