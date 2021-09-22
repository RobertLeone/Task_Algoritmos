# Configura o idioma em Português
# -*- coding: utf-8 -*-

# Bibliotecas do python
import os
import sys
import time

menu = ""
A = 0
B = 0
C = 0
D = 0
E = 0
list = []

# Efetuar a leitura de cinco números inteiros e identificar o maior e o menor valores.
# Limpa a tela e pula uma linha
os.system('cls')
print('\n')

#Função
def startMenu():
    print("-------DIVISOR-------\n"
          "1 - Ler e Exibir\n"
          "2 - Sair")
    menu = int(input('Digite a opção: '))

    #Escola do menu
    if menu == 1:

        #Basicamente o dado é gravado na variável e adicionado a uma lista
        A = int(input('Digite o número: '))
        list.append(A)

        B = int(input('Digite o número: '))
        list.append(B)

        C = int(input('Digite o número: '))
        list.append(C)

        D = int(input('Digite o número: '))
        list.append(D)

        E = int(input('Digite o número: '))
        list.append(E)

        # Após isso, basta achar o valor máximo e mínimo
        print("O maior valor é: ", max(list))
        print("O menor valor é: ", min(list))

    else:
        print('Finalizado...')
        exit()

    startMenu()

startMenu()