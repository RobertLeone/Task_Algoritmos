# Configura o idioma em Português
# -*- coding: utf-8 -*-

# Bibliotecas do python
import os
import sys
import time

menu = ""
AUX = 0
N1 = 0
N2 = 0
N3 = 0
N4 = 0


# Fazer quadro resumo, diagrama de blocos e o código fonte: O usuário deverá digitar  um  ano
# qualquer  e  o  programa  deverá  exibir  uma  mensagem informando  se  o  Ano  digitado  é  bissexto
# ou  se  não  é  bissexto;  (crie  uma variável  do  tipo  string  para  armazenar  a  mensagem  “Bissexto”
# ou  “Não Bissexto”, use a função mod, estruturação de seleção
# Limpa a tela e pula uma linha
os.system('cls')
print('\n')

# Variaveis
menu = ""
ano = 0
M = ""

#Função
def startMenu():

    print("-------DIVISOR-------\n"
          "1 - Ler e Exibir\n"
          "2 - Sair")
    menu = int(input('Digite a opção: '))

    if menu == 1:

        ano = int(input('Digite o ano: '))

        if ano % 4 == 0:
            M = f'O ano de {ano}, é bissexto'
        else:
            M = f'O ano de {ano}, não é bissexto'
    else:

        print('Finalizando...')
        exit()

    print(M)

    startMenu()

startMenu()
