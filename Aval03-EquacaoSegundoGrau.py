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

# Ler variável
A = int(input('Digite o valor de A: '))
B = int(input('Digite o valor de B: '))
C = int(input('Digite o valor de C: '))

#Lógica IF

if A > 0:
    D = (B**2) - (4*A*C)
    X1 = int((-B + D**(1/2)) / 2*A)
    X2 = int((-B - D ** (1 / 2)) / 2 * A)
else:
    print("Não possui raiz real")
    exit()
# sem cálculos

# exibindo resultados na tela
print(f'O valor das raizes é: {X1} e {X2}')
print('\n') # pula uma linha
time.sleep(5) # pausa de  5 segundos
sys.exit # comando de fim do programa