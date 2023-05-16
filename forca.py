import random


def jogar_forca():

    mensagem_abertura()
    palavra_secreta = verificando_arquivos()
    lista = ["_" for letra in palavra_secreta]

    enforcou = False
    acertou = False
    erros = 0

    print(lista)

    while (not enforcou and not acertou):
        chute = input('Digite a Letra: ').upper().strip()
        index = 0

        if chute in palavra_secreta:
            for letra in palavra_secreta:
                if letra == chute:
                    print(f'Você acertou!!! a letra {letra} esta na posição {index}')
                    lista[index] = letra
                index +=1

        else:
            erros += 1
            print(f"Você so tem {6 - erros} vidas")
        print(lista)

        if erros >= 6:
            print(f'A palavra correta era {palavra_secreta}')
            enforcou = True

        if "_" not in lista:
            print('Você acertou a palavra, Parabens!!')
            acertou = True


def mensagem_abertura():
    print('Seja vem a Forca')

def verificando_arquivos():
    arquivo = open("palavras.txt", "r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()
    palavra_secreta = random.choice(palavras).upper()
    return palavra_secreta


if (__name__ == '__main__'):
    jogar_forca()