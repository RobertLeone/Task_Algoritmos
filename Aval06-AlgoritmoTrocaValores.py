# Configura o idioma em Português
# -*- coding: utf-8 -*-

# Bibliotecas do python
import os
import sys
import time

# Definição de variaveis e constantes
menu = ""
AUX = 0
N1 = 0
N2 = 0
N3 = 0
N4 = 0


# Fazer quadro resumo e o código fonte de um algoritmo que use o algoritmo de troca de valores
#para exibir em ordem crescente os quatro números lidos, N1, N2,  N3  e  N4.
#(Este  código  terá  4  IFs  para  ordenar  os  valores  1  para  cada valor)
# Limpa a tela e pula uma linha
os.system('cls')
print('\n')

# Variaveis
menu = ""
N1 = 0
N2 = 0
N3 = 0
N4 = 0
AUX = 0

#Função
def startMenu():

    print("-------DIVISOR-------\n"
          "1 - Ler e Exibir\n"
          "2 - Sair")
    menu = int(input('Digite a opção: '))

    if menu == 1:

        N1 = int(input('Digite o número: '))
        N2 = int(input('Digite o número: '))
        N3 = int(input('Digite o número: '))
        N4 = int(input('Digite o número: '))

        # É necessário que fique com esses IF's para o programa funcionar, o elif só iria pular
        # para a próxima lógica if
        if N1 > N2:
            AUX = N1
            N1 = N2
            N2 = AUX

        if N1 > N3:
            AUX = N1
            N1 = N3
            N3 = AUX

        if N1 > N4:
            AUX = N1
            N1 = N4
            N4 = AUX

        if N2 > N4:
            AUX = N2
            N2 = N4
            N4 = AUX

        if N3 > N4:
            AUX = N3
            N3 = N4
            N4 = AUX

        else:
            pass
    else:
        print('Finalizando...')
        exit()

    print('A ordem é: ', N1, N2, N3, N4)

    startMenu()

startMenu()