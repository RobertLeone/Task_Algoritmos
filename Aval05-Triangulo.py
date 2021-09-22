# Configura o idioma em Português
# -*- coding: utf-8 -*-

#usando módulos do python
import os
import sys
import time

# apagar a tela
os.system('cls')
print('\n')

# variáveis e constantes
A = 0
B = 0
C = 0
T = ""
menu = ""

# input
print("-------TRIANGULO?-------\n"
      "1 - Ler e Exibir\n"
      "2 - Sair")
menu = float(input('Digite a opção: '))

# lógica
if menu ==1:
    A = int(input("Digite o valor de A: "))
    B = int(input("Digite o valor de B: "))
    C = int(input("Digite o valor de C: "))

    if A < B + C and B < A + C and C < A + B:
        T = True
    else:
        T = False
else:
    time.sleep(2)
    exit()

if T == True:
    print("Trata-se de um Triângulo!")
else:
    print("Uma figura qualquer de três lados")

time.sleep(5) # pausa de  5 segundos
sys.exit # comando de fim do programa
