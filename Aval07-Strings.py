# Configura o idioma em Português
# -*- coding: utf-8 -*-

# Bibliotecas do python
import os
import sys
import time

# Faça um programa para ler os dados de uma pessoa: nome, email, idade, telefone, rua,
# número, cep, bairro, cidade, estado, país e salário. No final exiba um   texto   de   apresentação
# dessa   pessoa   usando   as   regras   de formatação/composição de strings aprendidas nesta aula.
# Cada variável deverá ter  o  seu  respectivo  datatype,  ou  seja,  idade  será  número  inteiro,
# nome  será string, salário será decimal, etc...
os.system('cls')
print('\n')

# Variaveis
menu = ""
aux = 0
nome = ""
email = ""
idade = 0
telefone = 0
rua = ""
numero = 0
cep = 0
bairro = ""
cidade = ""
estado = ""
pais = ""
salario = 0

#Função
def startMenu():
    #Definindo variáveis globais
    global menu
    global aux
    global nome
    global email
    global idade
    global telefone
    global rua
    global numero
    global cep
    global bairro
    global cidade
    global estado
    global pais
    global salario

    # If auxiliador para repetir o relatório caso o usuário queira
    if aux == 0:
        print("-------MENU-------\n"
              "1 - Guardar informações\n"
              "2 - Sair")
        menu = int(input('Digite a opção: '))

        # Caso o usuário queira guardar as informações
        if menu == 1:

            # Entradas
            nome = str(input('Digite seu Nome: '))
            email = str(input('Digite seu E-mail: '))
            idade = int(input('Digite sua Idade: '))
            telefone = int(input('Digite seu Telefone: '))
            rua = str(input('Digite sua Rua: '))
            numero = int(input('Digite seu número: '))
            cep = int(input('Digite seu CEP: '))
            bairro = str(input('Digite seu Bairro: '))
            cidade = str(input('Digite sua Cidade: '))
            estado = str(input('Digite seu Estado: '))
            pais = str(input('Digite seu País: '))
            salario = float(input('Digite seu Salário: '))

            # Formatações
            telefone = str(telefone)
            cep = str(cep)
            telefone = f'{telefone[0:5]}-{telefone[5:]}'
            cep = f'{cep[0:5]}-{cep[5:]}'

            os.system('cls')
            time.sleep(3)

            print('Informações guardadas com sucesso')

            aux = 1
        # Se o usuário escolher a opção sair o programado é finalizado
        else:
            print('Finalizando...')
            exit()

    # Print do relatório completo
    elif aux == 1:
        print(f'Relatório do aluno {nome}\n'
              f'Idade: {idade}\n'
              f'E-mail: {email}\n'
              f'Telefone: {telefone}\n'
              f'Endereço na rua: {rua}\n'
              f'Numero: {numero}\n'
              f'Bairro: {bairro}\n'
              f'CEP: {cep}\n'
              f'Cidade: {cidade}\n'
              f'Estado: {estado}\n'
              f'País: {pais}\n'
              f'Salário: {salario}\n')

        time.sleep(5)

        # Caso o usuário queira repetir
        print("-------Gostaria de repetir?-------\n"
              "1 - Sim\n"
              "2 - Não")

        menu = int(input('Digite a opção: '))

        if menu == 1:
            startMenu()
        else:
            print('Finalizando...')
            exit()

    startMenu()

startMenu()