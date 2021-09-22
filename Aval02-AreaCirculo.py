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
D = 0
P = 0
R = 0
A = 0
Pi = 3.14

# Ler variável
P = float(input('Digite o perimetro: '))

# cálculos
D = P / Pi
R = D / 2
A = R * R * Pi

# exibindo resultados na tela
print('O numero da Área é: ', A )
print('\n') # pula uma linha
time.sleep(5) # pausa de  5 segundos
sys.exit # comando de fim do programa