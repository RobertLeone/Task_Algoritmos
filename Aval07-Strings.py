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
msg = "Olá, meu nome é Robert Leone, moro na Rua Mineradores, 5458 no Bairro do Paraíso,\nCEP: 06532156, São Bernardo do Campo, São Paulo, Brasil." \
"Atualmente tenho 21 anos e meu\nendereço para contato é ruanota@hotmail.com e meu telefone é 940028922.\n" \
"Atualmente sou um estagiário no campo de Análise de Dados e Performance na minha atual empresa ganhando 1000.25 reais,\n" \
"este programa serve apenas como um modelo resumo para eu fazer a tarefa e os dados utilizados acima são fictícios.\n" \
"Estudo na FATEC de São Bernardo do Campo e esta é a atividade para a matéria “Algoritmo e Programação de Computadores”,\nestou utilizando a linguagem Python.\n" \
"Futuramente pretendo me tornar um Data Science, mas por enquanto estou com foco em Análise de Dados e Business Intelligence,\n" \
"futuramente pretendo utilizar esse material para fazer algumas análises de slicing no spark, será bem proveitoso para mim.\n" \
"Portanto, desconsidere todos os erros de português contidos nessa string, ela será meramente guardada para se captar dados fictícios\ncitados acima." \
"Irei utilizar o PyCharm para uma facilidade melhor em mexer com strings, espero que esse arquivo seja proveitoso para conseguir\ntodos os pontos necessários.\n"

# Função
def startMenu():
    # Definindo variáveis globais
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
            nome = str(msg[16:28])
            email = str(msg[193:213])
            idade = int(msg[154:157])
            telefone = int(msg[230:239])
            rua = str(msg[42:53])
            numero = int(msg[55:59])
            cep = int(msg[88:95])
            bairro = str(msg[73:80])
            cidade = str(msg[97:118])
            estado = str(msg[120:129])
            pais = str(msg[131:137])
            salario = float(msg[344:353])

            # Formatações
            telefone = str(telefone)
            cep = str(cep)
            telefone = f'{telefone[0:5]}-{telefone[5:]}'
            cep = f'{cep[0:5]}-{cep[5:]}'

            os.system('cls')
            time.sleep(1)

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

        time.sleep(1)

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