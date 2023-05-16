import random

def jogar_advinhação():

    print('Seja vem vindo')

    numero_seceto = random.randrange(1,101)
    tentativas = 0
    pontos_inicial = 1000
    pontos_perdidos_total = 0

    while True: 
        nivel = int(input("Qual nivel de dificuldade? \n Nivel 1 - 20 tentativas \n Nivel 2 - 10 tentativas \n Nivel 3 - 5 tentativas \n:"))
        if nivel == 1:
            tentativas = 20
            break
        elif nivel == 2:
            tentativas = 10
            break
        elif nivel == 3:
            tentativas = 5
            break
        else:
            print('numero nao identificado!')

    for rodada in range (1,tentativas + 1):
        print (f'rodada {rodada} de {tentativas} tentativas')
        num = int(input('Digite um numero: '))
        acertou  = num == numero_seceto
        menor    = num < numero_seceto
        maior    = num > numero_seceto

        pontos_perdidos = abs(num - numero_seceto)
        pontos_perdidos_total = pontos_perdidos_total + pontos_perdidos

        if (acertou):
            print ('Você Acertou !!!')
            break
        else:
            print('Você Errou !!!')
            if (maior):
                print('Voce chutou um numero maior do que deveria')
            elif (menor):
                print('Voce chutou um numero menor do que deveria')

        if rodada == tentativas - 1:
            print('Sua ultima tentativa')

        if rodada == tentativas:
            print('Suas tentativas acabaram')
            print(f'o numero correto é {numero_seceto}')
            
    print (f'Você fez {pontos_inicial - pontos_perdidos_total} pontos')
    print ('Fim do Jogo')
 