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
H = 0

# Ler variável
B = float(input('Digite o numero da base: '))
H = float(input('Digite o numero da altura: '))

# cálculos
A = (B * H) / 2

# exibindo resultados na tela
print('Área do triângulo é: ', A )
print('\n') # pula uma linha
time.sleep(5) # pausa de  5 segundos
sys.exit # comando de fim do programa