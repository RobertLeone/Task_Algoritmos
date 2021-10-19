# Configura o idioma em Português
# -*- coding: utf-8 -*-

# Bibliotecas do python
import os
import sys
import time

"""
Task: Faça um programa para ler VALOR de uma prestação e a quantidade de DIAS em atraso. Calcule o valor da 
MULTA com TXMULTA de 2% sobre o VALOR da prestação, calcule o valor total de JUROS proporcional aos dias, com
TXJUROS de 1% ao mês sobre o VALOR também. finalmente calcule o valor a pagar, VLPAGAR. Ao final exiba VALOR,
DIAS, MULTA, JUROS, VLPAGAR. 
"""

menu = 0
txm = 2/100
txj = 1/100
values = 0
day = 0

# Criando uma class
class operationTax:

    # Método construtora, é aqui onde as variáveis serão armazenadas nos atributos
    def __init__(self, a, b,values, day):
        self.txm = a
        self.txj = b
        self.values = values
        self.day = day

    # Função que calcula e imprime o que foi pedido em task
    def operationOne(self):
        multa = self.txm * self.values
        juros = self.txj * 1 / 30 * self.day * self.values
        vlpagar = values + multa + juros

        print(f'\nAqui está o resultado final:\n'
              f'Prestação: {self.values}\n'
              f'Dias de atraso: {self.day}\n'
              f'Multa: {multa:.2f}\n'
              f'Juros: {juros:.2f}\n'
              f'Deve: {vlpagar:.2f}')

        time.sleep(1)

# Enquanto for verdadeiro irá repetir o menu
while True:

    print("\n-------MENU-------\n"
          "1 - Ler\n"
          "2 - Exibir\n"
          "3 - Sair\n")

    menu = int(input('Digite a opção do menu: '))

    # Irá guardar as informações inputadas nas variáveis.
    if menu == 1:

        values = float(input('Digite o valor da prestação: '))
        day = int(input('Digite os dias em atraso: '))

        for x in range(3):
            print('. ', end = '')
            time.sleep(0.5)


        print('Dado amarzenado com sucesso!')

    # Variáveis serão carregadas no objeto e será inicializado o método.
    elif menu == 2:

        stat = operationTax(txm, txj, values, day)
        stat.operationOne()

    else:
        exit()


