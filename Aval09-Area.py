# -*- coding: utf-8 -*-
import os
import time


'''
Fazer o quadro resumo, diagrama hierárquico, diagrama de blocos e o código fonte de um programa que leia o Comprimento,
calcule o diâmetro, o raio e a área de um círculo. Ao final exiba Diâmetro, Raio e Área. 
(Faça um menu com as opções necessárias para executar as sub rotinas. )       
Fórmulas que serão usadas:  diametro= comprimento / 3.14 raio=diametro / 2 area=raio * raio * 3.14
'''

def diametro():

    comp = float(input('Digite o comprimento: '))
    diam = comp * 3.14

    return diam

def raio(diam):

    raio = diam / 2

    return raio

def getarea(rai):

    area = (rai**2) * 3.14

    return area

def exibir (area, rai, diam):

    print(f'Área: {area:.2f}\n'
          f'Raio: {rai:.2f}\n'
          f'Diâmetro: {diam}')

def controle():
    while True:
        os.system('cls')
        linhasmenu = '\n1 Ler'
        linhasmenu += '\n2 Calcular'
        linhasmenu += '\n3 Exibir'
        linhasmenu += '\n4 Sair'
        linhasmenu += '\nItem: '
        itemmenu = int ( input ( linhasmenu ) )

        if itemmenu == 1:

            diam = diametro()
            rai = raio(diam)

        elif itemmenu == 2:

            area = getarea(rai)

        elif itemmenu == 3:

            exibir(area, rai, diam)

        elif itemmenu == 4:

            exit()

        else:
            print('\nItem Inválido!')
            time.sleep(2)

controle()
exit()