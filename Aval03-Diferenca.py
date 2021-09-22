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
Dif = 0

# Ler variável
A = float(input('Digite o valor: '))
B = float(input('Digite o valor: '))

#Lógica IF

if A > B:
    Dif = A - B
else:
    Dif = B - A

# sem cálculos

# exibindo resultados na tela
print(f'A diferença é: {Dif}')
print('\n') # pula uma linha
time.sleep(5) # pausa de  5 segundos
sys.exit # comando de fim do programa