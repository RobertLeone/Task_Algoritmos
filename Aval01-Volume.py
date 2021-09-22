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
VL = 0
R = 0
Pi = 3.14
H = 0

# cálculos
R = float(input('Digite o raio da lata: '))
H = float(input('Digite a altura da lata: '))

# cálculos
VL = Pi*(R**2)*H

# exibindo resultados na tela
print('O volume da lata é: ', VL )
print('\n') # pula uma linha
time.sleep(5) # pausa de  5 segundos
sys.exit # comando de fim do programa
