# -*- coding: utf-8 -*-

# Vai ler a idade
def lerIdade():

    age = int(input('Digite a sua idade: '))

    return age

# Vai ler o pagamento realizado
def lerPag():

    pag = float(input('Digite o pagamento: '))

    return pag

# Irá exibir o ano e quanto deve a partir de idades acima de 18 anos
def exibirEighten(age, pag):

    # O loop for irá pegar as idades e jogar em l
    for l in age:

        # If irá filtrar apenas as idades menores ou iguais a 18 anos
        if l <= 18:

            # O código basicamente irá pegar o index da idade para ser utilizada na lista de pagamento e pegar o quanto deve
            print(f'A {age.index(l)+1}° pessoa tem {l} anos e deve R${pag[(age.index(l))]:.2f}')

        else:

            # Exclui os valores que não estão abaixo ou iguais a 18
            del pag[(age.index(l))]
            age.remove(l)

    # Assim é possível pegar o valor max e mínimo apenas dos abaixo ou igual a 18
    print(f'O maior pagamento foi de R${max(pag):.2f} e o menor pagamento foi de R${min(pag):.2f}\n')

# Mesma lógica do exibirEighten, porém irá pegar apenas idades acima de 18
def exibirNoteighten(age, pag):

    for l in age:

        if l > 18:

            print(f'A {age.index(l)+1}° pessoa tem {l} anos e deve R${pag[(age.index(l))]:.2f}')

        else:

            del pag[(age.index(l))]
            age.remove(l)

    print(f'O maior pagamento foi de R${max(pag):.2f} e o menor pagamento foi de R${min(pag):.2f}\n')

# Menu controle
def controle():

    # Variáveis
    age = []
    pag = []
    menu = 0
    maior = 0
    menor = 0

    # Menu de opções
    while True:

        print('\n1 - Executar\n2 - Resultados\n3 - Sair\n')

        menu = int(input('Digite a sua opção: '))

        if menu == 1:

            age.append(lerIdade())
            pag.append(lerPag())

        elif menu == 2:

            # Menu de escolha para idades acima de 18 ou não
            while True:

                print('Você quer exibir as idades acima de 18?\n')
                aux = input('Responda com Sim | Não | Sair: \n').lower()

                if aux == 'não':
                    exibirEighten(age, pag)

                elif aux == 'sim':
                    exibirNoteighten(age, pag)

                else:
                    break

        elif menu == 3:

            break

        else:

            pass

controle()