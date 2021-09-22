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
G = 9.8
H = 0
T = 0

# Ler variável
H = float(input('Digite a altura: '))

# cálculos
T = ((2*H/G) ** (1/2))

# exibindo resultados na tela
print('Tempo de queda é: ', T )
print('\n') # pula uma linha
time.sleep(5) # pausa de  5 segundos
sys.exit # comando de fim do programa