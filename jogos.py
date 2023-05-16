from adivinhacao import jogar_advinhação
from forca import jogar_forca

while True:
    selecionar =  int(input('Qual jogo vode deseja?\n 1 - Forca \n 2 - Advinhação\n'))
    if selecionar == 1:
        print ("Jogo Forca")
        jogar_forca()
        break
    elif selecionar == 2:
        print ("Jodo Advinhação")
        jogar_advinhação()
        break
    else:
        print('Numero nao indetificado!')
