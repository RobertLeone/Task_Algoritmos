# -*- coding: utf-8 -*-

# Vai ler qual o sexo
def lerSexo():

    sexo = ''

    # Impede que outro caractere seja usado
    while sexo not in ('f','h'):
        sexo = input('Digite o sexo: ').lower()

        # Se incorreto irá exibir mensagem de erro
        if sexo not in ('f','h'):
            print('Tente novamente')
        else:
            pass

    return sexo

# Irá ler o salário
def lerSal():

    salario = float(input('Digite o salário: '))

    return salario

# Vai calcular a média aritmética de 2 salários
def calMedia(saldo, saldo2):

    media = (saldo + saldo2) / 2

    return media

# Irá exibir a mensagem na tela das informações obtidas
def exibir(sexo, saldo, sexo2, saldo2, media):

    if sexo == 'h':
        sexo = 'Homem'

    if sexo2 == 'h':
        sexo2 = 'Homem'

    if sexo == 'f':
        sexo = 'Mulher'

    if sexo2 == 'f':
        sexo2 = 'Mulher'

    else:
        pass

    print(f'''
A média salarial é de R${media:.2f}:
1 - {sexo} recebe R${saldo}
2 - {sexo2} recebe R${saldo2}   
            ''')

# Controle principal
def controle():

    # Variáveis
    sexo = ''
    sexo2 = ''
    saldo = 0
    saldo2 = 0
    media = 0
    menu = 0

    # Menu de opções
    while True:

        print('\n1 - Executar\n2 - Resultados\n3 - Sair')

        menu = int(input('Digite a sua opção: '))

        if menu == 1:

            sexo = lerSexo()
            saldo = lerSal()
            sexo2 = lerSexo()
            saldo2 = lerSal()
            media = calMedia(saldo, saldo2)


        elif menu == 2:

            exibir(sexo, saldo, sexo2, saldo2, media)

        elif menu == 3:

            break

        else:
            pass

controle()