# -*- coding: utf-8 -*-
import os
import sys
import time

# estabelece a taxa em 10%
taxaaumento = 1 / 10


def cal_Aumento(salario):
    sal = taxaaumento * salario + salario
    return sal


def mostrar(salario, aumento):
    os.system('cls')
    saida = f'Salario:R$ {salario:.2f} \nAumento:R$ {aumento:.2f}'
    print(saida)
    time.sleep(5)


def executar():
    os.system('cls')
    salario = float(input('\nSalário:'))
    aumento = cal_Aumento(salario)
    mostrar(salario, aumento)
    time.sleep(5)


def controle():
    while True:
        os.system('cls')
        menu = '\n1 executar\n2 sair\nitem:'
        item = int(input(menu))
        if item == 1:
            executar()
        elif item == 2:
            sys.exit()
        else:
            print('Item inválido!');
            time.sleep(2)


# executando o programa
controle()