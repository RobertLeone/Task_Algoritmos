# Configura o idioma em Português
# -*- coding: utf-8 -*-

'''
Considere o seguinte caso: Um capital (ValorCapital) aplicado a juros (JUROS) simples
durante 2 anos (Período), sob taxa de juros de 5% ao mês, vai gerar um MONTANTE
qualquer. Faça um programa que a partir da leitura do valor do montante e do período em meses,
determine o valor do capital aplicado. (Verifique na internet a fórmula do juros simples,
sugestão  site  Brasil  Escola).  
Faça  um  menu  com  while  infinito  para controlar  o  programa  e  ao  final
exiba  todas  as  variáveis  do  problema  para  que  o usuário possa conferir os resultados de sua aplicação. 
'''
# Taxa de 5%
tax = 5/100

# Input do período em ano e convertido a mês
def valoresPeriodo():
    periodo = float(input('Digite o período em anos: '))
    periodo = periodo * 12
    return periodo

# Input do montante total
def valoresMontante():
    montante = float(input('Digite o montante total: '))
    return montante 

# Cálculo da taxa de juros simples e do capital     
def capitalTotal(a,b):
    jey = 1+(tax*b)

    capital = a / jey

    return capital

# Processo de exibição dos resultados
def exibirJuros(a,b,c):
    jey = 1+(tax*b)

    print(f'Do montante de {a}\n'
          f'No período de {b/12} anos\n'
          f'A taxa é de {jey:.2f}\n'
          f'E seu capital inicial é de {c:.2f}')

# Controle do menu
def controleOne():
    while True:
        print('1 - Ler\n'
              '2 - Calcular\n'
              '3 - Exibir\n'
              '4 - Sair')
        menu = int(input('Digite o menu: '))

        if menu == 1:
            a = valoresMontante()
            b = valoresPeriodo()
        
        elif menu == 2:
            c = capitalTotal(a, b)
        
        elif menu == 3:
            exibirJuros(a, b, c)

        elif menu == 4:
            exit()
        else:
            print('Item inválido!')

# Chamada da função menu
controleOne()