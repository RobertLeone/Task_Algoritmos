# Configura o idioma em Português
# -*- coding: utf-8 -*-

# Bibliotecas do python
import os
import sys
import time

# Limpa a tela e pula uma linha
os.system('cls')
print('\n')

# variáveis e constantes
A = 0
B = 0
C = 0
D = 0
menu = ""

# Função criada
def startMenu():
    #Menu com input
    print("-------DIVISOR-------\n"
          "1 - Ler e Exibir\n"
          "2 - Sair")
    menu = int(input('Digite a opção: '))

    #Caso o menu escolhido seja o ler e exibir
    if menu == 1:
        A = int(input("Digite o primeiro número: "))
        B = int(input("Digite o segundo número: "))
        C = int(input("Digite o terceiro número: "))
        D = int(input("Digite o quarto número: "))

        #Aqui foi utilizado vários IF e ELSE's para os números serem mostrados em sequências
        if A % 2 == 0 and A % 3 == 0:
            print("\nPrimeiro número ", A, "é divisível por 2 e 3")
            print("Portanto 2 e 3 são divisores de ", A)
        else:
            print("\nO número", A, "não é divisível por 2 e 3")

        if B % 2 == 0 and B % 3 == 0:
            print("\nSegundo número ", B, "é divisível por 2 e 3")
            print("Portanto 2 e 3 são divisores de ", B)
        else:
            print("\nO número", B, "não é divisível por 2 e 3")

        if C % 2 == 0 and C % 3 == 0:
            print("\nTerceiro número ", C, "é divisível por 2 e 3")
            print("Portanto 2 e 3 são divisores de ", C)
        else:
            print("\nO número", C, "não é divisível por 2 e 3")

        if D % 2 == 0 and D % 3 == 0:
            print("\nQuarto número ", D, "é divisível por 2 e 3")
            print("Portanto 2 e 3 são divisores de ", D)
        else:
            print("\nO número", D, "não é divisível por 2 e 3")

        #Espera um tempo e limpa
        time.sleep(2)
        os.system("cls")

        #Inicia a função novamente para voltar ao menu
        startMenu()

    #O programa só é finalizado se a opção 2 for escolhida
    if menu == 2:
        print("Finalizando...")
        exit()

#Inicia a função
startMenu()

