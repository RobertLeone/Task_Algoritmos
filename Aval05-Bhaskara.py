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
D = 0
X1 = 0
X2 = 0

#Lógica IF

print("*******MENU BHASKARA*******\n1 - Executar\n2 - Informação\n3 - Sair")
menu = int(input("Digite sua opção"))

if menu == 1:
    A = int(input('Digite o valor de A: '))
    B = int(input('Digite o valor de B: '))
    C = int(input('Digite o valor de C: '))

    if A >= 0:
        D = (B**2) - (4*A*C)
        X1 = (-B + (D**(1/2))) / 2*A
        X2 = (-B - (D**(1/2))) / 2*A

    else:
        print("Não possui raiz")
        exit()

elif menu ==2:
    print("Para delta: (B**2) - (4*A*C)\n"
          "Para a primeira raiz: (-B + (D**(1/2))) / 2*A\n"
          "Para a segunda raiz: (-B - (D**(1/2))) / 2*A\n")
    time.sleep(2)
    exit()
else:
    exit()

# sem cálculos

# exibindo resultados na tela
print(f'O valor das raizes é: {X1:.2f} e {X2:.2f}')
print('\n') # pula uma linha
time.sleep(5) # pausa de  5 segundos
sys.exit # comando de fim do programa